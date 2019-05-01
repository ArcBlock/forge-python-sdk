import base64

import base58


def multibase_b58encode(data):
    """
    Follow forge's base58 encode convention to encode bytes

    Args:
        data(bytes): data to be encoded

    Returns: string

    """
    raw = base58.b58encode(data)
    return 'z' + raw.decode()


def multibase_b58decode(data):
    """
    Follow forge's base58 encode convention to decode string

    Args:
        data(string): encoded string

    Returns: bytes

    """
    if data.startswith('z'):
        return base58.b58decode((data[1:]).encode())
    raise ValueError('{} cannot be decoded by multibase'
                     ' base58.'.format(str(data)))


def multibase_b64encode(data):
    """
    Follow forge's base64 urlsafe encode convention to encode bytes

    Args:
        data(bytes): data to be encoded

    Returns: string

    """
    if isinstance(data, str):
        data = data.encode()
    return base64.urlsafe_b64encode(data).decode().rstrip('=')


def multibase_b64decode(data):
    """
    Follow forge's base64 urlsafe encode convention to decode string

    Args:
        data(string): encoded string

    Returns: bytes
    """

    if isinstance(data, str):
        data = data.encode()
    return base64.urlsafe_b64decode(
        (data + b'=' * (-len(data) % 4)))
