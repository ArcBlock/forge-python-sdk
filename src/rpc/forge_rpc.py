from protos import rpc_pb2_grpc, rpc_pb2
import grpc


class ForgeRpc:
    def __init__(self, socket):
        self.chan = grpc.insecure_channel(socket)
        self.stub = rpc_pb2_grpc.ChainRpcStub(self.chan)

    def get_chain_info(self):
        return self.stub.get_chain_info(rpc_pb2.RequestGetChainInfo())

    # def __getattr__(self, name):
    #     print("you're calling {0} method".format(name))
