import ast
import base64
import codecs
import json
import logging
import math
from collections import Iterable
from datetime import datetime
from functools import reduce

import base58
from google.protobuf.any_pb2 import Any
from google.protobuf.internal.decoder import _DecodeVarint32
from google.protobuf.internal.encoder import _VarintBytes

from .. import protos

logger = logging.getLogger('forge-util')


def parse_to_proto(binary, proto_message):
    result = proto_message()
    result.ParseFromString(binary)
    return result


def decode_to_proto(binary, proto_message):
    data, req_len, start_pos = decode(binary)
    result = proto_message()
    result.ParseFromString(data)
    return result


def decode(binary):
    req_len, start_pos = __decode_zigzag(binary)
    res = binary[start_pos: start_pos + req_len]
    return res, req_len, start_pos


def encode(proto_data):
    size = proto_data.ByteSize()
    varint_bytes = __encode_zigzag(size)
    proto_bytes = proto_data.SerializeToString()
    return varint_bytes + proto_bytes


def encode_to_any(type_url, data):
    return Any(
        type_url=type_url,
        value=data.SerializeToString(),
    )


def __decode_zigzag(binary):
    length, start = _DecodeVarint32(binary, 0)
    res = length & 1
    if res == 1:
        return -((length + 1) >> 1), start
    elif res == 0:
        return length >> 1, start


def __encode_zigzag(integer):
    if integer >= 0:
        return _VarintBytes(integer << 1)
    else:
        return _VarintBytes(-((integer << 1) + 1))


def to_iter(to_req, data):
    if isinstance(data, dict) or isinstance(data, str):
        return iter([to_req(data)])
    elif isinstance(data, Iterable):
        return (to_req(i) for i in data)
    else:
        return iter([data])


def data_of_create_asset(tx, proto_def):
    create_tx = parse_to_proto(tx.itx.value, protos.CreateAssetTx)
    data = parse_to_proto(create_tx.data.value, proto_def)
    return data


def is_proto_empty(proto_message):
    if proto_message.SerializeToString() == b'':
        return True
    else:
        return False


def _to_bytes(n, length, endianess='big'):
    b = '%x' % n
    h = ('0' * (len(b) % 2) + b).zfill(length * 2)
    s = codecs.decode(h, "hex")
    return s if endianess == 'big' else s[::-1]


def _bytes_size(n):
    return math.ceil(len(hex(n)) / 2 - 1)


def int_to_bytes(n):
    size = int(_bytes_size(n))
    return _to_bytes(n, size)


def bytes_to_int(bytes):
    return reduce(lambda s, x: (s << 8) + x, bytearray(bytes))


def multibase_b58encode(data):
    raw = base58.b58encode(data)
    return 'z' + raw.decode()


def multibase_b58decode(data):
    if data.startswith('z'):
        return base58.b58decode((data[1:]).encode())
    raise ValueError('{} cannot be decoded by multibase'
                     ' base58.'.format(str(data)))


def to_json_b64urlsafe(dictionary):
    json_data = json.dumps(dictionary)
    return b64encode_no_padding(json_data)


def b64encode_no_padding(data):
    if isinstance(data, str):
        data = data.encode()
    return base64.urlsafe_b64encode(data).decode().rstrip('=')


def b64decode_padding_safe(data):
    if isinstance(data, str):
        data = data.encode()
    return base64.urlsafe_b64decode(
        (data + b'=' * (-len(data) % 4)))


def b64encoded_to_dict(data):
    try:
        dict_string = b64decode_padding_safe(data).decode()
        return ast.literal_eval(dict_string)
    except Exception as e:
        logger.error('Error in decoding b64urlsafe '
                     'encoded data to dictionary.')
        logger.error(e, exc_info=True)
        return {}


# TODO: utc timestamp
def current_utc_timestamp():
    return round(datetime.utcnow().timestamp())


def clean_dict(d):
    return {k: v for k, v in d.items() if v and v != ''}
