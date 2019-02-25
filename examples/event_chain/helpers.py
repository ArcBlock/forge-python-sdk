from enum import Enum
from google.protobuf.timestamp_pb2 import Timestamp


def gen_timestamp(datetime):
    res = Timestamp()
    res.FromDatetime(datetime)
    return res


def add_to_proto_list(info, repeated):
    res = {item for item in repeated}
    res.add(info)
    return res


def remove_from_proto_list(info, repeated):
    res = filter(lambda item: item != info, repeated)
    return res


class ForgeTxType(Enum):
    ACTIVATE_ASSET = 'fg:t:activate_asset'
    CREATE_ASSET = 'fg:t:create_asset'
    EXCHANGE = 'fg:t:exchange'
