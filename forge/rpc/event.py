from forge import protos


class RpcEvent:

    def __init__(self, chan):
        self.stub = protos.EventRpcStub(chan)

    def subscribe(self, req=None, type=0, filter=None):
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
            res = self.stub.subscribe(req)

        else:
            res = self.stub.subscribe(
                protos.RequestSubscribe(type=type, filter=filter),
            )
        for r in res:
            yield r

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
        if req:
            return self.stub.unsubscribe(req)
        else:
            return self.stub.unsubscribe(
                protos.RequestUnsubscribe(topic=topic),
            )
