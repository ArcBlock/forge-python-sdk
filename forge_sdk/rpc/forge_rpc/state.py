from forge_sdk.config import config
from forge_sdk.protos import protos
from forge_sdk.rpc import lib

stub = protos.StateRpcStub(config.get_grpc_channel())


def get_account_state(queries):
    """GRPC call to get detailed of account

    Args:
        queries(dict): dictionaries of requested parameters

    Returns:
        ResponseGetAccountState(stream)

    """

    def to_req(item):
        kwargs = {
            'address': item.get('address'),
            'keys': item.get('keys', []),
        }
        return protos.RequestGetAccountState(**kwargs)

    requests = lib.to_iter(to_req, queries)

    return stub.get_account_state(requests)


def get_asset_state(queries):
    """GRPC call to get detailed of asset

    Args:
        queries(dict): dictionaries of requested parameters

    Returns:
        ResponseGetAssetState(stream)
    """

    def to_req(item):
        kwargs = {
            'address': item.get('address'),
            'keys': item.get('keys', []),
        }
        req = protos.RequestGetAssetState(**kwargs)
        return req

    requests = lib.to_iter(to_req, queries)

    return stub.get_asset_state(requests)


def get_stake_state(queries):
    """GRPC call to get detailed of stake

    Args:
        queries(dict): dictionaries of requested parameters

    Returns:
        ResponseGetStakeState(stream)

    """

    def to_req(items):
        kwargs = {
            'address': items.get('address'),
            'keys': items.get('keys', []),
        }
        return protos.RequestGetStakeState(**kwargs)

    requests = lib.to_iter(to_req, queries)
    return stub.get_stake_state(requests)


def get_forge_state(keys=[], height=None):
    """ GRPC call to get forge state

    Args:
        keys(list[string]): optional, list of keys to receive. GRPC returns
            all keys if not specified.
        height(int): optional, forge state of specific block height

    Returns:
        ResponseGetForgeState

    """

    request = protos.RequestGetForgeState(keys=keys,
                                          height=height)
    return stub.get_forge_state(request)
