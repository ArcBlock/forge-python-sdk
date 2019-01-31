import logging

import grpc

from forge import protos
from forge import utils
from forge.rpc.chain import RpcChain
from forge.rpc.event import RpcEvent
from forge.rpc.file import RpcFile
from forge.rpc.state import RpcState
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

        self.event = RpcEvent(self.chan)
        self.subscribe = self.event.subscribe
        self.unsubscribe = self.event.unsubscribe

        self.state = RpcState(self.chan)
        self.get_account_state = self.state.get_account_state
        self.get_asset_state = self.state.get_asset_state
        self.get_channel_state = self.state.get_channel_state
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

    def send_itx(self, type_url, itx, wallet, token=''):
        encoded_itx = utils.encode_to_any(type_url, itx)
        nonce = self.get_nonce(wallet.address)
        tx_builder = self.create_tx(
            encoded_itx, wallet.address, nonce,
            wallet, token,
        )
        return self.send_tx(tx_builder.tx)

    def get_nonce(self, address):
        accounts = self.get_account_state({'address': address})
        account = next(accounts)
        if not account:
            self.logger.error("Account doesn't exist!")
        else:
            return account.state.nonce
