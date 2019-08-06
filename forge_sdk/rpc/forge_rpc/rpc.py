import json
import logging
import random

import pystache
from google.protobuf.any_pb2 import Any

from forge_sdk import did
from forge_sdk import utils
from forge_sdk.protos import protos
from forge_sdk.rpc.forge_rpc.chain import ForgeChainRpc
from forge_sdk.rpc.forge_rpc.event import ForgeEventRpc
from forge_sdk.rpc.forge_rpc.file import ForgeFileRpc
from forge_sdk.rpc.forge_rpc.state import ForgeStateRpc
from forge_sdk.rpc.forge_rpc.statistic import ForgeStatsRpc
from forge_sdk.rpc.forge_rpc.wallet import ForgeWalletRpc

logger = logging.getLogger('rpc')

RAND_NONCE = random.randint(1, 10000)


class ForgeRpc:
    def __init__(self, channel):
        self.chain_rpc = ForgeChainRpc(channel)
        self.event_rpc = ForgeEventRpc(channel)
        self.file_rpc = ForgeFileRpc(channel)
        self.state_rpc = ForgeStateRpc(channel)
        self.stats_rpc = ForgeStatsRpc(channel)
        self.wallet_rpc = ForgeWalletRpc(channel)

    def __getattr__(self, item):
        for stub in [self.chain_rpc, self.event_rpc, self.file_rpc,
                     self.state_rpc, self.stats_rpc, self.wallet_rpc]:
            if hasattr(stub, item):
                return getattr(stub, item)

    def get_single_account_state(self, address):
        """
        GRPC call to get account state of a single address

        Args:
            address(string): address of the account

        Returns:
            :obj:`AccountState`

        """
        if address:
            accounts = self.state_rpc.get_account_state({'address': address})
            account = next(accounts)
            if not utils.is_proto_empty(account):
                return account.state

    def get_single_tether_state(self, address):
        if address:
            tethers = self.state_rpc.get_tether_state({'address': address})
            tether = next(tethers)
            if not utils.is_proto_empty(tether):
                return tether.state

    def get_single_tx_info(self, hash):
        """
        GRPC call to get transaction state of a single hash

        Args:
            hash(string): hash of the transaction

        Returns:
            :obj:`TransactionInfo`

        """
        if hash:
            infos = self.chain_rpc.get_tx(hash)
            info = next(infos)
            if not utils.is_proto_empty(info):
                return info.info

    def get_single_asset_state(self, address):
        """
        GRPC call to get asset state of a single address

        Args:
            address(string): address of the asset

        Returns:
            :obj:`AssetState`

        """
        if address:
            assets = self.state_rpc.get_asset_state({'address': address})
            asset = next(assets)
            if not utils.is_proto_empty(asset):
                return asset.state

    def build_signed_tx(self, itx, wallet, token=None, nonce=RAND_NONCE,
                        type_url=None):
        """
        Build a transaction for user. If wallet has secret key, use the
        provided
        secret key to sign transaction; otherwise, it's assumed that this
        wallet
        is created and kept on forge, and sdk will ask forge to sign the
        transaction with provided token.

        Args:
            itx(:obj:`google.protobuf.any`): encoded itx with type_url
            wallet(:obj:`WalletInfo`): wallet to build the tx
            token(string): only required if wallet doesn't include secret key
            nonce(int): required to be 0 if building a PokeTx

        Returns:
            :obj:`Transaction`

        """

        encoded_itx = utils.encode_to_any(type_url, itx) if (
            type_url and not isinstance(itx, Any)) else itx

        if utils.is_sk_included(wallet) and not token:
            return utils.build_signed_tx_local(itx=encoded_itx,
                                               wallet=wallet,
                                               nonce=nonce,
                                               chain_id=self.chain_id)
        else:
            tx_response = self.chain_rpc.create_tx(encoded_itx,
                                                   wallet.address,
                                                   wallet,
                                                   token,
                                                   nonce)
            if tx_response.code != 0:
                logger.error(f"Error in creating tx: {tx_response}")
            else:
                return tx_response.tx

    def build_multisig_tx(self, tx, wallet, token=None, data=None):
        """
        Build a multisig for transaction. If wallet has secret key, use the
        provided
        secret key to sign transaction; otherwise, it's assumed that this
        wallet
        is created and kept on forge, and sdk will ask forge to sign the
        transaction with provided token.

        Args:
            tx(:obj:`Transaction`): transaction that needs multi-signed
            wallet(:obj:`WalletInfo`): wallet to build the tx
            token(string): only required if wallet doesn't include secret key
            data(bytes): extra data to be included in the multisig

        Returns:
            :obj:`Transaction`

        """
        if utils.is_sk_included(wallet) and not token:
            return utils.build_multisig_tx_local(tx, wallet, data)
        else:
            return self.chain_rpc.multisig(tx, wallet, token, data)

    def get_account_balance(self, address):
        """
        Retrieve the balance of account.

        Args:
            address(string): address of an account on Forge chain

        Returns:
            int

        Examples:
            >>> from forge_sdk.rpc.forge_rpc import wallet
            >>> alice = wallet.create_wallet(moniker='alice',
            passphrase='abc123')
            >>> balance = get_account_balance(alice.wallet.address)

        """
        account_state = self.get_single_account_state(address)
        if account_state:
            return utils.bytes_to_int(account_state.balance.value)

    def is_tx_ok(self, tx_hash):
        """
        Check if a transaction executed successfully

        Args:
            tx_hash(string): hash of the transaction

        Returns:
            bool

        Examples:
            >>> is_tx_ok('txtxtx123')
            False
        """
        tx_state = self.get_single_tx_info(tx_hash)
        if not tx_state:
            logging.error('tx does not exist')
            return False
        elif tx_state.code == 0:
            return True
        else:
            logger.error(f'tx: {tx_hash} failed with code {tx_state.code}')
            return False

    def create_asset(self, type_url, asset, wallet, token=None, **kwargs):
        """
        GRPC call to create asset
        Create asset on the chain. If asset address is not provided in kwargs,
        sdk will calculate and fill the asset address.

        Args:
            type_url(string): type_url for asset data
            asset(:obj:`CreateAssetTx`): asset to be included in itx, can be
            string, bytes,
                or protobuf objects
            wallet(:obj:`WalletInfo`): sender's wallet
            token(string): sender's token

        Returns:
            :obj:`ResponseSendTx`, string

        Examples:
            >>> from forge_sdk import rpc
            >>> user = rpc.create_wallet(moniker='user_alice',
            passphrase='abc123')
            >>> response, asset_address = create_asset('test:test:asset',
            b'sample_asset', user.wallet, user.token)
        """

        itx = utils.build_create_asset_itx(type_url=type_url, asset=asset,
                                           encoded=False, **kwargs)

        tx = self.build_signed_tx(
            itx=utils.encode_to_any('fg:t:create_asset', itx),
            wallet=wallet,
            token=token)

        res = self.chain_rpc.send_tx(tx)

        return res, itx.address

    def update_asset(self, address, type_url, asset, wallet, token=None):
        """
        GRPC call to create asset

        Args:
            type_url(string): type_url for this itx
            address(string): address of asset to update
            asset(object): asset to be updated in itx, can be string, bytes,
                or protobuf objects
            wallet(:obj:`WalletInfo`): sender's wallet
            token(string): sender's token

        Returns:
            :obj:`ResponseSendTx`

        Examples:
            >>> from forge_sdk import rpc
            >>> user = rpc.create_wallet(moniker='user_alice',
            passphrase='abc123')
            >>> response, asset_address = create_asset('test:test:asset',
            b'sample_asset', user.wallet)
            >>> res = update_asset(asset_address, 'test:test:update', b'update
        asset', user.wallet)
        """

        encoded_asset = utils.encode_to_any(type_url, asset)
        update_asset_itx = utils.encode_to_any(
            type_url='fg:t:update_asset',
            data=protos.UpdateAssetTx(
                address=address,
                data=encoded_asset,
            ),
        )
        tx = self.build_signed_tx(
            itx=update_asset_itx,
            wallet=wallet, token=token,
        )
        return self.chain_rpc.send_tx(tx.tx)

    def prepare_exchange(self, exchange_tx, wallet, token=None):
        """
        Add sender's signature to  exchange transaction

        Args:
            exchange_tx(:obj:`ExchangeTx`): ExchangeTx transaction
                sender_wallet(:obj:`WalletInfo`): wallet of the sender
            wallet(:obj:`WalletInfo`): wallet of the sender
            token(string): required if the sender_wallet does not have a
                secret key.

        Returns:
            :obj:`Transaction`

        """
        type_url = 'fg:t:exchange'
        tx = self.build_signed_tx(
            itx=utils.encode_to_any(type_url, exchange_tx),
            wallet=wallet, token=token)
        return tx

    def finalize_exchange(self, tx, wallet, token=None, data=None):
        """
        Multi-sign the exchange tx

        Args:
            tx(:obj:`Transaction`):sender signed transaction
            wallet(:obj:`WalletInfo`): sender's wallet
            token(string): sender's token
            data(bytes): data to be included in the multisig

        Returns:
            :obj:`Transaction`

        """
        return self.build_multisig_tx(tx, wallet, token, data)

    def declare(self, moniker, wallet, token=None, issuer=None, data=None):
        """
        Send DeclareTx

        Args:
            declare_tx(:obj:`DeclareTx`): delclareTx
            wallet(:obj:`WalletInfo`): sender's wallet
            token(string): sender's token

        Returns:
            :obj:`ResponseSendTx`

        Examples:
            >>> from forge_sdk import rpc
            >>> user = rpc.create_wallet(passphrase='abc123')
            >>> declare_tx = protos.DeclareTx(moniker='alice')
            >>> res = declare(declare_tx, user.wallet)

        """
        itx = protos.DeclareTx(moniker=moniker,
                               issuer=issuer,
                               data=data)
        return self.send_itx(type_url='fg:t:declare',
                             tx=itx,
                             wallet=wallet,
                             token=token)

    def account_migrate(self, account_migrate_tx, wallet, token=None):
        """
        Send account_migrate transaction

        Args:
            account_migrate_tx(:obj:`AccountMigrateTx`): account migrate
            transaction
            wallet(:obj:`WalletInfo`): sender's old wallet
            token(string): sender's old wallet token

        Returns:
            :obj:`ResponseSendTx`

        Examples:
            >>> from forge_sdk import rpc
            >>> old_wallet = rpc.create_wallet(moniker='alice',
            passphrase='abc123')
            >>> new_wallet = rpc.create_wallet(passphrase='abc123')
            >>> migrate_tx = protos.AccountMigrateTx(pk=new_wallet.wallet.pk,
            address=new_wallet.wallet.address)
            >>> res = account_migrate(migrate_tx, old_wallet.wallet)
        """

        return self.send_itx(type_url='fg:t:account_migrate',
                             tx=account_migrate_tx,
                             wallet=wallet, token=token)

    def prepare_consume_asset(self, consume_asset_tx, wallet, token=None):
        """
        Add sender/issuer's signature to tx

        Args:
            consume_asset_tx(:obj:`ConsumeAssetTx`): ConsumeAssetTx
            wallet(:obj:`WalletInfo`): wallet of the asset issuer or account
                issued by the asset issuer
            token(string): required if the wallet doesn't have sk

        Returns:
            :obj:`Transaction`

        """
        type_url = 'fg:t:consume_asset'
        tx = self.build_signed_tx(utils.encode_to_any(
            type_url, consume_asset_tx), wallet, token)
        return tx

    def finalize_consume_asset(self, tx, wallet, token=None, data=None):
        """
        Add multisig to the :obj:`ConsumeAssetTx`

        Args:
            tx(:obj:`Transaction`): issuer/account issued by issuer signed
                transaction
            wallet(:obj:`WalletInfo`): wallet of the account that's going to
                consume this asset
            token(string): required if the wallet doesn't have sk
            data(bytes): data to be included in the multisig

        Returns:
            :obj:`Transaction`

        """
        return self.build_multisig_tx(tx, wallet, token, data)

    def create_asset_factory(self, moniker, asset, wallet, token=None,
                             data=None):
        """
        Create Asset Factory

        Args:
            moniker(string): nickname for this asset factory
            asset_factory(:obj:`AssetFactory`): AssetFactory
            wallet(:obj:`WalletInfo`): wallet of the sender
            token(string): required if the wallet does not have a secret key.

        Returns:
            obj:`ResponseSendTx`, string
        """

        return self.create_asset(type_url='fg:x:asset_factory',
                                 moniker=moniker,
                                 asset=asset,
                                 wallet=wallet,
                                 token=token,
                                 data=data)

    def is_template_match_asset(self, template, asset):
        rendered = json.loads(pystache.render(template))
        try:
            asset(**rendered)
            return True
        except Exception as e:
            logger.error(f'Rendered template {rendered} and asset {asset} does'
                         f' not match')
            return False

    def build_asset_factory(self, description, price, template,
                            allowed_spec_args, asset_name,
                            **kwargs):
        """
        Helper function to build an asset factory, which can be used to create
        a asset factory.

        Args:
            limit(int): maximum number of asset this factory can create
            price(:obj:`BigUint`): token price of each asset created
            template(stirng): json string of the template encoded with mustache
            allowed_spec_args(list<string>): fields in template that need to be
                filled with value from :obj:`AcquireAssetTx`
            asset_name(string): the protobuf message encoded as data when
            creating
                asset
            **kwargs: additional parameters

        Returns:
            :obj:`AssetFactory`

        """
        if kwargs.get('type_url') and kwargs.get('data_value'):
            data = utils.encode_to_any(kwargs.get(
                'type_url'), kwargs.get('data_value'))
        else:
            data = None

        factory = protos.AssetFactory(
            description=description,
            limit=int(kwargs.get('limit')),
            price=utils.value_to_biguint(int(price)),
            allowed_spec_args=allowed_spec_args,
            asset_name=asset_name,
            template=template,
            attributes=protos.AssetAttributes(
                transferrable=kwargs.get('transferrable', True),
                ttl=kwargs.get('ttl', 7200)
            ),
            data=data,
        )

        return factory

    def acquire_asset(self, to, spec_datas, type_url, proto_lib, wallet,
                      data=None, token=None):
        """
        Send transaction to acquire asset. Returns the response and calculated
        asset address as a list, corresponding to the spec datas provided.

        Args:
            to(string): address of the assetFactory
            spec_datas(list<:obj:`AcquireAssetTx`>): list of spec datas,
            used to
                generate asset with factory template
            wallet(:obj:`WalletInfo`): wallet of the sender
            data(bytes): optional, data to be included in the
            :obj:`AcquireAssetTx`
            token(string): required if the wallet does not have a secret key.

        Returns:
            :obj:`ResponseSendTx`, list<string>

        """
        acquire_asset_tx, asset_address_list = self.build_acquire_asset_tx(to,
                                                                           spec_datas,
                                                                           type_url,
                                                                           proto_lib,
                                                                           data,
                                                                           )

        return self.send_itx(type_url="fg:t:acquire_asset",
                             tx=acquire_asset_tx,
                             wallet=wallet, token=token), asset_address_list

    def build_acquire_asset_tx(self, to, spec_datas, type_url, proto_lib,
                               data=None):
        factory_state = self.get_asset_factory(to)
        if not factory_state:
            logger.error(f"AssetFactory with address {to} does not exist.")
            return None
        else:
            asset_spec_list = []
            asset_address_list = []
            for spec_data in spec_datas:
                asset_spec = self._build_asset_spec(factory_state,
                                                    type_url,
                                                    spec_data,
                                                    to,
                                                    proto_lib)

                asset_spec_list.append(asset_spec)
                asset_address_list.append(asset_spec.address)

            acquire_asset_tx = protos.AcquireAssetTx(to=to,
                                                     specs=asset_spec_list,
                                                     data=data)
            return acquire_asset_tx, asset_address_list

    def get_asset_factory(self, address):
        state = self.get_single_asset_state(address)
        if not state:
            logger.error(
                f"AssetFactory with address {address} does not exist.")
            return None
        elif state.data.type_url != 'fg:s:asset_factory_state':
            logger.error(f"{address} is not an address for asset factory.")
            return None
        else:
            return utils.parse_to_proto(state.data.value,
                                        protos.AssetFactoryState)

    def _build_asset_spec(self, factory_state, type_url, spec_data,
                          factory_address, proto_lib):
        expected_args = factory_state.allowed_spec_args
        for arg in expected_args:
            if arg not in spec_data:
                logger.error(f"{arg} is not found in {spec_data}.")
                return None

        # apply specs to create new params
        try:
            asset_params = json.loads(pystache.render(
                factory_state.template, spec_data))
            asset_proto = getattr(proto_lib, factory_state.asset_name)
            asset = asset_proto(**asset_params)
        except Exception as e:
            logger.error(
                f"Provided spec data can't be parsed   with factory "
                f"template "
                f"{factory_state.template}")
            return None

        # apply params to createAssetTx and calculate address
        tx_params = {
            'readonly': True,
            'parent': factory_address,
        }
        for attribute in factory_state.attributes.DESCRIPTOR.fields:
            tx_params[attribute.name] = getattr(factory_state.attributes,
                                                attribute.name)

        create_asset_itx = utils.build_create_asset_itx(type_url=type_url,
                                                        asset=asset,
                                                        encoded=False,
                                                        **tx_params)

        return protos.AssetSpec(address=create_asset_itx.address,
                                data=json.dumps(spec_data))

    def send_itx(self, tx, wallet, token=None, type_url=None,
                 nonce=RAND_NONCE):
        """
        GRPC call to send inner transaction

        Args:
            type_url(string): type_url for this itx
            tx(:obj:`protos.object`): transactions defined in protos
            wallet(:obj:`WalletInfo`): sender's wallet
            token(string): sender's token
            nonce(int): need to be set to 0 if itx is pokeTx

        Returns:
            :obj:`ResponseSendTx`

        """
        tx = self.build_signed_tx(
            itx=tx,
            wallet=wallet,
            token=token,
            nonce=nonce,
            type_url=type_url,
        )
        return self.chain_rpc.send_tx(tx)

    def stake_for_node(self, to, value, wallet, token=None, message=None):
        stake_address = did.get_stake_address(wallet.address, to)
        stake_itx = protos.StakeTx(
            to=to,
            value=utils.int_to_bigsint(value),
            message=message,
            address=stake_address,
            data=utils.encode_to_any('fg:x:stake_node',
                                     protos.StakeForNode())
        )
        tx = self.build_signed_tx(type_url='fg:t:stake',
                                  itx=stake_itx,
                                  wallet=wallet,
                                  token=token)
        return self.chain_rpc.send_tx(tx)

    def deploy_protocol(self, text, wallet, token=None):
        """
        This helper function helps deploy a pre-compiled transaction protocol
        Args:
            text(string): output of forge compiler; a precompiled and encoded
                :obj:`DeployProtocolTx`
            wallet(:obj:`WalletInfo`): wallet to build the tx
            token(string): only required if wallet doesn't include secret key

        Returns:
            :obj:`ResponseSendTx`
        """
        itx = utils.parse_to_proto(utils.multibase_b64decode(text),
                                   protos.DeployProtocolTx)

        itx.address = did.get_tx_address(itx)
        return self.send_itx(tx=itx, wallet=wallet, token=token,
                             type_url='fg:t:deploy_protocol',
                             nonce=0)

    def poke(self, wallet, token=None):
        itx = utils.build_poke_itx()
        return self.send_itx(tx=itx, wallet=wallet, token=token, nonce=0)

    def transfer(self, wallet, to, value=None, assets=None, data=None, token=None):
        itx = utils.build_transfer_itx(to, value, assets, data)
        return self.send_itx(tx=itx, wallet=wallet, token=token)
