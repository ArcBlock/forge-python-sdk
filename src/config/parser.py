import os
import os.path as path
from os.path import expanduser

import toml

FORGE_CONFIG_ENV = 'FORGE_CONFIG'
FORGE_CONFIG_DEFAULT_PATH = '~/.forge/forge.toml'
FORGE_CONFIG_FILE_NAME = 'forge.toml'


def parse_config(path=None):
    if path:
        return parse_from_path(path)
    else:
        return parse_from_default()


def parse_from_path(file_path):
    forge_toml = toml.load(file_path)
    return ForgeConfig(forge_toml)


def parse_from_default():
    forge_env = os.getenv(FORGE_CONFIG_ENV, '')
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
        self.sock_grpc = self.parse_socket(
            toml_dict['forge']['path'],
            toml_dict['forge']['sock_grpc'],
        )
        self.sock_tcp = self.parse_socket(
            toml_dict['app']['path'],
            toml_dict['app']['sock_tcp'],
        )

    def parse_socket(self, forge_path, forge_socket):
        expanded_forge_path = expanduser(forge_path)
        socket_type = forge_socket.split("://")[0]
        parsed_socket = forge_socket.split("://")[1]
        if socket_type == 'unix':
            socket_target = '/'.join([
                'unix:/',
                expanded_forge_path, parsed_socket,
            ])
        else:
            socket_target = parsed_socket
        return socket_target
