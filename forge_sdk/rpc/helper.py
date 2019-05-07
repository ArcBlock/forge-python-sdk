import logging
from datetime import datetime

from forge_sdk import did
from forge_sdk import utils
from forge_sdk.protos import protos
from forge_sdk.rpc.forge_rpc import chain as chain_rpc
from forge_sdk.rpc.forge_rpc import state as state_rpc

logger = logging.getLogger('rpc-helper')


def get_single_account_state(address):
    """
    GRPC call to get account state of a single address

    Args:
        address(string): address of the account

    Returns:
        :obj:`AccountState`

    """
    if address:
        accounts = state_rpc.get_account_state({'address': address})
        account = next(accounts)
        if utils.is_proto_empty(account):
            return None
        else:
            return account.state


def get_single_tx_info(hash):
    """
    GRPC call to get transaction state of a single hash

    Args:
        hash(string): hash of the transaction

    Returns:
        :obj:`TransactionInfo`

    """
    if hash:
        infos = chain_rpc.get_tx(hash)
        info = next(infos)
        if utils.is_proto_empty(info):
            return None
        else:
            return info.info


def get_single_asset_state(address):
    """
    GRPC call to get asset state of a single address

    Args:
        address(string): address of the asset

    Returns:
        :obj:`AssetState`

    """
    if address:
        assets = state_rpc.get_asset_state({'address': address})
        asset = next(assets)
        if not utils.is_proto_empty(asset):
            return asset.state


def build_tx(itx, wallet, token=None, nonce=1):
    """
    Build a transaction for user. If wallet has secret key, use the provided
    secret key to sign transaction; otherwise, it's assumed that this wallet
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
    if _is_sk_included(wallet) and not token:
        return _build_tx(itx, wallet, nonce)
    else:
        tx_response = chain_rpc.create_tx(itx, wallet.address, wallet, token,
                                          nonce)
        if tx_response.code != 0:
            logger.error(f"Error in creating tx: {tx_response}")
        else:
            return tx_response.tx


def build_multisig(tx, wallet, token=None, data=None):
    """
    Build a multisig for transaction. If wallet has secret key, use the provided
    secret key to sign transaction; otherwise, it's assumed that this wallet
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
    if _is_sk_included(wallet) and not token:
        return _build_multisig(tx, wallet, data)
    else:
        return chain_rpc.multisig(tx, wallet, token, data)


def poke(wallet, token=None):
    """
    Send a Poke Transaction.

    Args:
        token(string): required if the wallet does not have a secret key.

    Returns:
        :obj:`ResponseSendTx`

    Examples:
        >>> from forge_sdk.rpc.forge_rpc import wallet
        >>> alice = wallet.create_wallet(moniker='alice', passphrase='abc123')
        >>> res = poke(alice.wallet)
        >>> assert res.hash

    """
    type_url = 'fg:t:poke'
    poke_tx = protos.PokeTx(date=str(datetime.utcnow().date()),
                            address='zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz')

    return send_itx(type_url, poke_tx, wallet, token, 0)


def transfer(transfer_tx, wallet, token=None):
    """
    Send a Transfer transaction.

    Args:
        transfer_tx(:obj:`TransferTx`): transfer inner transaction
        wallet(:obj:`WalletInfo`): wallet of the sender
        token(string): required if the wallet does not have a secret key.

    Returns:
        :obj:`ResponseSendTx`

    Examples:
        >>> from forge_sdk.rpc.forge_rpc import wallet
        >>> alice = wallet.create_wallet(moniker='alice', passphrase='abc123')
        >>> mike = wallet.create_wallet(moniker='mike', passphrase='abc123')
        >>> transfer_tx = protos.TransferTx(to=mike.wallet.address, value = utils.int_to_biguint(10))
        >>> res = transfer(transfer_tx, alice.wallet)
        >>> assert res.hash

    """
    type_url = 'fg:t:transfer'
    return send_itx(type_url, transfer_tx, wallet, token)


def get_account_balance(address):
    """
    Retrieve the balance of account.

    Args:
        address(string): address of an account on Forge chain

    Returns:
        int

    Examples:
        >>> from forge_sdk.rpc.forge_rpc import wallet
        >>> alice = wallet.create_wallet(moniker='alice', passphrase='abc123')
        >>> balance = get_account_balance(alice.wallet.address)

    """
    account_state = get_single_account_state(address)
    if account_state:
        return utils.bytes_to_int(account_state.balance.value)


def is_tx_ok(tx_hash):
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
    tx_state = get_single_tx_info(tx_hash)
    if not tx_state:
        logging.error('tx does not exist')
        return False
    elif tx_state.code == 0:
        return True
    else:
        logger.error(f'tx: {tx_hash} failed with code {tx_state.code}')
        return False


def create_asset(type_url, asset, wallet, token=None, **kwargs):
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
        >>> user = rpc.create_wallet(moniker='user_alice', passphrase='abc123')
        >>> response, asset_address = create_asset('test:test:asset', b'sample_asset', user.wallet, user.token)
    """

    encoded_asset = utils.encode_to_any(type_url, asset)
    params = {
        'moniker': kwargs.get('moniker'),
        'readonly': kwargs.get('readonly'),
        'transferrable': kwargs.get('transferrable'),
        'ttl': kwargs.get('ttl'),
        'parent': kwargs.get('parent'),
        'data': encoded_asset,
    }
    if not kwargs.get('address'):
        itx_no_address = protos.CreateAssetTx(**params)
        asset_address = did.get_asset_address(wallet.address,
                                              itx_no_address)
        params['address'] = asset_address
    else:
        params['address'] = kwargs.get('address')
    itx = protos.CreateAssetTx(**params)

    tx = build_tx(
        utils.encode_to_any('fg:t:create_asset', itx), wallet, token,
    )
    res = chain_rpc.send_tx(tx)
    return res, itx.address


def update_asset(address, type_url, asset, wallet, token=None):
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
        >>> user = rpc.create_wallet(moniker='user_alice', passphrase='abc123')
        >>> response, asset_address = create_asset('test:test:asset', b'sample_asset', user.wallet)
        >>> res = update_asset(asset_address, 'test:test:update', b'update asset', user.wallet)
    """

    encoded_asset = utils.encode_to_any(type_url, asset)
    update_asset_itx = utils.encode_to_any(
        type_url='fg:t:update_asset',
        data=protos.UpdateAssetTx(
            address=address,
            data=encoded_asset,
        ),
    )
    tx = chain_rpc.create_tx(
        update_asset_itx, wallet.address, wallet, token,
    )
    return chain_rpc.send_tx(tx.tx)


def prepare_exchange(exchange_tx, wallet, token=None):
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
    tx = build_tx(utils.encode_to_any(type_url, exchange_tx),
                  wallet, token)
    return tx


def finalize_exchange(tx, wallet, token=None, data=None):
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
    return build_multisig(tx, wallet, token, data)


def declare(declare_tx, wallet, token=None):
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
    type_url = 'fg:t:declare'
    return send_itx(type_url, declare_tx, wallet, token)


def account_migrate(account_migrate_tx, wallet, token=None):
    """
    Send account_migrate transaction

    Args:
        account_migrate_tx(:obj:`AccountMigrateTx`): account migrate transaction
        wallet(:obj:`WalletInfo`): sender's old wallet
        token(string): sender's old wallet token

    Returns:
        :obj:`ResponseSendTx`

    Examples:
        >>> from forge_sdk import rpc
        >>> old_wallet = rpc.create_wallet(moniker='alice', passphrase='abc123')
        >>> new_wallet = rpc.create_wallet(passphrase='abc123')
        >>> migrate_tx = protos.AccountMigrateTx(pk=new_wallet.wallet.pk, address=new_wallet.wallet.address)
        >>> res = account_migrate(migrate_tx, old_wallet.wallet)
    """
    type_url = 'fg:t:account_migrate'
    return send_itx(type_url, account_migrate_tx, wallet, token)


def prepare_consume_asset(consume_asset_tx, wallet, token=None):
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
    tx = build_tx(utils.encode_to_any(
        type_url, consume_asset_tx), wallet, token)
    return tx


def finalize_consume_asset(tx, wallet, token=None, data=None):
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
    return build_multisig(tx, wallet, token, data)


def create_asset_factory(moniker, asset_factory, wallet, token=None):
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
    return create_asset(type_url='fg:x:asset_factory',
                        asset=asset_factory,
                        wallet=wallet,
                        token=token,
                        moniker=moniker)


def acquire_asset(acquire_asset_tx, wallet, token=None):
    """
    Send transaction to acquire asset

    Args:
        acquire_asset_tx(:obj:`AcquireAssetTx`): AcquireAssetTx
        wallet(:obj:`WalletInfo`): wallet of the sender
        token(string): required if the wallet does not have a secret key.

    Returns:
        :obj:`ResponseSendTx`

    """
    return send_itx('fg:t:acquire_asset', acquire_asset_tx, wallet, token)


def send_itx(type_url, tx, wallet, token, nonce=1):
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
    encoded_itx = utils.encode_to_any(type_url, tx)
    tx = build_tx(
        itx=encoded_itx,
        wallet=wallet,
        token=token,
        nonce=nonce
    )
    return chain_rpc.send_tx(tx)


def _is_sk_included(wallet):
    assert (type(wallet) == protos.WalletInfo)
    return wallet.sk and not wallet.sk == b''


def _build_tx(itx, wallet, nonce):
    __chain_id = chain_rpc.get_chain_info().info.network
    params = {
        'from': wallet.address,
        'nonce': nonce,
        'chain_id': __chain_id,
        'pk': wallet.pk,
        'itx': itx
    }
    params['signature'] = _sign_tx(wallet, protos.Transaction(**params))
    return protos.Transaction(**params)


def _build_multisig(tx, wallet, data):
    params = {
        'from': getattr(tx, 'from'),
        'nonce': tx.nonce,
        'chain_id': tx.chain_id,
        'pk': tx.pk,
        'signature': tx.signature,
        'itx': tx.itx,
        'signatures': [protos.Multisig(
            signer=wallet.address,
            pk=wallet.pk,
            data=data,
        )]
    }
    unmultisig_tx = protos.Transaction(**params)
    params['signatures'] = [protos.Multisig(
        signer=wallet.address,
        pk=wallet.pk,
        signature=_sign_tx(wallet, unmultisig_tx),
        data=data
    )]
    return protos.Transaction(**params)


def _sign_tx(wallet, tx):
    did_type = did.AbtDid.parse_type_from_did(wallet.address)
    tx_hash = did_type.hasher.hash(tx.SerializeToString())
    signature = did_type.signer.sign(tx_hash, wallet.sk)
    return signature
