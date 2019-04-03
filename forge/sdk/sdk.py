import logging

from forge.config import config
from forge.server import ForgeServer

logger = logging.getLogger('forge-sdk')

server = None

def init_server(handlers):
    global server
    if not server:
        server = ForgeServer(handlers, config.get_tcp_socket())
