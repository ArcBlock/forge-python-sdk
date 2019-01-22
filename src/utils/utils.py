from google.protobuf.internal.decoder import _DecodeVarint32
from google.protobuf.internal.encoder import _VarintBytes


def parse_proto_from(data, proto_message):
    result = proto_message()
    result.ParseFromString(data)
    return result


def decode_varint_request(data, beginning=0):
    req_len, start_pos = _DecodeVarint32(data, beginning)
    request = data[start_pos: start_pos + req_len]
    return request, req_len, start_pos


def encode_varint_request(proto_data):
    size = proto_data.ByteSize()
    varint_bytes = _VarintBytes(size)
    proto_bytes = proto_data.SerializeToString()
    return varint_bytes + proto_bytes
