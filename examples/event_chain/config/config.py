import logging
import os.path as path

from forge import ForgeConfig

logger = logging.getLogger('ec-config')

app_config = path.join(path.dirname(__file__), "forge.toml")

forge_config = ForgeConfig(app_config)

app_path = forge_config.get_app_path()

app_host = forge_config.get_app_host()
app_port = forge_config.get_app_port()

db_path = path.join(app_path, "ec.db")
