import base64

import base58


def multibase_b58encode(data):
    raw = base58.b58encode(data)
    return 'z' + raw.decode()


def multibase_b58decode(data):
    if data.startswith('z'):
        return base58.b58decode((data[1:]).encode())
    raise ValueError('{} cannot be decoded by multibase'
                     ' base58.'.format(str(data)))


def multibase_b64encode(data):
    if isinstance(data, str):
        data = data.encode()
    return base64.urlsafe_b64encode(data).decode().rstrip('=')


def multibase_b64decode(data):
    if isinstance(data, str):
        data = data.encode()
    return base64.urlsafe_b64decode(
        (data + b'=' * (-len(data) % 4)))
