from google.protobuf.any_pb2 import Any

from forge_sdk.utils import conversion


def parse_to_proto(binary, proto_message):
    """
    Parse bytes to given proto message

    Args:
        binary(bytes): serialized value of proto message
        proto_message(:obj:`protos.objects`): proto message objects

    Returns:
        :obj:`protos.objects`

    Examples:
        >>> from forge_sdk import protos
        >>> serialized = protos.TransferTx(to='mike address').SerializeToString()
        >>> tx = parse_to_proto(serialized, protos.TransferTx)
        >>> tx.to
        "mike address"

    """
    result = proto_message()
    result.ParseFromString(binary)
    return result


def encode_to_any(type_url, data):
    """
    Encode the provided data into :obj:`protobuf.Any`. This function encodes
    string with UTF-8, integer with helper function `int_to_bytes`, and proto
    messages with internal `SerializeToString()` method.

    Args:
        type_url(string): the type_url to encode the data with. This will be
            the `type_url` field of final result.
        data(bytes): the data to encode. This will be the `value` field of
            final result.

    Returns:
        :obj:`Any`

    Examples:
        >>> res = encode_to_any('test_string','test')
        >>> res.type_url
        'test_string
        >>> res.value
        b'test'

    """
    if not data:
        value = None
    elif isinstance(data, str):
        value = data.encode()
    elif isinstance(data, int):
        value = conversion.int_to_bytes(data)
    elif isinstance(data, bytes):
        value = data
    else:
        value = data.SerializeToString()

    return Any(
        type_url=type_url,
        value=value
    )


def is_proto_empty(proto_message):
    """
    Check if proto message is empty

    Args:
        proto_message(:obj:`proto.objects`): proto objects

    Returns:
        bool

    Examples:
        >>> is_proto_empty(protos.DeclareTx())
        True
        >>> is_proto_empty(protos.TransferTx(to='mike'))
        False

    """
    return proto_message.SerializeToString() == b''
