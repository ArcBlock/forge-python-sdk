import logging
import os
import os.path as path

from forge_sdk import rpc
from forge_sdk.config import config as forge_config


logger = logging.getLogger('ec-config')

app_config_path = path.join(path.dirname(__file__), "forge.toml")

APP_SK = 'zyQBXZ7NijYQQRzLUryjkd1Mj4qSpofcnsgEh8a8ZrtbgM1jSKHrC85V' \
         'edZsQ5N3x5M298zpridcq2bKBZtmqroT'
APP_PK = "zExrfT2pXtVqdAqgZwjvdMBo5RpqSqn1fa43Wp93peuSR"
APP_ADDR = "z1UT9an1Z4W1gnmzASneER2J5eqtx5jfwgx"

ARC = 'https://abtwallet.io/i/'


forge_config.use_config(app_config_path)

app_path = forge_config.get_app_path()

app_host = forge_config.get_app_host()

forge_port = forge_config.get_forge_port()

db_path = path.join(app_path, "ec.db")

googlemaps_key = os.environ.get('GOOGLEMAPS_KEY')

chain_info = rpc.get_chain_info().info
chain_id = chain_info.network

SERVER_ADDRESS = "http://" + app_host + ":5000"

if not os.path.exists(app_path):
    os.system('mkdir -p {}'.format(app_path))
    logger.info("{} created.".format(app_path))
