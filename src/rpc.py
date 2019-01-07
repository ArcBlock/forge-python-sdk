import grpc
from protos import rpc_pb2_grpc, rpc_pb2


def run():
    channel = grpc.insecure_channel(
        'unix:///Users/tchen/.forge/core/socks/forge_grpc.sock')
    stub = rpc_pb2_grpc.ChainRpcStub(channel)
    response = stub.get_chain_info(rpc_pb2.RequestGetChainInfo())
    print('Chain info:', response)


if __name__ == "__main__":
    run()
