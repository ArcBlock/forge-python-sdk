import logging
import os
import os.path as path

from forge.config import config as forge_config
from forge.rpc import rpc


logger = logging.getLogger('ec-config')

app_config_path = path.join(path.dirname(__file__), "forge.toml")

forge_config.use_config(app_config_path)

app_path = forge_config.get_app_path()

app_host = forge_config.get_app_host()

forge_port = forge_config.get_forge_port()

db_path = path.join(app_path, "ec.db")

googlemaps_key = os.environ.get('GOOGLEMAPS_KEY')

chain_info = rpc.get_chain_info().info
chain_id = chain_info.network
