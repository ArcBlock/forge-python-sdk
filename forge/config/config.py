import logging
import os
import os.path as path
from os.path import expanduser

import grpc
import toml
from deepmerge import Merger

logger = logging.getLogger('forge-config')

default_forge_toml = path.join(path.dirname(__file__), "forge_default.toml")

config = toml.load(default_forge_toml)


def use_config(user_config=None, env=True):
    # Use Environment FORGE_CONFIG if exists
    env_config = os.environ.get('FORGE_CONFIG')
    if env:
        logger.info("Reading config from environment...")
        merge_config(env_config)
    elif user_config:
        logger.info("FORGE_CONFIG not found!")
        merge_config(user_config)
    else:
        logger.error("Please either specify a config path or "
                     "set FORGE_CONFIG in the environment!")


def merge_config(config_path):
    if path.exists(config_path):
        logger.info("Using config in {}".format(config_path))
        try:
            user_config = toml.load(config_path)

            merger = Merger(
                # strategy for each type
                [
                    (list, ["append"]),
                    (dict, ["merge"]),
                ],
                # fallback strategies for all other types
                ["override"],
                # strategies for conflicted types
                ["override"],
            )
            res_config = toml.load(default_forge_toml)
            merger.merge(res_config, user_config)
            global config
            config = res_config

        except Exception as e:
            logger.error(e, exc_info=True)
            logger.error("Fail to parse toml config in {}".format(config_path))


use_config()


def __parse_socket(forge_path, forge_socket):
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


def __parse_socket_grpc(forge_path, forge_socket):
    socket_addr = __parse_socket(forge_path, forge_socket)
    socket_type = socket_addr.split('://')[0]
    if socket_type == 'unix':
        return socket_addr
    elif socket_type == 'tcp':
        return socket_addr.split('://')[1]


def get_app_path():
    return expanduser(config['app']['path'])


def get_app_host():
    return config['app']['host']


def get_forge_path():
    return expanduser(config['forge']['path'])


def get_grpc_socket():
    return __parse_socket_grpc(
        get_forge_path(),
        config['forge']['sock_grpc'],
    )


def get_tcp_socket():
    return __parse_socket(
        get_app_path(),
        config['app']['sock_tcp'],
    )


def get_forge_port():
    return config['app']['forge_port']


def get_grpc_channel():
    return grpc.insecure_channel(get_grpc_socket())
