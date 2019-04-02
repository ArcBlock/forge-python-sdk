from forge import protos


class RpcWallet:
    __wallet_type = protos.WalletType(pk=0, hash=1, address=1)

    def __init__(self, chan):
        self.stub = protos.WalletRpcStub(chan)

    def create_wallet(
            self, wallet_type=__wallet_type, moniker='',
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
            return self.stub.create_wallet(req)
        else:
            req_kwargs = {
                'type': wallet_type,
                'moniker': moniker,
                'passphrase': passphrase,
            }
            return self.stub.create_wallet(
                protos.RequestCreateWallet(**req_kwargs),
            )

    def load_wallet(self, address='', passphrase='', req=None):
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
            return self.stub.load_wallet(req)
        else:
            req_kwargs = {
                'address': address,
                'passphrase': passphrase,
            }
            return self.stub.load_wallet(
                protos.RequestLoadWallet(**req_kwargs),
            )

    def recover_wallet(
            self, passphrase='', moniker='', data=b'',
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
            return self.stub.recover_wallet(req)
        else:
            req_kwargs = {
                'data': data,
                'type': wallet_type,
                'passphrase': passphrase,
                'moniker': moniker,
            }
            req = protos.RequestRecoverWallet(**req_kwargs)
            print(req)
            return self.stub.recover_wallet(req)

    def list_wallet(self):
        """
        RPC call to list wallets

        Returns
        -------
        stream ResponseListWallets

        """
        return self.stub.list_wallet(protos.RequestListWallet())

    def remove_wallet(self, address='', req=None):
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
            return self.stub.remove_wallet(req)
        else:
            req_kwargs = {
                'address': address,
            }
            return self.stub.remove_wallet(
                protos.RequestRemoveWallet(**req_kwargs),
            )

    def declare_node(self, req):
        """

        Parameters
        ----------
        req: RequestDeclareNode

        Returns
        -------
        ResponseDeclareNode

        """
        if req is not None:
            return self.stub.declare_node(req)
        else:
            return self.stub.declare_node(protos.RequestDeclareNode())
