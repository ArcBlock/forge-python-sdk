from forge_sdk.config import config
from forge_sdk.protos import protos

stub = protos.EventRpcStub(config.get_grpc_channel())


def subscribe(topic_type, tx_filter=None):
    """ RPC request to subscribe to specific type of transactions

    Note:
        This request might block the python thread

    Args:
        topic_type(:obj:`TopicType`): type of topic to subscribe
        tx_filter(string): filter for targetd transactions

    Returns:
        ResponseSubscribe

    """

    request = protos.RequestSubscribe(type=topic_type, filter=tx_filter)
    res = stub.subscribe(request)
    for r in res:
        yield r


def unsubscribe(topic):
    """GRPC call to stop previously subscribed transactions

    Args:
        topic(string): topic id returned in subscribe request

    Returns:
        ResponseUnsubscribe

    """
    request = protos.RequestUnsubscribe(topic=topic)
    return stub.unsubscribe(request)
