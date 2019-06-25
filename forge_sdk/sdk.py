import json
import logging
import os

import grpc

from forge_sdk import protos
from forge_sdk.config import ForgeConfig
from forge_sdk.rpc.forge_rpc import ForgeRpc

logger = logging.getLogger('forge-rpc')


class ForgeConn:
    def __init__(self, grpc_sock=None):
        if not grpc_sock:
            grpc_sock = os.environ.get('FORGE_SOCK_GRPC', '127.0.0.1:27210')

        logger.info(f'Connecting to socket {grpc_sock}')

        self.channel = grpc.insecure_channel(grpc_sock)

        self.rpc = self._connect_rpc()
        self.config = self._get_config()
        self.rpc.__setattr__('chain_id', self.config.chain_id)

    def _connect_rpc(self):
        return ForgeRpc(self.channel)

    def _get_config(self):
        config = self.rpc.get_config().config
        return ForgeConfig(json.loads(config))
