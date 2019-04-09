from forge import protos
from forge.config import config

stub = protos.WalletRpcStub(config.get_grpc_channel())

__wallet_type = protos.WalletType(pk=0, hash=1, address=1)


def create_wallet(
        wallet_type=__wallet_type, moniker='',
        passphrase='', req=None,
):
    """GRPC call to create a wallet on Forge

    Note:
        the wallet created by this GRPC call will save encrypted private key
        on Forge node.

    Args:
        wallet_type(:obj:`WalletType`): the wallet type to create
        moniker(string): optional, nickname for wallet. Wallet will not be
            declared if no moniker is provided.
        passphrase(string): required, password to encrypt wallet
        req(:obj:`RequestCreateWallet`): completed request

    Returns:
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


def load_wallet(address, passphrase, req=None):
    """GRPC call to load wallet stored on Forge

    Args:
        address(string): address of the wallet stored
        passphrase(string): password used to create the wallet
        req(:obj:`ReqeustLoadWallet`): completed request

    Returns:
        ResponseLoadWallet

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
        passphrase, moniker, data,
        wallet_type=__wallet_type, req=None,
):
    """GRPC call to recover a wallet on forge

    Note:
        This GRPC call requires your private key. Please be careful when
        providing that information

    Args:
        passphrase(string): new passphrase to encrypt this wallet on Forge
        moniker(string): nickname for this wallet
        data(bytes): seed word or private key
        wallet_type(:obj:`WalletType`): deprecated
        req(:obj:`ReqeustRecoverWallet`): completed request

    Returns:
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
    """ GRPC call to list al wallets on current Forge Node

    Returns
        ResponseListWallets(stream)

    """
    return stub.list_wallet(protos.RequestListWallet())


def remove_wallet(address, req=None):
    """GRPC call to remove wallet with given address

    Args:
        address(string): address of wallet to be removed from Forge
        req(:obj:`RequestRemoveWallet`): completed request

    Returns:
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
    """GRPC call to declare current node

    Args:
        req(:obj:`RequestDeclareNode`: completed request

    Returns:
        ResponseDeclareNode

    """
    if req:
        return stub.declare_node(req)
    else:
        return stub.declare_node(protos.RequestDeclareNode())
