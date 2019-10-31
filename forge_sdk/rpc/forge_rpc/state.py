from forge_sdk.protos import protos
from forge_sdk.rpc import lib


class ForgeStateRpc:

    def __init__(self, channel):
        self.stub = protos.StateRpcStub(channel)

    def get_account_state(self, queries):
        """GRPC call to get detailed of account

        Args:
            queries(dict): dictionaries of requested parameters

        Returns:
            ResponseGetAccountState(stream)

        """

        def to_req(query):
            return protos.RequestGetAccountState(
                    address=query.get('address'),
                    keys=query.get('keys'),
                    height=query.get('height')
            )

        requests = lib.to_iter(to_req, queries)

        return self.stub.get_account_state(requests)

    def get_asset_state(self, queries):
        """GRPC call to get detailed of asset

        Args:
            queries(dict): dictionaries of requested parameters

        Returns:
            ResponseGetAssetState(stream)
        """

        def to_req(query):
            return protos.RequestGetAssetState(
                    address=query.get('address'),
                    keys=query.get('keys'),
                    height=query.get('height'),
            )

        requests = lib.to_iter(to_req, queries)

        return self.stub.get_asset_state(requests)

    def get_protocol_state(self, queries):
        """GRPC call to get detailed of asset

        Args:
            queries(dict): dictionaries of requested parameters

        Returns:
            ResponseGetAssetState(stream)
        """

        def to_req(query):
            return protos.RequestGetProtocolState(
                    address=query.get('address'),
                    keys=query.get('keys'),
                    height=query.get('height'),
            )

        requests = lib.to_iter(to_req, queries)

        return self.stub.get_protocol_state(requests)

    def get_delegate_state(self, queries):
        """GRPC call to get detailed of stake

        Args:
            queries(dict): dictionaries of requested parameters

        Returns:
            ResponseGetStakeState(stream)

        """

        def to_req(query):
            return protos.RequestGetDelegateState(
                    address=query.get('address'),
                    keys=query.get('keys'),
                    height=query.get('height'),
            )

        requests = lib.to_iter(to_req, queries)
        return self.stub.get_delegate_state(requests)

    def get_swap_state(self, queries):
        """GRPC call to get state of tether

        Args:
            queries(dict): dictionaries of requested parameters

        Returns:
            ResponseGetTetherState(stream)

        """

        def to_req(query):
            return protos.RequestGetSwapState(
                    address=query.get('address'),
                    keys=query.get('keys'),
                    height=query.get('height'),
            )

        requests = lib.to_iter(to_req, queries)

        return self.stub.get_swap_state(requests)

    def get_forge_state(self, keys=None, height=None):
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
        return self.stub.get_forge_state(request)

    def get_forge_token(self):
        """
        Get Forge Token

        Returns:
            (:obj:`ForgeToken`)

        """

        return self.get_forge_state(['token']).state.token
