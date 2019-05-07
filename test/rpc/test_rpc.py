import unittest
from datetime import datetime
from time import sleep

from google.protobuf.any_pb2 import Any

from forge_sdk import did
from forge_sdk import rpc
from forge_sdk import utils
from forge_sdk.protos import protos
from forge_sdk.protos.protos import BigUint
from forge_sdk.protos.protos import TransferTx

SLEEP_SECS = 1


def verify_tx_response(response):
    if response.code == 0 and response.hash is not None:
        return True
    else:
        return False


class RpcTest(unittest.TestCase):

    def setUp(self):
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
        res = rpc.create_wallet(
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
        res = rpc.create_tx(**kwargs)
        assert res.code == 0

    def test_get_tx(self):
        tx_hash = self.test_send_tx().hash

        hash_list = [tx_hash]
        print("hash to get", tx_hash)

        res = rpc.get_tx(tx_hash=hash_list)
        for i in res:
            print(i)
            assert (i.code == 0)

    def test_get_block(self):
        height_list = [1, 2, 3]
        res = rpc.get_block(height=height_list)
        for i in res:
            assert (i.code == 0)
            print(i)

    def test_send_tx(self):
        kwargs = {
            'itx': self.trans_itx,
            'from_address': self.wallet1.wallet.address,
            'wallet': self.wallet1.wallet,
            'nonce': 2,
            'token': self.wallet1.token,
        }
        tx = rpc.create_tx(**kwargs).tx
        res = rpc.send_tx(tx=tx, token=self.wallet1.token)
        assert (res.code == 0)
        return res

    def test_get_chain_info(self):
        res = rpc.get_chain_info()
        assert (res.code == 0)

    def test_search(self):
        res = rpc.search(key='1', value='2')
        assert (res.code == 0)

    # def test_create_wallet(self):
    #     res = rpc.create_wallet(moniker='test', passphrase='abc123')
    #     print(res)
    #     assert (res.code == 0)

    def test_load_wallet(self):
        res = rpc.load_wallet(
            address=self.wallet1.wallet.address,
            passphrase='abc123',
        )
        assert (res.code == 0)

    def test_recover_wallet(self):
        temp_wallet = rpc.create_wallet(passphrase='abcd123')
        res = rpc.recover_wallet(
            wallet_type=self.wallet_type,
            data=temp_wallet.wallet.sk,
            passphrase='abcd123',
            moniker='bobalice',
        )
        assert (res.code == 0)

    def test_list_wallet(self):
        res = rpc.list_wallet()
        for i in res:
            assert (i.code == 0)

    def test_remove_wallet(self):
        res = rpc.remove_wallet(address=self.wallet1.wallet.address)
        assert (res.code == 0)

    def test_get_account_state(self):
        sleep(5)

        def verify_result(req):
            res = rpc.get_account_state(req)
            for i in res:
                print(i)
                assert (i.code == 0)
                assert (i.state.moniker == 'wallet1')

        wallet1_addr = self.wallet1.wallet.address

        dict_list = [{'address': wallet1_addr}, {'address': wallet1_addr}]
        single_dict = [{'address': wallet1_addr}]

        verify_result(dict_list)
        verify_result(single_dict)
        res = rpc.get_account_state(dict_list)
        for i in res:
            print(type(i.state.pk))

    def test_forge_state(self):
        res = rpc.get_forge_state()
        assert (res.code == 0)

    def test_send_itx(self):
        trans_itx = TransferTx(
            to=self.wallet2.wallet.address,
            value=BigUint(value=b'11'),
        )
        res = rpc.send_itx(
            'fg:t:transfer', trans_itx,
            self.wallet1.wallet, self.wallet1.token,
        )
        assert (res.code == 0)
        print(res)

    def test_poke_tx(self):

        pokeTx = protos.PokeTx(
            date=str(datetime.utcnow().date()),
            address='zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz',
        )
        res = rpc.send_itx(
            type_url='fg:t:poke',
            tx=pokeTx,
            wallet=self.wallet1.wallet,
            token=self.wallet1.token,
            nonce=0
        )
        assert (res.code == 0)

    def test_consume_asset(self):
        res, asset_address = rpc.create_asset(
            'fg:t:create_asset', b'hello',
            self.wallet1.wallet,
            self.wallet1.token,
        )
        assert (verify_tx_response(res))
        print("Asset created.")

        exchange_itx = protos.ExchangeTx(
            sender=protos.ExchangeInfo(assets=[asset_address]),
            receiver=protos.ExchangeInfo(value=BigUint(value=bytes(10))),
        )

        sender_exchange_signed = rpc.create_tx(
            itx=utils.encode_to_any(
                'fg:t:exchange',
                exchange_itx,
            ),
            from_address=self.wallet1.wallet.address,
            wallet=self.wallet1.wallet,
            token=self.wallet1.token,
        )

        assert (sender_exchange_signed.tx is not None)

        receiver_exchange_signed = rpc.multisig(
            tx=sender_exchange_signed.tx,
            wallet=self.wallet2.wallet,
            token=self.wallet2.token,
        )

        assert (receiver_exchange_signed is not None)

        res = rpc.send_tx(receiver_exchange_signed)

        assert (verify_tx_response(res))

        print("Asset exchanged.")

        consume_asset_itx = protos.ConsumeAssetTx(
            issuer=self.wallet1.wallet.address,
        )

        issuer_signed = rpc.create_tx(
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

        res_both_sig = rpc.multisig(
            tx=issuer_signed.tx,
            wallet=self.wallet2.wallet,
            token=self.wallet2.token,
            data=Any(
                type_url='fg:x:address',
                value=asset_address.encode(),
            ),
        )
        res = rpc.send_tx(res_both_sig)
        assert (verify_tx_response(res))

        sleep(5)

        # check asset state
        asset = rpc.get_single_asset_state(asset_address)
        assert (not asset.transferrable)
        assert (asset.readonly)
