# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import event_pb2 as event__pb2


class EventRpcStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.subscribe = channel.unary_stream(
        '/forge_abi.EventRpc/subscribe',
        request_serializer=event__pb2.RequestSubscribe.SerializeToString,
        response_deserializer=event__pb2.ResponseSubscribe.FromString,
        )


class EventRpcServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def subscribe(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_EventRpcServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'subscribe': grpc.unary_stream_rpc_method_handler(
          servicer.subscribe,
          request_deserializer=event__pb2.RequestSubscribe.FromString,
          response_serializer=event__pb2.ResponseSubscribe.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'forge_abi.EventRpc', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
