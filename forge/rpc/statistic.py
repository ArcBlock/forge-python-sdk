from forge import protos


class RpcStatistic:
    def __init__(self, chan):
        self.stub = protos.StatisticRpcStub(chan)

    def list_asset_transactions(self, address, paging=None):
        return self.stub.list_asset_transactions(
            protos.RequestListAssetTransactions(
                address=address,
                paging=paging,
            ),
        )

    def list_transactions(
            self, address_filter, time_filter=None,
            type_filter=None, paging=None,
    ):
        req = protos.RequestListTransactions(
            paging=paging,
            time_filter=time_filter,
            address_filter=address_filter,
            type_filter=type_filter,
        )
        return self.stub.list_transactions(req)
