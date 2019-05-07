import unittest
from time import sleep

from google.protobuf.any_pb2 import Any

from forge_sdk import rpc
from forge_sdk import utils
from forge_sdk.protos import protos
from forge_sdk.protos.protos import TransferTx

SLEEP_SECS = 1


def verify_tx_response(response):
    if response.code == 0 and response.hash is not None:
        return True
    else:
        return False


class HelperRPCTest(unittest.TestCase):

    def setUp(self):
        self.wallet_type = protos.WalletType(pk=0, hash=1, address=1)
        self.alice = self.init_wallet('alice')
        self.mike = self.init_wallet('mike')
        self.trans_tx = Any(
            type_url='fg:t:transfer',
            value=TransferTx(
                to=self.alice.wallet.address,
                value=utils.int_to_biguint(2),
            ).SerializeToString(),
        )

    def init_wallet(self, moniker):
        res = rpc.create_wallet(
            wallet_type=self.wallet_type,
            moniker=moniker,
            passphrase='abc123',
        )
        return res

    def test_build_tx(self):

        forge_built_tx = rpc.create_tx(self.trans_tx, self.alice.wallet.address,
                                       self.alice.wallet, self.alice.token)

        built_tx_1 = rpc.build_tx(
            self.trans_tx, self.alice.wallet, self.alice.token)

        built_tx_2 = rpc.build_tx(self.trans_tx, self.alice.wallet)

        assert forge_built_tx.tx.signature == built_tx_2.signature
        assert forge_built_tx.tx.signature == built_tx_1.signature

    def test_send_poke_tx(self):
        res = rpc.poke(self.alice.wallet)
        sleep(5)
        assert rpc.is_tx_ok(res.hash)

    def test_send_transfer_tx(self):
        transfer_tx = protos.TransferTx(to=self.mike.wallet.address,
                                        value=utils.int_to_biguint(10))
        res = rpc.transfer(transfer_tx, self.alice.wallet)
        sleep(5)
        assert rpc.is_tx_ok(res.hash)

    def test_send_exchange_tx(self):
        res, asset_address = rpc.create_asset('test',
                                              'asset',
                                              self.alice.wallet)
        sleep(5)
        sender_info = protos.ExchangeInfo(assets=[asset_address])
        receiver_info = protos.ExchangeInfo(value=utils.int_to_biguint(10))
        exchange_tx = protos.ExchangeTx(sender=sender_info,
                                        receiver=receiver_info)
        tx = rpc.prepare_exchange(exchange_tx, self.alice.wallet)
        tx = rpc.finalize_exchange(tx, self.mike.wallet)
        res = rpc.send_tx(tx)
        assert res.hash
