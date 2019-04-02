from forge import protos
from forge.config import config
from forge.utils import utils

stub = protos.ChainRpcStub(config.get_grpc_channel())


def create_tx(itx=None, from_address='',
              wallet=None, token=None, req=None, nonce=1,
              ):
    """RPC call to create transaction.

    Parameters
    ----------
    req : RequestCreateTx
    itx : google.protobuf.An
    from_address : string
    nonce : uint64
    wallet : WalletInfo
    token : string

    Returns
    -------
    ResponseCreateTx

    """

    if req is not None:
        return stub.create_tx(req)
    else:
        req_kwargs = {
            'itx': itx,
            'from': from_address,
            'nonce': nonce,
            'wallet': wallet,
            'token': token,
        }
        return stub.create_tx(protos.RequestCreateTx(**req_kwargs))


def send_tx(
        tx=None, wallet=None, token=None, commit=False, req=None,
):
    """
    RPC call to send transaction.

    Parameters
    ----------
    req: RequestSendTx
    tx : Transaction
    wallet: WalletInfo
    token: string
    commit: bool

    Returns
    -------
    ResponseSendTx

    """
    if req is not None:
        return stub.send_tx(req)
    else:
        req_kwargs = {
            'tx': tx,
            'wallet': wallet,
            'token': token,
            'commit': commit,
        }
        req = protos.RequestSendTx(**req_kwargs)
        return stub.send_tx(req)


def get_tx(tx_hash='', req=None):
    """
    RPC call to get transaction.

    Parameters
    ----------
    req: stream RequestGetTx
    tx_hash: single string or string iterator

    Returns
    -------
    stream  ResponseGetTx

    """

    def to_req(item):
        if isinstance(item, protos.RequestGetTx):
            return item
        else:
            return protos.RequestGetTx(hash=item)

    if req is not None:
        return stub.get_tx(utils.to_iter(to_req, req))
    else:
        return stub.get_tx(utils.to_iter(to_req, tx_hash))


def get_block(height=0, req=None):
    """
    RPC call to get blocks.

    Parameters
    ----------
    req: RequestGetBlock
    height: uint64

    Returns
    -------
    stream ResponseGetBlock

    """

    def to_req(item):
        if isinstance(item, protos.RequestGetBlock):
            return item
        else:
            return protos.RequestGetBlock(height=item)

    if req is not None:
        return stub.get_block(utils.to_iter(to_req, req))
    else:
        return stub.get_block(utils.to_iter(to_req, height))


def search(key='', value='', req=None):
    """

    Parameters
    ----------
    req: RequestSearch
    key: string
    value: string

    Returns
    -------
    ResponseSearch

    """
    if req is not None:
        return stub.search(req)
    else:
        req_kwargs = {
            'key': key,
            'value': value,
        }
        return stub.search(protos.RequestSearch(**req_kwargs))


def get_unconfirmed_tx(req=None, limit=1):
    """

    Parameters
    ----------
    req: RequestGetUnconfirmedTxs
    limit: int

    Returns
    -------
    ResponseGetUnconfirmedTxs

    """
    if req is not None:
        return stub.get_unconfirmed_txs(req)
    else:
        return stub.get_unconfirmed_txs(
            protos.RequestGetUnconfirmedTxs(limit=limit),
        )


def get_chain_info(req=None):
    """

    Parameters
    ----------
    req: RequestGetChainInfo

    Returns
    -------
    ResponseGetChainInfo

    """
    if req is not None:
        return stub.get_chain_info(req)
    else:
        return stub.get_chain_info(protos.RequestGetChainInfo())


def get_net_info(req=None):
    """

    Parameters
    ----------
    req: RequestGetNetInfo

    Returns
    -------
    ResponseGetNetInfo

    """
    if req is not None:
        return stub.get_net_info(req)
    else:
        return stub.get_net_info(protos.RequestGetNetInfo())


def get_validators_info(req=None):
    """

    Parameters
    ----------
    req: RequestGetValidatorsInfo

    Returns
    -------
    ResponseGetValidatorsInfo

    """
    if req is not None:
        return stub.get_validators_info(req)
    else:
        return stub.get_validators_info(
            protos.RequestGetValidatorsInfo(),
        )


def get_config(req=None):
    """

    Parameters
    ----------
    req: RequestGetConfig

    Returns
    -------
    ResponseGetConfig

    """
    if req is not None:
        return stub.get_config(req)
    else:
        return stub.get_config(
            protos.RequestGetConfig(),
        )


def multisig(tx=None, wallet=None, token=None, data=None, req=None):
    if req is not None:
        return stub.multisig(req)
    else:
        req = protos.RequestMultisig(
            tx=tx, wallet=wallet, token=token,
            data=data,
        )
        return stub.multisig(req)


def get_asset_address(
        sender_address='', itx=None,
        wallet_type=None, req=None,
):
    if req is not None:
        return stub.get_asset_address(req)
    else:
        return stub.get_asset_address(
            protos.RequestGetAssetAddress(
                sender_address=sender_address, itx=itx,
                wallet_type=wallet_type,
            ),
        )
