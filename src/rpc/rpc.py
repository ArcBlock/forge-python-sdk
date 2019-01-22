from collections import Iterator

import grpc

import protos


class ForgeRpc:
    __wallet_type = protos.WalletType(pk=0, hash=1, address=1)

    def __init__(self, socket):
        """
        Init Forge RPC with given socket.

        Args:
            socket: string of TCP/UDS socket
        """
        self.chan = grpc.insecure_channel(socket)
        self.chain = protos.ChainRpcStub(self.chan)
        self.wallet = protos.WalletRpcStub(self.chan)
        self.state = protos.StateRpcStub(self.chan)
        self.file = protos.FileRpcStub(self.chan)

    def create_tx(
            self, req=None, itx=None, from_address='', nonce=0,
            wallet=None, token='',
    ):
        """
        RPC call to create transaction.

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
            return self.chain.create_tx(req)
        else:
            req_kwargs = {
                'itx': itx,
                'from': from_address,
                'nonce': nonce,
                'wallet': wallet,
                'token': token,
            }
            return self.chain.create_tx(protos.RequestCreateTx(**req_kwargs))

    def send_tx(
            self, req=None, tx=None, wallet=None, token='', commit=False,
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
            return self.chain.send_tx(req)
        else:
            req_kwargs = {
                'tx': tx,
                'wallet': wallet,
                'token': token,
                'commit': commit,
            }
            req = protos.RequestSendTx(**req_kwargs)
            return self.chain.send_tx(req)

    def get_tx(self, req=None, tx_hash=''):
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
                return protos.RequestGetTx(hash=tx_hash)

        if req is not None:
            return self.chain.get_tx(self.__to_iter(to_req, req))
        else:
            hashes = self.__to_iter(to_req, tx_hash)
            return self.chain.get_tx(hashes)

    @staticmethod
    def __to_iter(to_req, items):
        if isinstance(items, Iterator):
            return map(to_req, items)
        else:
            req = to_req(items)
            return [req]

    def get_block(self, req=None, height=0):
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
            return self.chain.get_block(self.__to_iter(to_req, req))
        else:
            heights = self.__to_iter(to_req, height)
            return self.chain.get_block(heights)

    def get_chain_info(self):
        """
        RPC call to get chain info.

        Returns
        -------
        ResponseChainInfo

        """
        return self.chain.get_chain_info(protos.RequestGetChainInfo())

    def search(self, req=None, key='', value=''):
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
            return self.chain.search(req)
        else:
            req_kwargs = {
                'key': key,
                'value': value,
            }
            return self.chain.search(protos.RequestSearch(**req_kwargs))

    def create_wallet(
            self, req=None, wallet_type=__wallet_type, moniker='',
            passphrase='',
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
            return self.wallet.create_wallet(req)
        else:
            req_kwargs = {
                'type': wallet_type,
                'moniker': moniker,
                'passphrase': passphrase,
            }
            return self.wallet.create_wallet(
                protos.RequestCreateWallet(**req_kwargs),
            )

    def load_wallet(self, req=None, address='', passphrase=''):
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
            return self.wallet.load_wallet(req)
        else:
            req_kwargs = {
                'address': address,
                'passphrase': passphrase,
            }
            return self.wallet.load_wallet(
                protos.RequestLoadWallet(**req_kwargs),
            )

    def recover_wallet(
            self, passphrase='', moniker='', req=None, data=b'',
            wallet_type=__wallet_type,
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
            print(req)
            return self.wallet.recover_wallet(req)
        else:
            req_kwargs = {
                'data': data,
                'type': wallet_type,
                'passphrase': passphrase,
                'moniker': moniker,
            }
            req = protos.RequestRecoverWallet(**req_kwargs)
            print(req)
            return self.wallet.recover_wallet(
                req,
            )

    def list_wallets(self):
        """
        RPC call to list wallets

        Returns
        -------
        stream ResponseListWallets

        """
        return self.wallet.list_wallets(protos.RequestListWallets())

    def remove_wallet(self, req=None, address=''):
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
            return self.wallet.remove_wallet(req)
        else:
            req_kwargs = {
                'address': address,
            }
            return self.wallet.remove_wallet(
                protos.RequestRemoveWallet(**req_kwargs),
            )

    def get_account_state(self, req=None):
        """
        RPC call to get account state.

        Parameters
        ----------
        req: stream RequestGetAccountState

        Returns
        -------
        stream ResponseGetAccountState

        """

        return self.state.get_account_state(req)

    def get_asset_state(self, req=None):
        """
        RPC call to get asset state.

        Parameters
        ----------
        req: stream RequestGetAssetState

        Returns
        -------
        stream ResponseGetAssetState

        """

        return self.state.get_account_state(req)

    def get_channel_state(self, req=None):
        """
        RPC call to get channel state.

        Parameters
        ----------
        req: stream RequestGetChannelState

        Returns
        -------
        stream ResponseGetChannelState

        """

        return self.state.get_channel_state(req)

    def get_forge_state(self, req=None, key='', tx_hash=''):
        """
        RPC call to get forge state.

        Parameters
        ----------
        req: RequestGetForgeState

        Returns
        -------
        ResponseGetForgeState

        """
        if req is not None:
            return self.state.get_forge_state(req)
        else:
            req_kwargs = {
                'key': key,
                'hash': tx_hash,
            }
            return self.state.get_forge_state(**req_kwargs)

    def store_file(self, req=None, chunk=b''):
        """
        RPC call to store file

        Parameters
        ----------
        req: stream RequestStoreFile
        chunk: iterator of bytes

        Returns
        -------
        ResponseStoreFile

        """

        def to_req(item):
            if isinstance(item, protos.RequestStoreFile):
                return item
            else:
                return protos.RequestStoreFile(chunk=item)

        if req is not None:
            return self.file.store_file(self.__to_iter(to_req, req))
        else:
            chunks = self.__to_iter(to_req, chunk)
            return self.file.store_file(chunks)

    def load_file(self, req=None, file_hash=''):
        """
        RPC call to load file.

        Parameters
        ----------
        req: RequestLoadFile
        file_hash: string

        Returns
        -------
        stream ResponseLoadFile

        """
        if req is not None:
            return self.file.load_file(req)
        else:
            req_kwargs = {
                'hash': file_hash,
            }
            return self.file.load_file(protos.RequestLoadFile(**req_kwargs))

    # def __getattr__(self, name):
    #     print("you're calling {0} method".format(name))
