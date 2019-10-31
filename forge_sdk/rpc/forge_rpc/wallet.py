from forge_sdk.protos import protos

_wallet_type = protos.WalletType(pk=0, hash=1, address=1)


class ForgeWalletRpc:

    def __init__(self, channel):
        self.stub = protos.WalletRpcStub(channel)

    def declare_node(self):
        """GRPC call to declare current node

        Returns:
            ResponseDeclareNode

        """
        return self.stub.declare_node(protos.RequestDeclareNode())
