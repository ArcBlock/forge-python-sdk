from collections import Iterable

import grpc

from .. import protos


def to_iter(to_req, data):
    if isinstance(data, dict) or isinstance(data, str):
        return iter([to_req(data)])
    elif isinstance(data, Iterable):
        return (to_req(i) for i in data)
    else:
        return iter([data])


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
            self, itx=None, from_address='', nonce=0,
            wallet=None, token='', req=None,
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
            self, tx=None, wallet=None, token='', commit=False, req=None,
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

    def get_tx(self, tx_hash='', req=None):
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
            return self.chain.get_tx(to_iter(to_req, req))
        else:
            return self.chain.get_tx(to_iter(to_req, tx_hash))

    def get_block(self, height=0, req=None):
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
            return self.chain.get_block(to_iter(to_req, req))
        else:
            return self.chain.get_block(to_iter(to_req, height))

    def get_chain_info(self):
        """
        RPC call to get chain info.

        Returns
        -------
        ResponseChainInfo

        """
        return self.chain.get_chain_info(protos.RequestGetChainInfo())

    def search(self, key='', value='', req=None):
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
            return self.wallet.recover_wallet(req)
        else:
            req_kwargs = {
                'data': data,
                'type': wallet_type,
                'passphrase': passphrase,
                'moniker': moniker,
            }
            req = protos.RequestRecoverWallet(**req_kwargs)
            return self.wallet.recover_wallet(req)

    def list_wallet(self):
        """
        RPC call to list wallets

        Returns
        -------
        stream ResponseListWallets

        """
        return self.wallet.list_wallet(protos.RequestListWallet())

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
            return self.wallet.remove_wallet(req)
        else:
            req_kwargs = {
                'address': address,
            }
            return self.wallet.remove_wallet(
                protos.RequestRemoveWallet(**req_kwargs),
            )

    def get_account_state(self, req):
        """
        RPC call to get account state.

        Parameters
        ----------
        req: stream RequestGetAccountState

        Returns
        -------
        stream ResponseGetAccountState

        """

        def to_req(item):
            if isinstance(item, protos.RequestGetAccountState):
                return item
            else:
                kwargs = {
                    'address': item.get('address'),
                    'keys': item.get('keys', []),
                    'app_hash': item.get('app_hash', ''),
                }
                return protos.RequestGetAccountState(**kwargs)

        requests = to_iter(to_req, req)

        return self.state.get_account_state(requests)

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

        def to_req(item):
            if isinstance(item, protos.RequestGetAssetState):
                return item
            else:
                kwargs = {
                    'address': item.get('address'),
                    'keys': item.get('keys', []),
                    'app_hash': item.get('app_hash', ''),
                }
                return protos.RequestGetAssetState(**kwargs)

        requests = to_iter(to_req, req)

        return self.state.get_asset_state(requests)

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

        def to_req(item):
            if isinstance(item, protos.RequestGetChannelState):
                return item
            else:
                kwargs = {
                    'address': item.get('address'),
                    'keys': item.get('keys', []),
                    'app_hash': item.get('app_hash', ''),
                }
                return protos.RequestGetChannelState(**kwargs)

        requests = to_iter(to_req, req)
        return self.state.get_channel_state(requests)

    def get_forge_state(self, keys='', app_hash='', req=None):
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
                'keys': keys,
                'app_hash': app_hash,
            }
            return self.state.get_forge_state(
                protos.RequestGetForgeState(**req_kwargs),
            )

    def store_file(self, chunk=b'', req=None):
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
            return self.file.store_file(to_iter(to_req, req))
        else:
            chunks = to_iter(to_req, chunk)
            return self.file.store_file(chunks)

    def load_file(self, file_hash='', req=None):
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
