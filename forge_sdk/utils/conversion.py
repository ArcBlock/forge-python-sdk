import codecs
import math
from functools import reduce

from forge_sdk import protos

token_decimal = (10 ** int(16))


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


def int_to_bigsint(n, minus=False):
    return protos.BigSint(value=int_to_bytes(n),
                          minus=minus)


def value_to_biguint(value):
    r"""
    Convert token to smallest unit, then to bigUint

    Args:
        value(num): token value

    Returns:
        :obj:`BigUint`

    Examples:
        >>> value_to_biguint(1)
        value: "#\206\362o\301\000\000"

    """
    return int_to_biguint(int(value * token_decimal))


def to_unit(token):
    return int(token * token_decimal)


def from_unit(unit):
    return int(unit / token_decimal)


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
