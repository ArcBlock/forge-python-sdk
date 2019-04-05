from forge import protos
from forge.config import config

stub = protos.StatisticRpcStub(config.get_grpc_channel())


def get_forge_statistics(day_info=None, date=None, req=None):
    if req:
        return stub.get_forge_statistics(req)
    elif day_info:
        return stub.get_forge_statistics(
            protos.RequestGetForgeStatistics(day_info=day_info))
    elif date:
        return stub.get_forge_statistics(
            protos.RequestGetForgeStatistics(date=date))
    else:
        raise ValueError('Please pass either day_info or date for grpc call'
                         'get_forge_statistics.')


def list_assets(owner_address, paging=None, req=None):
    if req:
        return stub.list_assets(req)
    else:
        return stub.list_assets(
            protos.RequestListAssets(owner_address=owner_address,
                                     paging=paging))


def get_stakes(address_filter=None, paging=None, req=None):
    if req:
        return stub.get_stakes(req)
    else:
        return stub.get_stakes(
            protos.RequestGetStakes(address_filter=address_filter,
                                    paging=paging))


def get_top_accounts(paging=None, req=None):
    if req:
        return stub.get_top_accounts(req)
    else:
        return stub.get_top_accounts(
            protos.RequestGetTopAccounts(paging=paging))


def list_blocks(paging=None, proposer=None, time_filter=None,
                height_filter=None, num_txs_filter=None,
                num_invalid_txs_filter=None, req=None):
    if req:
        return stub.list_blocks(req)
    else:
        return stub.list_blocks(protos.RequestListBlocks(
            paging=paging, proposer=proposer, time_filter=time_filter,
            height_filter=height_filter, num_txs_filter=num_txs_filter,
            num_invalid_txs_filter=num_invalid_txs_filter
        ))


def get_health_status(req=None):
    if req:
        return stub.get_health_status(req)
    else:
        return stub.get_health_status(protos.RequestGetHealthStatus())


def list_asset_transactions(address=None, paging=None, req=None):
    if req:
        return stub.list_asset_transactions(req)
    else:
        return stub.list_asset_transactions(
            protos.RequestListAssetTransactions(
                address=address,
                paging=paging,
            ),
        )


def list_transactions(
        address_filter=None, time_filter=None,
        type_filter=None, paging=None,
):
    req = protos.RequestListTransactions(
        paging=paging,
        time_filter=time_filter,
        address_filter=address_filter,
        type_filter=type_filter,
    )
    return stub.list_transactions(req)
