from forge import protos
from forge.config import config

stub = protos.StatisticRpcStub(config.get_grpc_channel())


def list_asset_transactions(address, paging=None):
    return stub.list_asset_transactions(
        protos.RequestListAssetTransactions(
            address=address,
            paging=paging,
        ),
    )


def list_transactions(
    address_filter, time_filter=None,
        type_filter=None, paging=None,
):
    req = protos.RequestListTransactions(
        paging=paging,
        time_filter=time_filter,
        address_filter=address_filter,
        type_filter=type_filter,
    )
    return stub.list_transactions(req)
