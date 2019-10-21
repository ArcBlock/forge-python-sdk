import json
import logging
import os

import grpc
from forge_sdk.config import ForgeConfig
from forge_sdk.rpc import ForgeRpcHelper
from forge_sdk.rpc.forge_rpc.chain import ForgeChainRpc
from forge_sdk.rpc.forge_rpc.event import ForgeEventRpc
from forge_sdk.rpc.forge_rpc.file import ForgeFileRpc
from forge_sdk.rpc.forge_rpc.state import ForgeStateRpc
from forge_sdk.rpc.forge_rpc.statistic import ForgeStatsRpc
from forge_sdk.rpc.forge_rpc.wallet import ForgeWalletRpc
from forge_sdk.utils import itx as itx_utils, tx as tx_util
from forge_sdk import utils

logger = logging.getLogger('forge-conn')


def send_forge_transaction(tx_func):
    def inner(conn, **kwargs):
        itx_func = tx_func.__name__ + '_itx'
        itx = kwargs.get('itx', getattr(itx_utils, itx_func)(**kwargs))
        return conn.send_itx(itx, **kwargs)

    return inner


class ForgeConn:
    def __init__(self, grpc_sock=None):
        if not grpc_sock:
            grpc_sock = os.environ.get('FORGE_SOCK_GRPC', '127.0.0.1:27210')

        logger.info(f'Connecting to socket {grpc_sock}')

        self._basic_set_up(grpc_sock)

        # chain rpc
        self.send_tx = self._chain_rpc.send_tx
        self.get_tx = self._chain_rpc.get_tx
        self.get_block = self._chain_rpc.get_block
        self.search = self._chain_rpc.search
        self.get_unconfirmed_tx = self._chain_rpc.get_unconfirmed_tx
        self.get_chain_info = self._chain_rpc.get_chain_info
        self.get_net_info = self._chain_rpc.get_net_info
        self.get_validators_info = self._chain_rpc.get_validators_info
        self.get_config = self._chain_rpc.get_config
        self.get_blocks = self._chain_rpc.get_blocks
        self.get_node_info = self._chain_rpc.get_node_info

        # event rpc
        self.subscribe = self._event_rpc.subscribe
        self.unsubscribe = self._event_rpc.unsubscribe

        # state rpc
        self.get_account_state = self._state_rpc.get_account_state
        self.get_asset_state = self._state_rpc.get_asset_state
        self.get_stake_state = self._state_rpc.get_stake_state
        self.get_tether_state = self._state_rpc.get_tether_state
        self.get_forge_state = self._state_rpc.get_forge_state
        self.get_forge_token = self._state_rpc.get_forge_token

        # stats rpc
        self.get_forge_stats = self._stats_rpc.get_forge_stats
        self.list_assets = self._stats_rpc.list_assets
        self.list_stakes = self._stats_rpc.list_stakes
        self.list_top_accounts = self._stats_rpc.list_top_accounts
        self.list_blocks = self._stats_rpc.list_blocks
        self.get_health_status = self._stats_rpc.get_health_status
        self.list_asset_transactions = self._stats_rpc.list_asset_transactions
        self.list_transactions = self._stats_rpc.list_transactions
        self.list_tethers = self._stats_rpc.list_tethers

        # wallet rpc
        self.create_wallet = self._wallet_rpc.create_wallet
        self.load_wallet = self._wallet_rpc.load_wallet
        self.recover_wallet = self._wallet_rpc.recover_wallet
        self.remove_wallet = self._wallet_rpc.remove_wallet
        self.declare_node = self._wallet_rpc.declare_node

        # Config
        self.config = self._get_config()
        self.token_decimal = self.config.decimal
        self.symbol = self.config.symbol

        # RPC
        self.rpc_helper = ForgeRpcHelper(self._channel, self.config.chain_id)
        self.fetch_account = self.rpc_helper.fetch_account
        self.fetch_tx = self.rpc_helper.fetch_tx
        self.fetch_balance = self.rpc_helper.fetch_balance
        self.fetch_asset = self.rpc_helper.fetch_asset
        self.build_unsigned_tx = self.rpc_helper.build_unsigned_tx
        self.build_tx = self.rpc_helper.build_tx
        self.send_itx = self.rpc_helper.send_itx

    @send_forge_transaction
    def transfer(self, **kwargs):
        return

    def create_asset(self, data, **kwargs):
        itx = itx_utils.create_asset_itx(data=data, **kwargs)
        return self.send_itx(itx, **kwargs), itx.address

    @send_forge_transaction
    def update_asset(self, **kwargs):
        return

    @send_forge_transaction
    def declare(self, **kwargs):
        return

    @send_forge_transaction
    def account_migrate(self, **kwargs):
        return

    @send_forge_transaction
    def delegate(self, **kwargs):
        return

    @send_forge_transaction
    def revoke_delegate(self, **kwargs):
        return

    @send_forge_transaction
    def activate_protocol(self, **kwargs):
        return

    @send_forge_transaction
    def deactivate_protocol(self, **kwargs):
        return

    @send_forge_transaction
    def upgrade_node(self, **kwargs):
        return

    def poke(self, wallet):
        itx = itx_utils.poke_itx()
        return self.rpc_helper.send_itx(itx=itx,
                                        nonce=0,
                                        wallet=wallet)

    def prepare_exchange(self, sender, receiver, **kwargs):
        itx = itx_utils.exchange_itx(sender=sender,
                                     receiver=receiver,
                                     **kwargs)
        tx = self.rpc_helper.build_tx(itx=itx, **kwargs)
        return tx

    def finalize_exchange(self, tx, wallet, **kwargs):
        signed_tx = tx_util.multisign_tx(tx=tx,
                                         wallet=wallet,
                                         multisig_data=kwargs.get('data'),
                                         delegatee=kwargs.get('delegatee'))
        return self._chain_rpc.send_tx(signed_tx, commit=kwargs.get('commit'))

    def prepare_consume_asset(self, issuer, **kwargs):
        itx = itx_utils.consume_asset_itx(issuer=issuer,
                                          **kwargs)
        return self.rpc_helper.build_tx(itx=itx, **kwargs)

    def finalize_consume_asset(self, tx, wallet, data, **kwargs):
        multisig_data = utils.to_any(data, 'fg:x:address')
        signed_tx = tx_util.multisign_tx(tx=tx,
                                         wallet=wallet,
                                         multisig_data=multisig_data,
                                         delegatee=kwargs.get('delegatee'))
        return self._chain_rpc.send_tx(signed_tx, commit=kwargs.get('commit'))

    def _basic_set_up(self, grpc_sock):
        self._channel = grpc.insecure_channel(grpc_sock)

        self._chain_rpc = ForgeChainRpc(self._channel)
        self._event_rpc = ForgeEventRpc(self._channel)
        self._file_rpc = ForgeFileRpc(self._channel)
        self._state_rpc = ForgeStateRpc(self._channel)
        self._stats_rpc = ForgeStatsRpc(self._channel)
        self._wallet_rpc = ForgeWalletRpc(self._channel)

    def to_unit(self, token):
        return int(token * (10 ** int(self.token_decimal)))

    def from_unit(self, unit):
        return int(unit / (10 ** int(self.token_decimal)))

    # Private helper methods
    def _get_config(self):
        config = self.get_config().config
        return ForgeConfig(json.loads(config))
