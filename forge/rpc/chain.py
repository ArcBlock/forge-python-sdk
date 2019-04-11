from forge import protos
from forge.config import config
from forge.utils import utils

stub = protos.ChainRpcStub(config.get_grpc_channel())


def create_tx(itx, from_address,
              wallet=None, token=None, req=None, nonce=1,
              ):
    """ GRPC call to build a complete transaction, including sender's pk and
    sender's signature

    Note:
        To sign a transaction successfully, either a wallet with private key or
        a token should be provided. However, this practice is not recommended
        for safety concern. Users should keep their own private keys and sign
        transactions locally.

    Args:
        itx (:obj:`google.protobuf.Any`): Inner transaction that should be
            included in this transaction
        from_address (string) : address of user responsible for sending this
            transactions
        wallet (:obj:`WalletInfo`) : user wallet
        token (string): token provided by forge for using wallets stored on
            forge
        req (:obj:`RequestCreateTx`): complete request
        nonce (int): optional, number of tx this account has sent

    Returns:
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
        tx, wallet=None, token=None, commit=False, req=None,
):
    """GRPC call to send the included transaction

    Args:
        tx(:obj:`Transaction`): transaction to be sent
        wallet (:obj:`WalletInfo`) : user wallet
        token (string): token provided by forge for using wallets stored on
            forge
        commit(bool): option to wait until transaction was included in a block
        req(:obj: `RequestSendTx`): complete request

    Returns:
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


def get_tx(tx_hash, reqs=None):
    """ GRPC call to get detailed information of a transaction

    Args:
        tx_hash(string or list[string]): hash of the transaction
        reqs (RequestGetTx): list of request

    Returns:
         ResponseGetTx(stream)

    """

    def to_req(item):
        if isinstance(item, protos.RequestGetTx):
            return item
        else:
            return protos.RequestGetTx(hash=item)

    if reqs is not None:
        return stub.get_tx(utils.to_iter(to_req, reqs))
    else:
        return stub.get_tx(utils.to_iter(to_req, tx_hash))


def get_block(height, req=None):
    """ GRPC call to get blocks information

    Args:
        height(int or list[int]): height of the block
        req(:obj: `RequestGetBlock`): sream of requests

    Returns:
        ResponseGetBlock(stream)

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


def search(key, value, req=None):
    """GRPC call to search for specific key-value pair

    Args:
        key(string): key
        value(string): value
        req(:obj:`RequestSearch`): request

    Returns:
        ResponseSearch(stream)

    """
    if req is not None:
        return stub.search(req)
    else:
        req_kwargs = {
            'key': key,
            'value': value,
        }
        return stub.search(protos.RequestSearch(**req_kwargs))


def get_unconfirmed_tx(limit=1, req=None):
    """GRPC call to get currently unconfirmed transactions

    Args:
        limit(int): maximum number of transactions to get
        req(:obj:`RequestGetUnconfirmedTx`): request

    Returns:
        ResponseGetUnconfirmedTxs

    """
    if req is not None:
        return stub.get_unconfirmed_txs(req)
    else:
        return stub.get_unconfirmed_txs(
            protos.RequestGetUnconfirmedTxs(limit=limit),
        )


def get_chain_info(req=None):
    """ RPC call to get information about current chain

    Args:
        req(:obj:`RequestGetChainInfo`): request

    Returns:
        ResponseGetChainInfo

    """
    if req is not None:
        return stub.get_chain_info(req)
    else:
        return stub.get_chain_info(protos.RequestGetChainInfo())


def get_net_info(req=None):
    """RPC call to get information of the net

    Args:
        req(:obj:`RequestGetNetInfo`): Request

    Returns:
        ResponseGetNetInfo
    """
    if req is not None:
        return stub.get_net_info(req)
    else:
        return stub.get_net_info(protos.RequestGetNetInfo())


def get_validators_info(req=None):
    """GRPC call to get informations about al current validators

    Args:
        req(:obj:`RequestGetValidatorsInfo`: completed request

    Returns:
        ResponseGetValidatorsInfo

    """

    if req is not None:
        return stub.get_validators_info(req)
    else:
        return stub.get_validators_info(
            protos.RequestGetValidatorsInfo(),
        )


def get_config(req=None):
    """ RPC call to get detailed configuration current chain is using

    Args:
        req(:obj:`RequestGetConfig`): completed Request

    Returns:
        ResponseGetConfig

    """

    if req is not None:
        return stub.get_config(req)
    else:
        return stub.get_config(
            protos.RequestGetConfig(),
        )


def multisig(tx, wallet=None, token=None, data=None, req=None):
    """GRPC call to get multi-signature of a transaction. When executing this
    transactions, Forge will insert the address to `signatures` field as
    `Multisig.signer`, then create a signature of the entire transaction

    Args:
        tx(:obj:`Trasnaction`): transaction to be signed
        wallet (:obj:`WalletInfo`) : user wallet
        token (string): token provided by forge for using wallets stored on
            forge
        data(:obj:`google.protobuf.Any`): extra data to be included in multisig
        req(:obj:`RequestMultisig`): completed request

    Returns:
        ResponseMultisig

    """
    if req is not None:
        return stub.multisig(req)
    else:
        req = protos.RequestMultisig(
            tx=tx, wallet=wallet, token=token,
            data=data,
        )
        return stub.multisig(req)


def get_asset_address(
        sender_address, itx,
        wallet_type=None, req=None,
):
    """RPC call to get asset address calculated from createAssetTx and
    sender address

    Args:
        sender_address(string): address of the creator of this asset
        itx(:obj:`CreateAssetTx`): the inner transaction to create asset
        wallet_type(:obj:`WalletType`): deprecated
        req(:obj:`RequestGetAssetAddress`): completed request

    Returns:
        ResponseGetAssetAddress

    """
    if req is not None:
        return stub.get_asset_address(req)
    else:
        return stub.get_asset_address(
            protos.RequestGetAssetAddress(
                sender_address=sender_address, itx=itx,
                wallet_type=wallet_type,
            ),
        )


def get_blocks(min_height,
               max_height,
               empty_excluded=False,
               paging=None,
               req=None):
    """GRPC call to get information of blocks

    Args:
        min_height(int): minimum height of blocks
        max_height(int): maximum height of blocks
        empty_excluded(bool): whether to include empty blocks or not
        paging(:obj:`PageInput`): optional, paging preference
        req(:obj:`RequestGetBlocks`): completed request

    Returns:
        ResponseGetBlocks

    """
    if req:
        return stub.get_blocks(req)
    else:
        return stub.get_blocks(
            protos.RequestGetBlocks(
                paging=paging,
                min_height=min_height,
                max_height=max_height,
                empty_excluded=empty_excluded
            )
        )


def get_node_info(req=None):
    """GRPC call to get information of current node

    Args:
        req(:obj:`RequestGetNodeInfo`): completed request

    Returns:
        ResponseGetNodeInfo

    """
    if req:
        return stub.get_node_info(req)
    else:
        return stub.get_node_info(protos.RequestGetNodeInfo())


def sign_data(data, wallet, token, req=None):
    """ GRPC call to get signature for specific data

    Args:
        data(bytes): data needs to be signed
        wallet (:obj:`WalletInfo`) : user wallet
        token (string): token provided by forge for using wallets stored on
            forge
        req(:obj:`RequestSignData`): completed request

    Returns:
        ResponseSignData

    """
    if req:
        return stub.sign_data(req)
    else:
        return stub.sign_data(protos.RequestSignData(
            data=data, wallet=wallet, token=token
        ))
