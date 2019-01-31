from forge import protos


class RpcEvent:

    def __init__(self, chan):
        self.stub = protos.EventRpcStub(chan)

    def subscribe(self, req=None, type=0, filter=''):
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
        if not req:
            return self.stub.subscribe(req)
        else:
            return self.stub.subscribe(
                protos.RequestSubscribe(type=type, filter=filter),
            )

    def unsubscribe(self, topic='', req=None):
        """

        Parameters
        ----------
        topic: str
        req: RequestUnsubscribe

        Returns
        -------
        ResponseUnsubscribe

        """
        if not req:
            return self.stub.unsubscribe(req)
        else:
            return self.stub.unsubscribe(
                protos.RequestUnsubscribe(topic=topic),
            )
