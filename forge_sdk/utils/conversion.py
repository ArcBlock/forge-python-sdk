import codecs
import math
from functools import reduce


def int_to_bytes(n):
    """
    Convert integer to bytes
    Args:
        n(int): integer to be converted

    Returns: bytes

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

    Returns: int

    """
    return reduce(lambda s, x: (s << 8) + x, bytearray(bytes))
