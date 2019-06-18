from forge_sdk.config.config import ForgeConfig


def parse_socket(forge_path, forge_socket):
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


def parse_socket_grpc(forge_path, forge_socket):
    socket_addr = parse_socket(forge_path, forge_socket)
    socket_type = socket_addr.split('://')[0]
    if socket_type == 'unix':
        return socket_addr
    elif socket_type == 'tcp':
        return socket_addr.split('://')[1]
