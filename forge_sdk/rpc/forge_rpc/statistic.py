from forge_sdk.config import config
from forge_sdk.protos import protos

stub = protos.StatsRpcStub(config.get_grpc_channel())


def get_forge_stats(day_info=None, date=None):
    """GRPC call to get statistics about forge

    Args:
        day_info(:obj:`Byday`): optional, date filter for information
        date(:obj:`ByHour`): optional, information returned by hour in specific
         day

    Returns:
        ResponseForgeStatistics

    """
    if day_info:
        return stub.get_forge_stats(
            protos.RequestGetForgeStats(day_info=day_info))
    elif date:
        return stub.get_(
            protos.RequestGetForgeStats(date=date))
    else:
        raise ValueError('Please pass either day_info or date for grpc call'
                         'get_forge_statistics.')


def list_assets(owner_address, paging=None):
    """GRPC call to list all assets under the given account address

    Args:
        owner_address(string): target account address
        paging(:obj:`PageInput`): optional, paging preference

    Returns:
        ResponseListAssets

    """
    request = protos.RequestListAssets(owner_address=owner_address,
                                       paging=paging)
    return stub.list_assets(request)


def list_stakes(address_filter=None, paging=None):
    """ GRPC call to get stakes

    Args:
        address_filter(:obj:`AddressFilter`): filter stakes to get
        paging(:obj:`PageInput`): paging preferences

    Returns:
        ResponseGetStakes

    """
    request = protos.RequestListStakes(address_filter=address_filter,
                                       paging=paging)
    return stub.list_stakes(request)


def list_top_accounts(paging=None):
    """GRPC call to get top accounts

    Args:
        paging(:obj:`PageInput`): paging preferences

    Returns:
        ResponseGetTopAccounts

    """
    request = protos.RequestListTopAccounts(paging=paging)
    return stub.list_top_accounts(request)


def list_blocks(paging=None, proposer=None, time_filter=None,
                height_filter=None, num_txs_filter=None,
                num_invalid_txs_filter=None):
    """GRPC call to list information of blocks

    Args:
        paging(:obj:`PageInput`): paging preferences
        proposer(string): address that proposed the block
        time_filter(:obj:`TimeFilter`): time filter
        height_filter(:obj: `RangeFilter`): height filter
        num_txs_filter(:obj:`RangeFilter`): number of transaction filter
        num_invalid_txs_filter(:obj:`RangeFilter` ): number of invalid
            transaction filter

    Returns:
        ResponseListBlocks

    """
    request = protos.RequestListBlocks(
        paging=paging, proposer=proposer, time_filter=time_filter,
        height_filter=height_filter, num_txs_filter=num_txs_filter,
        num_invalid_txs_filter=num_invalid_txs_filter
    )
    return stub.list_blocks(request)


def get_health_status():
    """GRPC call to get Forge health status

    Returns:
        ResponseGetHealthStatus

    """
    request = protos.RequestGetHealthStatus()
    return stub.get_health_status(request)


def list_asset_transactions(address, paging=None):
    """GRPC call to list transactions related to specific asset

    Args:
        address(string): asset address
        paging(:obj:`PageInput`): paging preferences

    Returns:
        ResponseListAssetTransaction

    """
    request = protos.RequestListAssetTransactions(
        address=address,
        paging=paging,
    )
    return stub.list_asset_transactions(request)


def list_transactions(
        address_filter=None, time_filter=None,
        type_filter=None, validity_filter=None, paging=None,
):
    """GRPC call to list transactions

    Args:
        address_filter(string): address filter
        time_filter(:obj:`TimeFilter`): time filter
        type_filter(:obj:`TypeFilter`): type filter
        validity_filter(:obj:`ValidityFilter`): validity filter
        paging(:obj:`PagingInput`): paging preference

    Returns:
        ResponseListTransactions

    """
    request = protos.RequestListTransactions(
        paging=paging,
        time_filter=time_filter,
        address_filter=address_filter,
        type_filter=type_filter,
        validity_filter=validity_filter,
    )
    return stub.list_transactions(request)
