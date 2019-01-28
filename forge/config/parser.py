import os.path as path
from os.path import expanduser

import toml
from deepmerge import Merger

DEFAULT_FORGE_CONFIG_PATH = './forge_default.toml'


def parse_config(file_path):
    toml_dict = toml.load(DEFAULT_FORGE_CONFIG_PATH)
    if not file_path and path.exists(file_path):
        raise FileNotFoundError("Can't find the forge config user provided!")
    elif path.exists(file_path):
        user_dict = toml.load(file_path)
        merger = Merger(
            [
                (list, ['override']),
                (dict, ['merge']),
                ['override'],
                ['override'],
            ],
        )
        merger.merge(toml_dict, user_dict)
    return ForgeConfig(toml_dict)


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
