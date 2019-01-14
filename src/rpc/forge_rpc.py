from collections import Iterator

import grpc

import protos


class ForgeRpc:
    def __init__(self, socket):
        self.chan = grpc.insecure_channel(socket)
        self.chain = protos.ChainRpcStub(self.chan)
        self.wallet = protos.WalletRpcStub(self.chan)
        self.state = protos.StateRpcStub(self.chan)
        self.file = protos.FileRpcStub(self.chan)

    # chain rpc

    def create_tx(self, **kwargs):
        if kwargs.get('req', None) is not None:
            return self.chain.create_tx(kwargs['req'])
        else:
            req_kwargs = {
                'itx': kwargs.get('itx', ''),
                'from': kwargs.get('from', ''),
                'nonce': kwargs.get('nonce', ''),
                'wallet': kwargs.get('wallet', ''),
                'token': kwargs.get('token', ''),
            }
            return self.chain.create_tx(protos.RequestCreateTx(**req_kwargs))

    def send_tx(self, **kwargs):
        if kwargs.get('req', None) is not None:
            return self.chain.send_tx(kwargs['req'])
        else:
            req_kwargs = {
                'tx': kwargs.get('tx', ''),
                'wallet': kwargs.get('wallet', ''),
                'commit': kwargs.get('commit', False),
                'token': kwargs.get('token', ''),
            }
            return self.chain.send_tx(protos.RequestSendTx(**req_kwargs))

    def get_tx(self, **kwargs):
        def to_req(item):
            if isinstance(item, protos.RequestGetTx):
                return item
            else:
                return protos.RequestGetTx(hash=item)

        if kwargs.get('req', None) is not None:
            return self.chain.get_tx(self.to_iter(to_req, kwargs['req']))
        else:
            hashes = self.to_iter(to_req, kwargs.get('hash', ''))
            return self.chain.get_tx(hashes)

    @staticmethod
    def __to_iter(to_req, items):
        if isinstance(items, Iterator):
            return map(to_req, items)
        else:
            req = to_req(items)
            return [req]  # map(lambda x: x, [req])

    def get_block(self, **kwargs):
        def to_req(item):
            if isinstance(item, protos.RequestGetBlock):
                return item
            else:
                return protos.RequestGetBlock(height=item)

        if kwargs.get('req', None) is not None:
            return self.chain.get_block(self.to_iter(to_req, kwargs['req']))
        else:
            heights = self.to_iter(to_req, kwargs.get('height', ''))
            return self.chain.get_block(heights)

    def get_chain_info(self):
        return self.chain.get_chain_info(protos.RequestGetChainInfo())

    def search(self, **kwargs):
        if kwargs.get('req', None) is not None:
            return self.chain.search(kwargs['req'])
        else:
            search_key = kwargs.get('key', '')
            search_value = kwargs.get('value', '')
            req = protos.RequestSearch(
                key=search_key, value=search_value,
            )
            return self.chain.search(req)

    # wallet rpc
    def create_wallet(self, **kwargs):
        if kwargs.get('req', None) is not None:
            return self.wallet.create_wallet(kwargs['req'])
        else:
            type = kwargs.get(
                'type', protos.WalletType(
                    pk=1, hash=1, address=1,
                ),
            )
            moniker = kwargs.get('moniker', '')
            passphrase = kwargs.get('passphrase', '')
            req = protos.RequestCreateWallet(
                type=type, moniker=moniker, passphrase=passphrase,
            )
            return self.wallet.create_wallet(req)

    def load_wallet(self, **kwargs):
        if kwargs.get('req', None) is not None:
            return self.chain.load_wallet(kwargs['req'])
        else:
            req_kwargs = {
                'address': kwargs.get('address', ''),
                'passphrase': kwargs.get('passphrase', ''),
            }
            return self.wallet.load_wallet(
                protos.RequestLoadWallet(**req_kwargs),
            )

    def recover_wallet(self, **kwargs):
        if kwargs.get('req', None) is not None:
            return self.wallet.recover_wallet(kwargs['req'])
        else:
            req_kwargs = {
                'data': kwargs.get('data', ''),
                'type': kwargs.get('type', ''),
                'passphrase': kwargs.get('passphrase', ''),
                'moniker': kwargs.get('moniker', ''),
            }
            return self.wallet.recover_wallet(
                protos.RequestRecoverWallet(**req_kwargs),
            )

    def list_wallets(self, **kwargs):
        return self.wallet.list_wallets(protos.RequestListWallets())

    def remove_wallet(self, **kwargs):
        if kwargs.get('req', None) is not None:
            return self.wallet.remove_wallet(kwargs['req'])
        else:
            req_kwargs = {
                'address': kwargs.get('address', ''),
            }
            return self.wallet.remove_wallet(
                protos.RequestRemoveWallet(**req_kwargs),
            )

    # state rpc
    def get_account_state(self, **kwargs):
        if kwargs.get('req', None) is not None:
            return self.wallet.get_account_state(kwargs['req'])
        else:
            req_kwargs = {
                'address': kwargs.get('address', ''),
                'key': kwargs.get('key', ''),
                'app_hash': kwargs.get('app_hash', ''),
            }
            return self.state.get_account_state(
                protos.RequestGetAccountState(**req_kwargs),
            )

    def get_asset_state(self, **kwargs):
        if kwargs.get('req', None) is not None:
            return self.wallet.get_asset_state(kwargs['req'])
        else:
            req_kwargs = {
                'address': kwargs.get('address'),
                'key': kwargs.get('key'),
                'app_hash': kwargs.get('app_hash'),
            }
            return self.state.get_asset_state(
                protos.RequestGetAssetState(req_kwargs),
            )

    def get_channel_state(self, **kwargs):
        if kwargs.get('req', None) is not None:
            return self.wallet.get_channel_state(kwargs['req'])
        else:
            req_kwargs = {
                'address': kwargs.get('address'),
                'key': kwargs.get('key'),
                'app_hash': kwargs.get('app_hash'),
            }
            return self.state.get_channel_state(
                protos.RequestGetChannelState(req_kwargs),
            )

    def get_forge_state(self, **kwargs):
        if kwargs.get('req', None) is not None:
            return self.wallet.get_forge_state(kwargs['req'])
        else:
            req_kwargs = {
                'key': kwargs.get('key', ''),
                'app_hash': kwargs.get('app_hash', ''),
            }
            return self.state.get_forge_state(
                protos.RequestGetForgeState(**req_kwargs),
            )

    # file rpc
    def store_file(self, **kwargs):
        def to_req(item):
            if isinstance(item, protos.RequestStoreFile):
                return item
            else:
                return protos.RequestStoreFile(chunk=item)

        if kwargs.get('req', None) is not None:
            return self.file.store_file(self.to_iter(to_req, kwargs['req']))
        else:
            chunks = self.to_iter(to_req, kwargs.get('chunk', ''))
            return self.file.store_file(chunks)

    def load_file(self, **kwargs):
        if kwargs.get('req', None) is not None:
            return self.file.load_file(kwargs['req'])
        else:
            req_kwargs = {
                'hash': kwargs.get('hash'),
            }
            return self.file.load_file(protos.RequestLoadFile(**req_kwargs))

    # def __getattr__(self, name):
    #     print("you're calling {0} method".format(name))
