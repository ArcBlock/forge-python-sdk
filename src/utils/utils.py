from google.protobuf.internal.decoder import _DecodeVarint32
from google.protobuf.internal.encoder import _VarintBytes


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
