from forge_sdk.protos import protos

_wallet_type = protos.WalletType(pk=0, hash=1, address=1)


class ForgeWalletRpc:

    def __init__(self, channel):
        self.stub = protos.WalletRpcStub(channel)

    def create_wallet(self, passphrase,
                      wallet_type=_wallet_type, moniker=''):
        """GRPC call to create a wallet on Forge

        Note:
            the wallet created by this GRPC call will save encrypted private
            key
            on Forge node.

        Args:
            passphrase(string): required, password to encrypt wallet
            wallet_type(:obj:`WalletType`): the wallet type to create
            moniker(string): optional, nickname for wallet. Wallet will not be
                declared if no moniker is provided.

        Returns:
            ResponseCreateWallet

        """
        req_kwargs = {
            'type': wallet_type,
            'moniker': moniker,
            'passphrase': passphrase,
        }
        request = protos.RequestCreateWallet(**req_kwargs)
        return self.stub.create_wallet(request)

    def load_wallet(self, address, passphrase):
        """GRPC call to load wallet stored on Forge

        Args:
            address(string): address of the wallet stored
            passphrase(string): password used to create the wallet

        Returns:
            ResponseLoadWallet

        """
        request = protos.RequestLoadWallet(address=address,
                                           passphrase=passphrase)
        return self.stub.load_wallet(request)

    def recover_wallet(self,
                       passphrase, moniker, data,
                       wallet_type=_wallet_type
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

        Returns:
            ResponseRecoverWallet

        """
        req_kwargs = {
            'data': data,
            'type': wallet_type,
            'passphrase': passphrase,
            'moniker': moniker,
        }
        request = protos.RequestRecoverWallet(**req_kwargs)
        return self.stub.recover_wallet(request)

    def remove_wallet(self, address):
        """GRPC call to remove wallet with given address

        Args:
            address(string): address of wallet to be removed from Forge

        Returns:
            ResponseRemoveWallet

        """
        request = protos.RequestRemoveWallet(address=address)
        return self.stub.remove_wallet(request)

    def declare_node(self):
        """GRPC call to declare current node

        Returns:
            ResponseDeclareNode

        """
        return self.stub.declare_node(protos.RequestDeclareNode())
