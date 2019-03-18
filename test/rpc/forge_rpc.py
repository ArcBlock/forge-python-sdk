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


def verify_tx_response(response):
    if response.code == 0 and response.hash is not None:
        return True
    else:
        return False


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
        res = self.rpc.get_account_state(single_req)
        for i in res:
            print(type(i.state.pk))

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
            sender=protos.ExchangeInfo(
                value=protos.BigUint(value=bytes(3)),
            ),
            receiver=protos.ExchangeInfo(
                value=protos.BigUint(value=bytes(3)),
            ),
        )
        sender_signed = self.rpc.create_tx(
            itx=utils.encode_to_any('fg:t:exchange', exchange_itx),
            from_address=self.wallet1.wallet.address,
            wallet=self.wallet1.wallet,
            token=self.wallet1.token,
        ).tx
        print(sender_signed)
        sleep(5)
        receiver_signed = self.rpc.multisig(
            tx=sender_signed, wallet=self.wallet2.wallet,
            token=self.wallet2.token,
        ).tx
        print(receiver_signed)
        res = self.rpc.send_tx(
            tx=receiver_signed,
            wallet=self.wallet2.wallet,
            token=self.wallet2.token,
        )
        if (res.code != 0):
            print(res)
        assert (res.code == 0)
        print(res)

    def test_consume_asset(self):
        sleep(5)
        asset_create_itx = protos.CreateAssetTx(
            moniker='TestAsset',
            data=Any(
                type_url='test',
                value=b'hello',
            ),
        )
        asset_address = self.rpc.get_asset_address(
            self.wallet1.wallet.address,
            asset_create_itx,
            self.wallet1.wallet.type, ).asset_address

        res = self.rpc.send_itx(
            'fg:t:create_asset', asset_create_itx,
            self.wallet1.wallet,
            self.wallet1.token,
        )
        assert (verify_tx_response(res))
        print("Asset created.")
        sleep(5)

        exchange_itx = protos.ExchangeTx(
            sender=protos.ExchangeInfo(assets=[asset_address]),
            receiver=protos.ExchangeInfo(value=BigUint(value=bytes(10))),
        )

        sender_exchange_signed = self.rpc.create_tx(
            itx=utils.encode_to_any(
                'fg:t:exchange',
                exchange_itx,
            ),
            from_address=self.wallet1.wallet.address,
            wallet=self.wallet1.wallet,
            token=self.wallet1.token,
        )

        assert (sender_exchange_signed.tx is not None)

        receiver_exchange_signed = self.rpc.multisig(
            tx=sender_exchange_signed.tx,
            wallet=self.wallet2.wallet,
            token=self.wallet2.token,
        )

        assert (receiver_exchange_signed.tx is not None)

        res = self.rpc.send_tx(receiver_exchange_signed.tx)

        assert (verify_tx_response(res))

        print("Asset exchanged.")

        consume_asset_itx = protos.ConsumeAssetTx(
            issuer=self.wallet1.wallet.address,
        )

        issuer_signed = self.rpc.create_tx(
            from_address=self.wallet1.wallet.address,
            wallet=self.wallet1.wallet,
            token=self.wallet1.token,
            itx=utils.encode_to_any(
                'fg:t:consume_asset',
                consume_asset_itx,
            ),
        )
        if issuer_signed.code != 0:
            print(res)
        assert (issuer_signed.code == 0)

        res_both_sig = self.rpc.multisig(
            tx=issuer_signed.tx,
            wallet=self.wallet2.wallet,
            token=self.wallet2.token,
            data=Any(
                type_url='fg:x:address',
                value=asset_address.encode(),
            ),
        )
        assert (res_both_sig.code == 0)

        res = self.rpc.send_tx(res_both_sig.tx)
        assert (verify_tx_response(res))

        sleep(5)

        # check asset state
        asset = self.rpc.get_single_asset_state(asset_address)
        assert (not asset.transferrable)
        assert (asset.readonly)


if __name__ == '__main__':
    unittest.main()
