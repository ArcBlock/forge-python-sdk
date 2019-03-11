import logging
import os.path as path

from forge import ForgeConfig

logger = logging.getLogger('ec-config')

app_config = path.join(path.dirname(__file__), "forge.toml")

forge_config = ForgeConfig(app_config)

app_path = forge_config.get_app_path()

db_path = path.join(app_path, "ec.db")
logger.info('db_path: {}'.format(db_path))
