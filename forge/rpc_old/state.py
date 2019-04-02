from forge import protos
from forge.utils import utils


class RpcState:
    def __init__(self, chan):
        self.stub = protos.StateRpcStub(chan)

    def get_account_state(self, req):
        """
        RPC call to get account state.

        Parameters
        ----------
        req: stream RequestGetAccountState

        Returns
        -------
        stream ResponseGetAccountState

        """

        def to_req(item):
            if isinstance(item, protos.RequestGetAccountState):
                return item
            else:
                kwargs = {
                    'address': item.get('address'),
                    'keys': item.get('keys', []),
                    # 'height': item.get('height', ''),
                }
                return protos.RequestGetAccountState(**kwargs)

        requests = utils.to_iter(to_req, req)

        return self.stub.get_account_state(requests)

    def get_asset_state(self, req=None):
        """
        RPC call to get asset state.

        Parameters
        ----------
        req: stream RequestGetAssetState

        Returns
        -------
        stream ResponseGetAssetState

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

        requests = utils.to_iter(to_req, req)

        return self.stub.get_asset_state(requests)

    def get_stake_state(self, req=None):
        """
        RPC call to get stake state.

        Parameters
        ----------
        req: stream RequestGetStakeState

        Returns
        -------
        stream ResponseGetChannelState

        """

        def to_req(item):
            if isinstance(item, protos.RequestGetStakeState):
                return item
            else:
                kwargs = {
                    'address': item.get('address'),
                    'keys': item.get('keys', []),
                    # 'app_hash': item.get('app_hash', ''),
                }
                return protos.RequestGetStakeState(**kwargs)

        requests = utils.to_iter(to_req, req)
        return self.stub.get_stake_state(requests)

    def get_forge_state(self, keys='', app_hash='', req=None):
        """
        RPC call to get forge state.

        Parameters
        ----------
        req: RequestGetForgeState

        Returns
        -------
        ResponseGetForgeState

        """
        if req is not None:
            return self.stub.get_forge_state(req)
        else:
            req_kwargs = {
                'keys': keys,
                # 'app_hash': app_hash,
            }
            return self.stub.get_forge_state(
                protos.RequestGetForgeState(**req_kwargs),
            )
