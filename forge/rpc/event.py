from forge import protos
from forge.config import config

stub = protos.EventRpcStub(config.get_grpc_channel())


def subscribe(type=0, filter=None, req=None):
    """ RPC request to subscribe to specific type of transactions

    Note:
        This request might block the python thread

    Args:
        type(:obj:`TopicType`): type of topic to subscribe
        filter(string): filter for targetd transactions
        req(:obj:`RequestSubscribe`): completed request

    Returns:
        ResponseSubscribe

    """

    if req:
        res = stub.subscribe(req)

    else:
        res = stub.subscribe(
            protos.RequestSubscribe(type=type, filter=filter),
        )
    for r in res:
        yield r


def unsubscribe(topic, req=None):
    """GRPC call to stop previously subscribed transactions

    Args:
        topic(string): topic id returned in subscribe request
        req(:obj:`RequestUnsubscribe`): completed reques

    Returns:
        ResponseUnsubscribe

    """
    """

    Parameters
    ----------
    topic: str
    req: RequestUnsubscribe

    Returns
    -------
    ResponseUnsubscribe

    """
    if req:
        return stub.unsubscribe(req)
    else:
        return stub.unsubscribe(
            protos.RequestUnsubscribe(topic=topic),
        )
