import logging
import os
import os.path as path

from .kv_handler import init_kv_handler
from forge import ForgeSdk

logger = logging.getLogger(__name__)


def init():
    kv_handler = init_kv_handler()
    logger.info('KV handler is registered')

    config = path.join(os.getcwd(), 'priv', "kvstore.toml")
    sdk = ForgeSdk({kv_handler}, config)

    logger.info('SDK for kv application is initiated!')
    return sdk


def start_server():
    sdk = init()
    sdk.server.start()


def kv_rpc():
    sdk = init()
    return sdk.rpc


if __name__ == '__main__':
    start_server()
