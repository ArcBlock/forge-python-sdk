import logging

from .config import parser
from .rpc import ForgeRpc
from .server import ForgeServer


class ForgeSdk:
    def __init__(self, handlers=None, config_path=''):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s-%(name)s-%(process)d-%('
            'levelname)s-%(message)s',
        )
        self.handlers = handlers
        self.logger = logging.getLogger(__name__)
        self.config = parser.parse_config(config_path)
        self.rpc = ForgeRpc(self.config.sock_grpc)

        if handlers:
            self.server = ForgeServer(
                handlers=handlers,
                address=self.config.sock_tcp,
            )

    def register_handler(self, handler):
        # sanity check
        # add to server
        self.server.register_handler(handler)


class TxHandler:
    def __init__(self, tx_type, function_dic):
        self.tx_type = tx_type
        self.function_dic = function_dic
