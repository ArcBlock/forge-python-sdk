import unittest
from time import sleep

from google.protobuf.any_pb2 import Any

from forge import ForgeRpc
from forge import protos
from forge import utils
from forge.protos import BigUint
from forge.protos import TransferTx

FORGE_TEST_SOCKET = '127.0.0.1:27210'
SLEEP_SECS = 5


class RpcTest(unittest.TestCase):

    def setUp(self):
        self.rpc = ForgeRpc(socket=FORGE_TEST_SOCKET)
        self.wallet_type = protos.WalletType(pk=0, hash=1, address=1)
        self.wallet1 = self.init_wallet('wallet1')
        self.wallet2 = self.init_wallet('wallet2')
        self.trans_itx = Any(
            type_url='fg:t:transfer',
            value=TransferTx(
                to=self.wallet2.wallet.address,
                value=BigUint(value=b'11'),
            ).SerializeToString(),
        )

    def init_wallet(self, moniker):
        res = self.rpc.create_wallet(
            wallet_type=self.wallet_type,
            moniker=moniker,
            passphrase='abc123',
        )
        return res

    def test_create_tx(self):
        kwargs = {
            'itx': self.trans_itx,
            'from_address': self.wallet1.wallet.address,
            'wallet': self.wallet1.wallet,
            'nonce': 2,
            'token': self.wallet1.token,
        }
        res = self.rpc.create_tx(**kwargs)
        assert res.code == 0

    def test_get_tx(self):
        tx_hash = self.test_send_tx().hash
        sleep(SLEEP_SECS)

        hash_list = [tx_hash]
        print("hash to get", tx_hash)
        sleep(1)

        res = self.rpc.get_tx(tx_hash=hash_list)
        for i in res:
            print(i)
            assert (i.code == 0)

    def test_get_block(self):
        height_list = [1, 2, 3]
        res = self.rpc.get_block(height=height_list)
        for i in res:
            assert (i.code == 0)
            print(i)

    def test_send_tx(self):
        sleep(SLEEP_SECS)
        kwargs = {
            'itx': self.trans_itx,
            'from_address': self.wallet1.wallet.address,
            'wallet': self.wallet1.wallet,
            'nonce': 2,
            'token': self.wallet1.token,
        }
        tx = self.rpc.create_tx(**kwargs).tx
        res = self.rpc.send_tx(tx=tx, token=self.wallet1.token)
        assert (res.code == 0)

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
            address=self.wallet1.wallet.address,
            passphrase='abc123',
        )
        assert (res.code == 0)

    def test_recover_wallet(self):
        temp_wallet = self.rpc.create_wallet(passphrase='abcd123')
        res = self.rpc.recover_wallet(
            req=protos.RequestRecoverWallet(
                type=self.wallet_type,
                data=temp_wallet.wallet.sk,
                passphrase='abcd123',
                moniker='bobalice',
            ),
        )
        assert (res.code == 0)

    def test_list_wallet(self):
        res = self.rpc.list_wallet()
        for i in res:
            assert (i.code == 0)

    def test_remove_wallet(self):
        res = self.rpc.remove_wallet(address=self.wallet1.wallet.address)
        assert (res.code == 0)

    def test_get_account_state(self):
        sleep(SLEEP_SECS)

        def verify_result(req):
            res = self.rpc.get_account_state(req)
            for i in res:
                print(i)
                assert (i.code == 0)
                assert (i.state.moniker == 'wallet1')

        wallet1_addr = self.wallet1.wallet.address

        reqs_list = [
            protos.RequestGetAccountState(
                address=wallet1_addr,
            ),
            protos.RequestGetAccountState(
                address=wallet1_addr,
            ),
        ]
        dict_list = [{'address': wallet1_addr}, {'address': wallet1_addr}]
        single_req = protos.RequestGetAccountState(
            address=wallet1_addr,
        )
        single_dict = [{'address': wallet1_addr}]

        verify_result(reqs_list)
        verify_result(dict_list)
        verify_result(single_req)
        verify_result(single_dict)

    def test_get_asset_state(self):

        reqs = [
            protos.RequestGetAssetState(
                address=self.wallet1.wallet.address,
            ),
            protos.RequestGetAssetState(
                address=self.wallet1.wallet.address,
            ),
        ]
        res = self.rpc.get_asset_state(req=reqs.__iter__())
        for i in res:
            assert (i.code == 0)

    def test_forge_state(self):
        res = self.rpc.get_forge_state(req=protos.RequestGetForgeState())
        assert (res.code == 0)

    def test_send_itx(self):
        trans_itx = TransferTx(
            to=self.wallet2.wallet.address,
            value=BigUint(value=b'11'),
        )
        res = self.rpc.send_itx(
            'fg:t:transfer', trans_itx,
            self.wallet1.wallet, self.wallet1.token,
        )
        assert (res.code == 0)
        print(res)

    def test_send_exchange_itx(self):
        exchange_itx = protos.ExchangeTx(
            sender=protos.ExchangeInfo(value=protos.BigUint(value=bytes(3))),
            receiver=protos.ExchangeInfo(value=protos.BigUint(value=bytes(3))),
        )
        sender_signed = self.rpc.create_tx(
            itx=utils.encode_to_any('fg:t:exchange', exchange_itx),
            from_address=self.wallet1.wallet.address,
            wallet=self.wallet1.wallet,
            token=self.wallet1.token,
        ).tx
        sleep(5)
        receiver_signed = self.rpc.multisig(
            tx=sender_signed, wallet=self.wallet2.wallet,
            token=self.wallet2.token,
        ).tx
        res = self.rpc.send_tx(
            tx=receiver_signed,
            wallet=self.wallet2.wallet,
            token=self.wallet2.token,
        )
        assert(res.code == 0)
        print(res)


if __name__ == '__main__':
    unittest.main()
