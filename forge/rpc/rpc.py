import logging

import grpc

from forge import protos
from forge import utils
from forge.rpc.chain import RpcChain
from forge.rpc.event import RpcEvent
from forge.rpc.file import RpcFile
from forge.rpc.state import RpcState
from forge.rpc.statistic import RpcStatistic
from forge.rpc.wallet import RpcWallet


class ForgeRpc:
    __wallet_type = protos.WalletType(pk=0, hash=1, address=1)

    def __init__(self, socket):
        """
        Init Forge RPC with given socket.

        Args:
            socket: string of TCP/UDS socket
        """
        self.chan = grpc.insecure_channel(socket)
        self.logger = logging.getLogger(__name__)

        self.chain = RpcChain(self.chan)
        self.create_tx = self.chain.create_tx
        self.send_tx = self.chain.send_tx
        self.get_tx = self.chain.get_tx
        self.get_block = self.chain.get_block
        self.get_unconfirmed_tx = self.chain.get_unconfirmed_tx
        self.get_chain_info = self.chain.get_chain_info
        self.search = self.chain.search
        self.get_net_info = self.chain.get_net_info
        self.get_validators_info = self.chain.get_validators_info
        self.get_config = self.chain.get_config
        self.multisig = self.chain.multisig
        self.get_asset_address = self.chain.get_asset_address

        self.event = RpcEvent(self.chan)
        self.subscribe = self.event.subscribe
        self.unsubscribe = self.event.unsubscribe

        self.state = RpcState(self.chan)
        self.get_account_state = self.state.get_account_state
        self.get_asset_state = self.state.get_asset_state
        self.get_forge_state = self.state.get_forge_state
        self.get_stake_state = self.state.get_stake_state  # test

        self.file = RpcFile(self.chan)
        self.store_file = self.file.store_file
        self.load_file = self.file.load_file

        self.wallet = RpcWallet(self.chan)
        self.create_wallet = self.wallet.create_wallet
        self.load_wallet = self.wallet.load_wallet
        self.recover_wallet = self.wallet.recover_wallet
        self.remove_wallet = self.wallet.remove_wallet
        self.list_wallet = self.wallet.list_wallet
        self.declare_node = self.wallet.declare_node

        self.statistic = RpcStatistic(self.chan)
        self.list_asset_transactions = self.statistic.list_asset_transactions
        self.list_transactions = self.statistic.list_transactions

    def send_itx(self, type_url, itx, wallet, token, nonce=1):
        encoded_itx = utils.encode_to_any(type_url, itx)
        tx = self.create_tx(
            itx=encoded_itx, from_address=wallet.address,
            wallet=wallet, token=token, nonce=nonce
        )
        return self.send_tx(tx.tx)

    def create_asset(self, type_url, asset, wallet, token):
        encoded_asset = utils.encode_to_any(type_url, asset)
        create_asset_itx = utils.encode_to_any(
            type_url='fg:t:create_asset',
            data=protos.CreateAssetTx(data=encoded_asset),
        )
        tx = self.create_tx(
            create_asset_itx, wallet.address, wallet, token,
        )
        return self.send_tx(tx.tx)

    def update_asset(self, type_url, address, asset, wallet, token):
        encoded_asset = utils.encode_to_any(type_url, asset)
        update_asset_itx = utils.encode_to_any(
            type_url='fg:t:update_asset',
            data=protos.UpdateAssetTx(
                address=address,
                data=encoded_asset,
            ),
        )
        tx = self.create_tx(
            update_asset_itx, wallet.address, wallet, token,
        )
        return self.send_tx(tx.tx)

    def get_single_account_state(self, address):
        if address:
            accounts = self.get_account_state({'address': address})
            account = next(accounts)
            if utils.is_proto_empty(account):
                return None
            else:
                return account.state

    def get_single_tx_info(self, hash):
        if hash:
            infos = self.get_tx(hash)
            info = next(infos)
            if utils.is_proto_empty(info):
                return None
            else:
                return info.info

    def get_single_asset_state(self, address):
        if address:
            assets = self.get_asset_state({'address': address})
            asset = next(assets)
            if utils.is_proto_empty(asset):
                return None
            else:
                return asset.state

    def get_nonce(self, address):
        account = self.get_single_account_state(address)
        return account.nonce

    def multisig_consume_asset_tx(self, tx, wallet, token, data):
        return self.multisig(tx, wallet, token, data=data)
