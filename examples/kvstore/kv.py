import logging

import kv_handler as kv

from forge import ForgeSdk

logger = logging.getLogger(__name__)


def init_sdk():
    kv_handler = kv.init_kv_handler()
    logger.info('KV handler is registered')

    sdk = ForgeSdk([kv_handler])

    logger.info('SDK for kv application is initiated!')
    return sdk


if __name__ == '__main__':
    sdk = init_sdk()
    sdk.server.start()
