from forge_sdk.config import config
from forge_sdk.protos import protos
from forge_sdk.rpc import lib

stub = protos.ChainRpcStub(config.get_grpc_channel())


def create_tx(itx, from_address,
              wallet=None, token=None, nonce=1,
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
        nonce (int): optional, number of tx this account has sent

    Returns:
        :obj:`ResponseCreateTx`

    Examples:
        >>> from forge_sdk import rpc, protos, utils
        >>> user = rpc.create_wallet(moniker='alice', passphrase='abc123')
        >>> itx = utils.encode_to_any('fg:t:transfer', protos.TransferTx(to='zysnfkW9LH5jVUubpwcrGaopnN2oDBPTLmuP',value=protos.BigUint(value=b'\x01')))
        >>> create_tx(itx, user.wallet.address, user.wallet, user.token)
    """

    req_kwargs = {
        'itx': itx,
        'from': from_address,
        'nonce': nonce,
        'wallet': wallet,
        'token': token,
    }
    request = protos.RequestCreateTx(**req_kwargs)
    return stub.create_tx(request)


def send_tx(
        tx, wallet=None, token=None, commit=False,
):
    """GRPC call to send the included transaction

    Args:
        tx(:obj:`Transaction`): transaction to be sent
        wallet (:obj:`WalletInfo`) : user wallet
        token (string): token provided by forge for using wallets stored on
            forge
        commit(bool): option to wait until transaction was included in a block

    Returns:
            ResponseSendTx

    """
    req_kwargs = {
        'tx': tx,
        'wallet': wallet,
        'token': token,
        'commit': commit,
    }
    request = protos.RequestSendTx(**req_kwargs)
    return stub.send_tx(request)


def get_tx(tx_hash):
    """ GRPC call to get detailed information of a transaction

    Args:
        tx_hash(string or list[string]): hash of the transaction

    Returns:
         ResponseGetTx(stream)

    """

    def to_req(item):
        return protos.RequestGetTx(hash=item)

    requests = lib.to_iter(to_req, tx_hash)
    return stub.get_tx(requests)


def get_block(height):
    """ GRPC call to get blocks information

    Args:
        height(int or list[int]): height of the block

    Returns:
        ResponseGetBlock(stream)

    """

    def to_req(item):
        return protos.RequestGetBlock(height=item)

    requests = lib.to_iter(to_req, height)
    return stub.get_block(requests)


def search(key, value):
    """GRPC call to search for specific key-value pair

    Args:
        key(string): key
        value(string): value

    Returns:
        ResponseSearch(stream)

    """
    request = protos.RequestSearch(key=key,
                                   value=value)
    return stub.search(request)


def get_unconfirmed_tx(paging=None):
    """GRPC call to get currently unconfirmed transactions

    Args:
        paging(:obj:`PageInput`): paging preference

    Returns:
        ResponseGetUnconfirmedTxs

    """
    request = protos.RequestGetUnconfirmedTxs(paging=paging)
    return stub.get_unconfirmed_txs(request)


def get_chain_info():
    """ RPC call to get information about current chain

    Returns:
        ResponseGetChainInfo

    """
    request = protos.RequestGetChainInfo()
    return stub.get_chain_info(request)


def get_net_info():
    """RPC call to get information of the net

    Returns:
        ResponseGetNetInfo
    """
    request = protos.RequestGetNetInfo()
    return stub.get_net_info(request)


def get_validators_info():
    """GRPC call to get informations about al current validators

    Returns:
        ResponseGetValidatorsInfo

    """
    request = protos.RequestGetValidatorsInfo()
    return stub.get_validators_info(request)


def get_config():
    """ RPC call to get detailed configuration current chain is using

    Returns:
        ResponseGetConfig

    """

    request = protos.RequestGetConfig()
    return stub.get_config(request)


def multisig(tx, wallet=None, token=None, data=None):
    """GRPC call to get multi-signature of a transaction. When executing this
    transactions, Forge will insert the address to `signatures` field as
    `Multisig.signer`, then create a signature of the entire transaction

    Args:
        tx(:obj:`Trasnaction`): transaction to be signed
        wallet (:obj:`WalletInfo`) : user wallet
        token (string): token provided by forge for using wallets stored on
            forge
        data(:obj:`google.protobuf.Any`): extra data to be included in multisig

    Returns:
        ResponseMultisig

    """
    request = protos.RequestMultisig(
        tx=tx, wallet=wallet, token=token,
        data=data,
    )
    return stub.multisig(request).tx


def get_blocks(height_filter,
               empty_excluded=False,
               paging=None):
    """GRPC call to get information of blocks

    Args:
        height_filter(:obj:`RangeFilter`): range filter for blocks
        empty_excluded(bool): whether to include empty blocks or not
        paging(:obj:`PageInput`): optional, paging preference

    Returns:
        ResponseGetBlocks

    """
    request = protos.RequestGetBlocks(
        height_filter=height_filter,
        paging=paging,
        empty_excluded=empty_excluded
    )
    return stub.get_blocks(request)


def get_node_info():
    """GRPC call to get information of current node

    Returns:
        ResponseGetNodeInfo
    """
    request = protos.RequestGetNodeInfo()
    return stub.get_node_info(request)
