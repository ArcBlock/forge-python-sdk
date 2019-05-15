import codecs
import math
from functools import reduce

from forge_sdk import protos


def int_to_bytes(n):
    r"""
    Convert integer to bytes

    Args:
        n(int): integer to be converted

    Returns:
        bytes

    Examples:
        >>> int_to_bytes(10)
        b'\n'
        >>> int_to_bytes(222)
        b'\xde'
    """

    size = int(math.ceil(len(hex(n)) / 2 - 1))

    b = '%x' % n
    h = ('0' * (len(b) % 2) + b).zfill(size * 2)
    s = codecs.decode(h, "hex")
    return s


def bytes_to_int(bytes):
    """
    Convert bytes to integer

    Args:
        bytes(bytes): bytes to be converted

    Returns:
        int

    Examples:
        >>> bytes_to_int(b'\xde')
        222

    """

    return reduce(lambda s, x: (s << 8) + x, bytearray(bytes))


def int_to_biguint(n):
    """
    Convert integer to :obj:`protos.BigUint`

    Args:
        n(int): number to be converted

    Returns:
        :obj:`BigUint`

    Examples:
        >>> res = int_to_biguint(200)
        >>> res.value
        b'\xc8'
    """

    return protos.BigUint(value=int_to_bytes(n))


def token_to_biguint(token):
    r"""
    Convert token to smallest unit, then to bigUint

    Args:
        token(num): token value

    Returns:
        :obj:`BigUint`

    Examples:
        >>> token_to_biguint(1)
        value: "#\206\362o\301\000\000"

    """
    return int_to_biguint(int(token*1e+16))


def token_to_unit(token):
    return int(token*1e16)


def unit_to_token(unit):
    return int(unit/1e16)


def biguint_to_int(biguint):
    """
    Convert :obj:`BigUint` to integer
    Args:
        biguint(:obj:`BigUint`): BigUint to be converted

    Returns:
        int

    Examples:
        >>> from forge_sdk import protos
        >>> biguint = protos.BigUint(value=b'\xc8')
        >>> biguint_to_int(biguint)
        200

    """

    return bytes_to_int(biguint.value)
