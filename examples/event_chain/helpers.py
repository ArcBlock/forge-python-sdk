from datetime import datetime

from google.protobuf.timestamp_pb2 import Timestamp

from . import models


def gen_timestamp(year, month, day, hour):
    res = Timestamp()
    res.FromDatetime(datetime(year, month, day, hour))
    return res


def register_user(name, passphrase='abcde1234'):
    return models.DeclaredUser(moniker=name, passphrase=passphrase)
