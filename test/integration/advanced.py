import json
import random
import unittest
import uuid
from time import sleep

from forge_sdk import ForgeConn
from forge_sdk import utils
from forge_sdk.protos import protos
from test.lib import validate_response

SLEEP_SECS = 1
forge = ForgeConn('127.0.0.1:27210')
rpc = forge.rpc


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
        self.trans_tx = utils.build_transfer_itx(to=self.alice.wallet.address,
                                                 value=2)

    def init_wallet(self, moniker):
        res = rpc.create_wallet(
            wallet_type=self.wallet_type,
            moniker=moniker,
            passphrase='abc123',
        )
        return res

    def test_build_tx(self):
        nonce = random.randrange(1, 100)
        forge_built_tx = rpc.create_tx(self.trans_tx,
                                       self.alice.wallet.address,
                                       self.alice.wallet,
                                       self.alice.token,
                                       nonce=nonce)

        built_tx_1 = rpc.build_signed_tx(
            itx=self.trans_tx, wallet=self.alice.wallet,
            token=self.alice.token, nonce=nonce)

        built_tx_2 = rpc.build_signed_tx(itx=self.trans_tx,
                                         wallet=self.alice.wallet,
                                         nonce=nonce)

        assert forge_built_tx.tx.signature == built_tx_2.signature
        assert forge_built_tx.tx.signature == built_tx_1.signature

    @validate_response
    def test_send_transfer_tx(self):
        tx = rpc.build_signed_tx(itx=self.trans_tx, wallet=self.mike.wallet)
        res = rpc.send_tx(tx)
        return res

    def test_send_exchange_tx(self):
        res, asset_address = rpc.create_asset(type_url='test',
                                              asset=str(uuid.uuid1()),
                                              wallet=self.alice.wallet)
        assert utils.is_response_ok(res)
        sleep(5)
        asset = rpc.get_single_asset_state(asset_address)

        print('hash', res.hash)
        print('issuer', asset.issuer)
        print('alice', self.alice.wallet.address)

        assert (asset.issuer == self.alice.wallet.address)
        sender_info = protos.ExchangeInfo(assets=[asset_address])
        receiver_info = protos.ExchangeInfo(value=utils.int_to_biguint(10))
        exchange_tx = protos.ExchangeTx(sender=sender_info,
                                        receiver=receiver_info)
        tx = rpc.prepare_exchange(exchange_tx=exchange_tx,
                                  wallet=self.alice.wallet)
        tx = rpc.finalize_exchange(tx, self.mike.wallet)
        res = rpc.send_tx(tx)
        assert utils.is_response_ok(res)

    def test_asset_factory(self):
        # create asset_factory
        template = json.dumps({
            "row": "{{ row }}",
            "seat": "{{ seat }}",
            "room": "5C",
            "time": "11:00am 04/30/2019",
            "name": "Avengers: Endgame"
        })
        asset_attributes = protos.AssetAttributes(
            transferrable=True,
            ttl=3600,
        )

        factory = protos.AssetFactory(
            description='movie ticket factory' + str(uuid.uuid1()),
            limit=20,
            price=utils.value_to_biguint(5),
            template=template,
            allowed_spec_args=['row', 'seat'],
            asset_name='TestTicket',
            attributes=asset_attributes
        )

        res, factory_address = rpc.create_asset_factory(moniker='test_factory',
                                                        asset=factory,
                                                        wallet=self.alice.wallet)
        assert utils.is_response_ok(res)

        # send acquireAssetTx
        sleep(5)
        factory_state = rpc.get_single_asset_state(factory_address)
        assert factory_state.issuer == self.alice.wallet.address
        mike_original_balance = rpc.get_account_balance(
            self.mike.wallet.address)

        spec_datas = [{'row': '1', 'seat': str(uuid.uuid1())}, {
            'row': '2', 'seat': str(uuid.uuid4())}]
        res, tickets = rpc.acquire_asset(to=factory_address,
                                         spec_datas=spec_datas,
                                         type_url='fg:x:test_ticket',
                                         proto_lib=protos,
                                         wallet=self.mike.wallet)
        print('tickets', tickets)
        assert res.code == 0
        assert len(tickets) == len(spec_datas)
        sleep(6)
        for ticket in tickets:
            res = rpc.get_single_asset_state(ticket)
            assert res
            assert res.issuer == self.alice.wallet.address
            assert res.owner == self.mike.wallet.address

        mike_new_balance = rpc.get_account_balance(self.mike.wallet.address)
        assert (mike_original_balance -
                mike_new_balance) == utils.to_unit(5) * 2
