import os.path as path

from forge import ForgeConfig

app_config = path.join(path.dirname(__file__), "forge.toml")

forge_config = ForgeConfig(app_config)

db_path = path.join(forge_config.app_path, "sqlite.db")
