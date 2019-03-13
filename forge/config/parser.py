import logging
import os
import os.path as path
from os.path import expanduser

import toml
from deepmerge import Merger

logger = logging.getLogger('Forge-Parser')


def parse_config(file_path):
    default_config = path.join(path.dirname(__file__), "forge_default.toml")
    toml_dict = toml.load(default_config)
    custom_path = get_config_path(file_path)

    if not custom_path:
        return toml_dict
    else:
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

        user_dict = toml.load(custom_path)
        merger.merge(toml_dict, user_dict)
    return toml_dict


def get_config_path(user_file=None):
    env = os.environ.get('FORGE_CONFIG')
    if env:
        if path.exists(env):
            logger.info('Using config in {}'.format(env))
            return env
        else:
            logger.error('Config file {} not found.'.format(env))
    if user_file:
        if path.exists(user_file):
            logger.info('Using config in {}'.format(user_file))
            return user_file
        else:
            logger.error('Config file {} not found.'.format(user_file))


class ForgeConfig:

    def __init__(self, file_path=None):
        self.toml_dict = parse_config(file_path)
        self.forge_path = expanduser(self.toml_dict['forge']['path'])
        self.sock_grpc = self.__parse_socket_grpc(
            self.forge_path,
            self.toml_dict['forge']['sock_grpc'],
        )
        self.sock_tcp = self.__parse_socket(
            self.get_app_path(),
            self.toml_dict['app']['sock_tcp'],
        )

    def get_app_path(self):
        return expanduser(self.toml_dict['app']['path'])

    def get_app_host(self):
        return self.toml_dict['app']['host']

    def get_app_port(self):
        return self.toml_dict['app']['port']

    def __parse_socket(self, forge_path, forge_socket):
        """

        Parameters
        ----------
        Returns: string
            unix: "unix:///tmp/.forge_test/app/socks/abi.sock"
            tcp: "tcp://127.0.0.1:38210"

        -------

        """
        socket_type = forge_socket.split("://")[0]
        parsed_socket = forge_socket.split("://")[1]
        if socket_type == 'unix':
            socket_target = '/'.join([
                'unix:/',
                forge_path, parsed_socket,
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
