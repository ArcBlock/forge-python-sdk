from forge import protos
from forge.config import config

stub = protos.WalletRpcStub(config.get_grpc_channel())

__wallet_type = protos.WalletType(pk=0, hash=1, address=1)


def create_wallet(
        wallet_type=__wallet_type, moniker='',
        passphrase='', req=None,
):
    """

    Parameters
    ----------
    req: RequestCreateWallet
    wallet_type: WalletType
    moniker: string
    passphrase: string

    Returns
    -------
    ResponseCreateWallet

    """
    if req is not None:
        return stub.create_wallet(req)
    else:
        req_kwargs = {
            'type': wallet_type,
            'moniker': moniker,
            'passphrase': passphrase,
        }
        return stub.create_wallet(
            protos.RequestCreateWallet(**req_kwargs),
        )


def load_wallet(address='', passphrase='', req=None):
    """
    rpc call to load wallet.

    parameters
    ----------
    req: requestloadwallet
    address: string
    passphrase: string

    returns
    -------
    responseloadwallet

    """
    if req is not None:
        return stub.load_wallet(req)
    else:
        req_kwargs = {
            'address': address,
            'passphrase': passphrase,
        }
        return stub.load_wallet(
            protos.RequestLoadWallet(**req_kwargs),
        )


def recover_wallet(
        passphrase='', moniker='', data=b'',
        wallet_type=__wallet_type, req=None,
):
    """
    rpc call to recover wallet with given passphrase.

    parameters
    ----------
    passphrase: string
    moniker: string
    req: requestrecoverwallet
    data: bytes
        data could be bytes of seed words or secret key
    wallet_type: walletType

    Returns
    -------
    ResponseRecoverWallet

    """
    if req is not None:
        return stub.recover_wallet(req)
    else:
        req_kwargs = {
            'data': data,
            'type': wallet_type,
            'passphrase': passphrase,
            'moniker': moniker,
        }
        req = protos.RequestRecoverWallet(**req_kwargs)
        print(req)
        return stub.recover_wallet(req)


def list_wallet():
    """
    RPC call to list wallets

    Returns
    -------
    stream ResponseListWallets

    """
    return stub.list_wallet(protos.RequestListWallet())


def remove_wallet(address='', req=None):
    """
    RPC call to remove wallet with given address

    Parameters
    ----------
    req: RequestRemoveWallet
    address: string

    Returns
    -------
    ResponseRemoveWallet

    """
    if req is not None:
        return stub.remove_wallet(req)
    else:
        req_kwargs = {
            'address': address,
        }
        return stub.remove_wallet(
            protos.RequestRemoveWallet(**req_kwargs),
        )


def declare_node(req):
    """

    Parameters
    ----------
    req: RequestDeclareNode

    Returns
    -------
    ResponseDeclareNode

    """
    if req is not None:
        return stub.declare_node(req)
    else:
        return stub.declare_node(protos.RequestDeclareNode())
