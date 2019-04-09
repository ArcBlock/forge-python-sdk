import logging

from forge.config import config
from forge.server import ForgeServer

logger = logging.getLogger('forge-sdk')

server = None


def init_server(handlers):
    """ Init Forge Server

    Args:
        handlers(:obj:`TxHandlers`): handers for different types of tx

    Returns:
        None

    """
    global server
    if not server:
        server = ForgeServer(handlers, config.get_tcp_socket())
