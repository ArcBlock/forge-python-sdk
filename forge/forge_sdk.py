import logging

from .config import ForgeConfig
from .server import ForgeServer


class ForgeSdk:
    def __init__(self, handlers=[], config=None):
        logging.basicConfig(
            format='%(asctime)s-%(name)s-%(process)d-%('
            'levelname)s-%(message)s',
        )
        self.handlers = handlers
        self.logger = logging.getLogger(__name__)
        self.config = config if config else ForgeConfig()
        self.rpc = ForgeRpc(self.config.sock_grpc)

        self.server = ForgeServer(
            handlers=handlers,
            address=self.config.sock_tcp,
        )

    def register_handler(self, handler):
        # sanity check
        # add to server
        self.server.register_handler(handler)

    def start(self):
        self.server.start()


class TxHandler:
    def __init__(self, tx_type, function_dic):
        self.tx_type = tx_type
        self.function_dic = function_dic
