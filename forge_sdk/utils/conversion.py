import codecs
import math
from functools import reduce


def int_to_bytes(n):
    size = int(math.ceil(len(hex(n)) / 2 - 1))

    b = '%x' % n
    h = ('0' * (len(b) % 2) + b).zfill(size * 2)
    s = codecs.decode(h, "hex")
    return s


def bytes_to_int(bytes):
    return reduce(lambda s, x: (s << 8) + x, bytearray(bytes))
