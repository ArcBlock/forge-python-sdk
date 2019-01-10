from os.path import expanduser
import toml
import os.path as path
import os

FORGE_CONFIG_ENV = 'FORGE_CONFIG'
FORGE_CONFIG_DEFAULT_PATH = '~/.forge/forge.toml'
FORGE_CONFIG_FILE_NAME = 'forge.toml'


def parse_from_path(path):
	forge_toml = toml.load(path)
	return ForgeConfig(forge_toml)


def parse_from_default():
	forge_env = os.getenv(FORGE_CONFIG_ENV,'')
	file_path = path.expanduser(FORGE_CONFIG_DEFAULT_PATH)
	cwd_path = path.join(os.getcwd(), FORGE_CONFIG_FILE_NAME)

	if forge_env:
		return parse_from_path(forge_env)
	elif path.isfile(file_path):
		return parse_from_path(file_path)
	elif path.isfile(cwd_path):
		return parse_from_path(cwd_path)
	else:
		raise FileNotFoundError("Forge Config not found!")


class ForgeConfig:

	def __init__(self, toml_dict):
		self.toml_dict = toml_dict
		self.forge_path = self.toml_dict['forge']['path']
		self.forge_socket_grpc =self.toml_dict['forge']['sock_grpc']
		self.socket_target = self.parse_socket()

	def parse_socket(self):
		expanded_forge_path = expanduser(self.forge_path)
		parsed_socket = self.forge_socket_grpc.split("//")[1]
		socket_target = '/'.join(['unix:/', expanded_forge_path, parsed_socket])
		return socket_target
