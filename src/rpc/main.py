
import grpc
from protos import rpc_pb2_grpc, rpc_pb2
from config import parser

class ForgeRpc:
  def __init__(self, chan = None):
    if chan == None:
      socket_target = parser.parse_forge_toml()
      self.chan = grpc.insecure_channel(socket_target)
    else:
      self.chan = chan
    self.stub = rpc_pb2_grpc.ChainRpcStub(self.chan)
    
  def get_chain_info(self):
    return self.stub.get_chain_info(rpc_pb2.RequestGetChainInfo())

  def __getattr__(self, name):
    print("you're calling {0} method".format(name))
