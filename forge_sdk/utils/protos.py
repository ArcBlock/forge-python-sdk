from google.protobuf.any_pb2 import Any

from forge_sdk.utils import conversion


def parse_to_proto(binary, proto_message):
    result = proto_message()
    result.ParseFromString(binary)
    return result


def encode_to_any(type_url, data):
    if isinstance(data, str):
        value = data.encode()
    elif isinstance(data, int):
        value = conversion.int_to_bytes(data)
    else:
        value = data.SerializeToString()

    return Any(
        type_url=type_url,
        value=value
    )


def is_proto_empty(proto_message):
    return proto_message.SerializeToString() == b''
