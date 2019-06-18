from forge_sdk.protos import protos


class ForgeEventRpc:

    def __init__(self, channel):
        self.stub = protos.EventRpcStub(channel)

    def subscribe(self, topic_type, tx_filter=None):
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
        res = self.stub.subscribe(request)
        for r in res:
            yield r

    def unsubscribe(self, topic):
        """GRPC call to stop previously subscribed transactions

        Args:
            topic(string): topic id returned in subscribe request

        Returns:
            ResponseUnsubscribe

        """
        request = protos.RequestUnsubscribe(topic=topic)
        return self.stub.unsubscribe(request)
