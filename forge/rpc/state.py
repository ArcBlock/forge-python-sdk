from forge import protos
from forge.config import config
from forge.utils import utils

stub = protos.StateRpcStub(config.get_grpc_channel())


def get_account_state(queries, reqs=None):
    """GRPC call to get detailed of account

    Args:
        queries(dict): dictionaries of requested parameters
        reqs(list[:obj:`RequestGetAccountState`): stream of completed request

    Returns:
        ResponseGetAccountState(stream)

    """

    def to_req(item):
        if isinstance(item, protos.RequestGetAccountState):
            return item
        else:
            kwargs = {
                'address': item.get('address'),
                'keys': item.get('keys', []),
            }
            return protos.RequestGetAccountState(**kwargs)

    requests = reqs if reqs else utils.to_iter(to_req, queries)

    return stub.get_account_state(requests)


def get_asset_state(queries, reqs=None):
    """GRPC call to get detailed of asset

    Args:
        queries(dict): dictionaries of requested parameters
        reqs(list[:obj:`RequestGetAssetState`): stream of completed request

    Returns:
        ResponseGetAssetState(stream)
    """

    def to_req(item):
        if isinstance(item, protos.RequestGetAssetState):
            return item
        else:
            kwargs = {
                'address': item.get('address'),
                'keys': item.get('keys', []),
                # 'app_hash': item.get('app_hash', ''),
            }
            req = protos.RequestGetAssetState(**kwargs)
            return req

    requests = reqs if reqs else utils.to_iter(to_req, queries)

    return stub.get_asset_state(requests)


def get_stake_state(queries, reqs=None):
    """GRPC call to get detailed of stake

    Args:
        queries(dict): dictionaries of requested parameters
        reqs(list[:obj:`RequestGetStakeState`): stream of completed request

    Returns:
        ResponseGetStakeState(stream)

    """

    def to_req(item):
        if isinstance(item, protos.RequestGetStakeState):
            return item
        else:
            kwargs = {
                'address': item.get('address'),
                'keys': item.get('keys', []),
            }
            return protos.RequestGetStakeState(**kwargs)

    requests = reqs if reqs else utils.to_iter(to_req, queries)
    return stub.get_stake_state(requests)


def get_forge_state(keys=[], height=None, req=None):
    """ GRPC call to get forge state

    Args:
        keys(list[string]): optional, list of keys to receive. GRPC returns
            all keys if not specified.
        height(int): optional, forge state of specific block height
        req(:obj:`RequestGetForgeState`): completed request

    Returns:
        ResponseGetForgeState

    """
    if req is not None:
        return stub.get_forge_state(req)
    else:
        req_kwargs = {
            'keys': keys,
            'height': height,
        }
        return stub.get_forge_state(
            protos.RequestGetForgeState(**req_kwargs),
        )
