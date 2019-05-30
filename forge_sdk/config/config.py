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


def use_config():
    env_config = os.environ.get('FORGE_CONFIG')
    if env_config:
        logger.info("Reading config from environment...")
        merge_config(env_config)
    else:
        logger.warning("FORGE_CONFIG not found. Using default forge config.")


def get_app_path():
    """
    Get app path defined in config

    Returns:string

    """
    return expanduser(config['app']['path'])


def get_app_host():
    """
    Get app host address defined in config

    Returns:string

    """
    return config['app']['host']


def get_forge_path():
    """
    Get forge path defined in config

    Returns:string

    """
    return expanduser(config['forge']['path'])


def get_grpc_socket():
    """
    Get grpc socket address

    Returns: string

    """
    return _parse_socket_grpc(
        get_forge_path(),
        config['forge']['sock_grpc'],
    )


def get_forge_port():
    """
    Get the port number forge web uses

    Returns: string

    """
    return config['app']['forge_port']


def get_grpc_channel():
    """
    Create a new gRPC Chanel

    Returns: :obj:`grpc.channel`

    """
    return grpc.insecure_channel(get_grpc_socket())


def merge_config(config_path):
    if not path.exists(config_path):
        logger.error(f'{config_path} does not exist.')
    else:
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


def _parse_socket(forge_path, forge_socket):
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


def _parse_socket_grpc(forge_path, forge_socket):
    socket_addr = _parse_socket(forge_path, forge_socket)
    socket_type = socket_addr.split('://')[0]
    if socket_type == 'unix':
        return socket_addr
    elif socket_type == 'tcp':
        return socket_addr.split('://')[1]
