from forge import protos
from forge.utils import utils


class RpcChain:
    def __init__(self, chan):
        self.stub = protos.ChainRpcStub(chan)

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
            return self.stub.create_tx(req)
        else:
            req_kwargs = {
                'itx': itx,
                'from': from_address,
                'nonce': nonce,
                'wallet': wallet,
                'token': token,
            }
            return self.stub.create_tx(protos.RequestCreateTx(**req_kwargs))

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
            return self.stub.send_tx(req)
        else:
            req_kwargs = {
                'tx': tx,
                'wallet': wallet,
                'token': token,
                'commit': commit,
            }
            req = protos.RequestSendTx(**req_kwargs)
            return self.stub.send_tx(req)

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
            return self.stub.get_tx(utils.to_iter(to_req, req))
        else:
            return self.stub.get_tx(utils.to_iter(to_req, tx_hash))

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
            return self.stub.get_block(utils.to_iter(to_req, req))
        else:
            return self.stub.get_block(utils.to_iter(to_req, height))

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
            return self.stub.search(req)
        else:
            req_kwargs = {
                'key': key,
                'value': value,
            }
            return self.stub.search(protos.RequestSearch(**req_kwargs))

    def get_unconfirmed_tx(self, req=None, limit=1):
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
            return self.stub.get_unconfirmed_txs(req)
        else:
            return self.stub.get_unconfirmed_txs(
                protos.RequestGetUnconfirmedTxs(limit=limit),
            )

    def get_chain_info(self, req=None):
        """

        Parameters
        ----------
        req: RequestGetChainInfo

        Returns
        -------
        ResponseGetChainInfo

        """
        if req is not None:
            return self.stub.get_chain_info(req)
        else:
            return self.stub.get_chain_info(protos.RequestGetChainInfo())

    def get_net_info(self, req=None):
        """

        Parameters
        ----------
        req: RequestGetNetInfo

        Returns
        -------
        ResponseGetNetInfo

        """
        if req is not None:
            return self.stub.get_net_info(req)
        else:
            return self.stub.get_net_info(protos.RequestGetNetInfo())

    def get_validators_info(self, req=None):
        """

        Parameters
        ----------
        req: RequestGetValidatorsInfo

        Returns
        -------
        ResponseGetValidatorsInfo

        """
        if req is not None:
            return self.stub.get_validators_info(req)
        else:
            return self.stub.get_validators_info(
                protos.RequestGetValidatorsInfo(),
            )

    def get_config(self, req=None):
        """

        Parameters
        ----------
        req: RequestGetConfig

        Returns
        -------
        ResponseGetConfig

        """
        if req is not None:
            return self.stub.get_config(req)
        else:
            return self.stub.get_config(
                protos.RequestGetConfig(),
            )
