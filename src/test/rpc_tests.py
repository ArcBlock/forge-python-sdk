import unittest

from google.protobuf.any_pb2 import Any
from rpc import ForgeRpc

import protos
from protos import BigSint
from protos import TransferTx


class RpcTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(RpcTest, self).__init__(*args, **kwargs)
        self.rpc = ForgeRpc("127.0.0.1:28210")
        self.wallet_type = protos.WalletType(pk=0, hash=1, address=1)
        self.wallet1 = self.init_wallet('bobalice')
        self.transfer_tx = TransferTx(
            to=self.wallet1.walletInfo.address,
            value=BigSint(
                value=b'100',
            ),
        )
        self.trans_itx = Any(
            type_url='ft/Transfer',
            value=self.transfer_tx.SerializeToString(),
        )
        self.chain_id = int(self.rpc.get_chain_info().info.network)

    def init_wallet(self, moniker):
        res = self.rpc.create_wallet(
            wallet_type=self.wallet_type,
            moniker=moniker,
            passphrase='abc123',
        )
        return Wallet(res.token, res.wallet)

    def verify_tx(self, response):
        res_tx = TransferTx()
        res_tx.ParseFromString(response.tx.itx.value)
        assert res_tx.to == self.transfer_tx.to
        assert res_tx.value == self.transfer_tx.value

    def test_create_tx(self):
        kwargs = {
            'itx': self.trans_itx,
            'from_address': self.wallet1.walletInfo.address,
            'wallet': self.wallet1.walletInfo,
            'nonce': 1,
            'token': self.wallet1.token,
        }
        res = self.rpc.create_tx(**kwargs)
        assert res.code == 0
        self.verify_tx(res)

    def test_get_tx(self):
        hash_list = ['123', '12334']
        res = self.rpc.get_tx(tx_hash=hash_list.__iter__())
        print(res)

    def test_get_block(self):
        height_list = [1, 2, 3]
        res = self.rpc.get_block(height=height_list.__iter__())
        for i in res:
            assert (i.code == 0)

    def test_send_tx(self):
        tx = protos.Transaction(**{
            'from': self.wallet1.walletInfo.address,
            'nonce': 1,
            'chain_id': self.chain_id,
        })
        kwargs = {
            'tx': tx,
            'wallet': self.wallet1.walletInfo,
            'token': self.wallet1.token,
        }
        res = self.rpc.send_tx(**kwargs)
        print(res)

    def test_get_chain_info(self):
        res = self.rpc.get_chain_info()
        assert (res.code == 0)

    def test_search(self):
        res = self.rpc.search(key='1', value='2')
        assert (res.code == 0)

    # def test_create_wallet(self):
    #     res = self.rpc.create_wallet(moniker='test', passphrase='abc123')
    #     print(res)
    #     assert (res.code == 0)

    def test_load_wallet(self):
        res = self.rpc.load_wallet(
            address=self.wallet1.walletInfo.address,
            passphrase='abc123',
        )
        print('**************\nThe response is :')
        print(res)
        assert (res.code == 0)

    # TODO: insufficient data
    def test_recover_wallet(self):
        res = self.rpc.recover_wallet(
            req=protos.RequestRecoverWallet(
                type=self.wallet_type,
                data=self.wallet1.walletInfo.sk,
                passphrase='abc123',
                moniker='alice',
            ),
        )
        print('**************\nThe response is :')
        print(res)
        assert (res.code == 0)

    def test_list_wallets(self):
        res = self.rpc.list_wallets()
        for i in res:
            assert (i.code == 0)
            print(i.address)

    def test_remove_wallet(self):
        res = self.rpc.remove_wallet(address=self.wallet1.walletInfo.address)
        assert (res.code == 0)

    def test_get_account_state(self):

        reqs = [
            protos.RequestGetAccountState(
                address=self.wallet1.walletInfo.address,
            ),
            protos.RequestGetAccountState(
                address=self.wallet1.walletInfo.address,
            ),
        ]
        res = self.rpc.get_account_state(req=reqs.__iter__())
        for i in res:
            assert (i.code == 0)
            print(i)

    def test_get_asset_state(self):

        reqs = [
            protos.RequestGetAssetState(
                address=self.wallet1.walletInfo.address,
            ),
            protos.RequestGetAssetState(
                address=self.wallet1.walletInfo.address,
            ),
        ]
        res = self.rpc.get_asset_state(req=reqs.__iter__())
        for i in res:
            assert (i.code == 0)
            print(i)

    def test_get_channel_state(self):

        reqs = [
            protos.RequestGetChannelState(
                address=self.wallet1.walletInfo.address,
            ),
            protos.RequestGetChannelState(
                address=self.wallet1.walletInfo.address,
            ),
        ]
        res = self.rpc.get_channel_state(req=reqs.__iter__())
        print('**************\nThe response is :')
        print(res.code)
        # assert (res.code == 0) # TODO: can't iterate

    def test_forge_state(self):
        res = self.rpc.get_forge_state(protos.RequestGetForgeState())
        assert (res.code == 0)

    def test_store_file(self):
        chunks = [b'123', b'abce']
        res = self.rpc.store_file(chunk=chunks.__iter__())
        assert (res.code == 0)

    def test_load_file(self):
        chunks = [b'123ddfdfsf', b'abcedddd']
        stored_files = self.rpc.store_file(chunk=chunks.__iter__())
        res = self.rpc.load_file(file_hash=stored_files.hash)
        print(res)


class Wallet:
    def __init__(self, token, wallet_info):
        self.token = token
        self.walletInfo = wallet_info
