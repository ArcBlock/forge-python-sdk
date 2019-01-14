import grpc

import protos


class ForgeRpc:
    def __init__(self, socket):
        self.chan = grpc.insecure_channel(socket)
        self.chain = protos.ChainRpcStub(self.chan)
        self.wallet = protos.WalletRpcStub(self.chan)

    def get_chain_info(self):
        return self.chain.get_chain_info(protos.RequestGetChainInfo())

    def create_wallet(self, **kwargs):
        if kwargs.get('req', None) is not None:
            return self.wallet.create_wallet(kwargs['req'])
        else:
            # sanity check
            # type is empty, use default forge type
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

    # def __getattr__(self, name):
    #     print("you're calling {0} method".format(name))
