import logging
import random
from google.protobuf.any_pb2 import Any

from forge_sdk import utils
from forge_sdk.protos import protos
from forge_sdk.rpc.forge_rpc.chain import ForgeChainRpc
from forge_sdk.rpc.forge_rpc.state import ForgeStateRpc
from forge_sdk.rpc.forge_rpc.statistic import ForgeStatsRpc

logger = logging.getLogger('helper-rpc')

RANDOM_NONCE = random.randint(1, 10000)

class ForgeRpcHelper:

    def __init__(self, channel, chain_id):
        self.chain_id = chain_id
        self.chain_rpc = ForgeChainRpc(channel)
        self.state_rpc = ForgeStateRpc(channel)
        self.stats_rpc = ForgeStatsRpc(channel)

    def fetch_account(self, address):
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

    def fetch_balance(self, address):
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
        account_state = self.fetch_account(address)
        if account_state:
            return utils.bytes_to_int(account_state.balance.value)

    def fetch_tx(self, tx_hash):
        """
        GRPC call to get transaction state of a single hash

        Args:
            tx_hash(string): hash of the transaction

        Returns:
            :obj:`TransactionInfo`

        """
        if hash:
            infos = self.chain_rpc.get_tx(tx_hash)
            info = next(infos)
            if not utils.is_proto_empty(info):
                return info.info

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
        tx_state = self.fetch_tx(tx_hash)
        if not tx_state:
            logging.error('tx does not exist')
            return False
        elif tx_state.code == 0:
            return True
        else:
            logger.error(f'tx: {tx_hash} failed with code {tx_state.code}')
            return False

    def fetch_asset(self, address):
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

    def build_unsigned_tx(self, itx, wallet, **kwargs):
        if not isinstance(itx, Any):
            itx = utils.to_any(itx)
        delegatee = kwargs.get('delegatee')
        params = {
            'from': delegatee if delegatee else wallet.address,
            'delegator': wallet.address if delegatee else None,
            'nonce': kwargs.get('nonce', RANDOM_NONCE),
            'chain_id': self.chain_id,
            'pk': wallet.pk,
            'itx': itx,
            'gas': kwargs.get('gas'),
        }
        return protos.Transaction(**params)

    def build_tx(self, itx, wallet, **kwargs):

        unsigned_tx = self.build_unsigned_tx(
                itx=itx, wallet=wallet, **kwargs
        )
        signed_tx = utils.sign_tx(tx=unsigned_tx,
                                  wallet=wallet)
        return signed_tx

    def send_itx(self, itx, wallet, **kwargs):
        tx = self.build_tx(itx=itx,
                           wallet=wallet,
                           **kwargs)
        return self.chain_rpc.send_tx(tx, commit=kwargs.get('commit'))
