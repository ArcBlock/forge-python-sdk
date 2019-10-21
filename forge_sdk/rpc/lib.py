from collections import Iterable
from forge_sdk import protos
from forge_sdk import utils


def to_iter(to_req, data):
    if isinstance(data, dict) or isinstance(data, str):
        return iter([to_req(data)])
    elif isinstance(data, Iterable):
        return (to_req(i) for i in data)
    else:
        return iter([data])


def get_wallet(**kwargs):
    wallet = kwargs.get('wallet',
                        protos.WalletInfo(pk=kwargs.get('pk'),
                                          sk=kwargs.get('sk'),
                                          address=kwargs.get('address')))
    return wallet


