import os.path as path
from os.path import expanduser

import toml
from deepmerge import Merger


def parse_config(file_path):
    default_config = path.join(path.dirname(__file__), "forge_default.toml")
    toml_dict = toml.load(default_config)
    if not file_path:
        return toml_dict
    elif file_path and not path.exists(file_path):
        raise FileNotFoundError("Can't find the forge config user provided!")
    elif path.exists(file_path):
        user_dict = toml.load(file_path)
        merger = Merger(
            # pass in a list of tuple, with the
            # strategies you are looking to apply
            # to each type.
            [
                (list, ["append"]),
                (dict, ["merge"]),
            ],
            # next, choose the fallback strategies,
            # applied to all other types:
            ["override"],
            # finally, choose the strategies in
            # the case where the types conflict:
            ["override"],
        )
        merger.merge(toml_dict, user_dict)
    return toml_dict


class ForgeConfig:

    def __init__(self, file_path=None):
        self.toml_dict = parse_config(file_path)
        self.app_path = self.toml_dict['app']['path']
        self.forge_path = self.toml_dict['forge']['path']
        self.sock_grpc = self.__parse_socket_grpc(
            self.forge_path,
            self.toml_dict['forge']['sock_grpc'],
        )
        self.sock_tcp = self.__parse_socket(
            self.app_path,
            self.toml_dict['app']['sock_tcp'],
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
