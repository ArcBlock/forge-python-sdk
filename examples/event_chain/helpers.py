from google.protobuf.timestamp_pb2 import Timestamp


def gen_timestamp(datetime):
    res = Timestamp()
    res.FromDatetime(datetime)
    return res
