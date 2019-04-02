from forge import protos
from forge.config import config

stub = protos.EventRpcStub(config.get_grpc_channel())


def subscribe(req=None, type=0, filter=None):
    """

    Parameters
    ----------
    req: RequestSubscribe
    type: protos.TopicType
    filter: str

    Returns
    -------
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


def unsubscribe(topic='', req=None):
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
