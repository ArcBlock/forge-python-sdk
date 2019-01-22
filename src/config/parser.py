import os
import os.path as path
from os.path import expanduser

import toml

FORGE_CONFIG_ENV = 'FORGE_CONFIG'
FORGE_CONFIG_DEFAULT_PATH = '~/.forge/forge.toml'
FORGE_CONFIG_FILE_NAME = 'forge_test.toml'


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
    priv_path = path.join(os.getcwd(), 'priv', FORGE_CONFIG_FILE_NAME)

    if forge_env:
        return parse_from_path(forge_env)
    elif path.isfile(file_path):
        return parse_from_path(file_path)
    elif path.isfile(cwd_path):
        return parse_from_path(cwd_path)
    elif path.isfile(priv_path):
        return parse_from_path(priv_path)
    else:
        raise FileNotFoundError("Forge Config not found!")


class ForgeConfig:

    def __init__(self, toml_dict):
        self.toml_dict = toml_dict
        self.sock_grpc = self.__parse_socket_grpc(
            toml_dict['forge']['path'],
            toml_dict['forge']['sock_grpc'],
        )
        self.sock_tcp = self.__parse_socket(
            toml_dict['app']['path'],
            toml_dict['app']['sock_tcp'],
        )

    def __parse_socket(self, forge_path, forge_socket):
        """

        Parameters
        ----------
x
        Returns: string
            unix: "unix:///tmp/.forge_test/app/socks/abi.sock"
            tcp: "tcp://127.0.0.1:38210"

        -------

        """
        expanded_forge_path = expanduser(forge_path)
        socket_type = forge_socket.split("://")[0]
        parsed_socket = forge_socket.split("://")[1]
        if socket_type == 'unix':
            socket_target = '/'.join([
                'unix:/',
                expanded_forge_path, parsed_socket,
            ])
        else:
            socket_target = forge_socket
        return socket_target

    def __parse_socket_grpc(self, forge_path, forge_socket):
        socket_addr = self.__parse_socket(forge_path, forge_socket)
        socket_type = socket_addr.split('://')[0]
        if socket_type == 'unix':
            return socket_addr
        elif socket_type == 'tcp':
            return socket_addr.split('://')[1]
