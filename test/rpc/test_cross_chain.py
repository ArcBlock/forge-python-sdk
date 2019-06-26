import base64
import logging
import os
import unittest
import uuid
from datetime import datetime
from datetime import timedelta

from dotenv import find_dotenv
from dotenv import load_dotenv
from google.protobuf.timestamp_pb2 import Timestamp

from forge_sdk import did
from forge_sdk import ForgeConn
from forge_sdk import utils
from forge_sdk.protos import protos
from test.lib import validate_response

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

load_dotenv(find_dotenv())

abt_chain = ForgeConn('127.0.0.1:27210')
app_chain = ForgeConn('127.0.0.1:28210')

deposit_locktime = Timestamp(
    seconds=int((datetime.utcnow() + timedelta(days=2)).timestamp()))
deposit_cap = 4000

anchor = protos.WalletInfo(sk=base64.b16decode(os.environ.get('ANCHOR_SK')),
                           pk=base64.b16decode(os.environ.get('ANCHOR_PK')),
                           address=os.environ.get('ANCHOR_ADDR'))
custodian = protos.WalletInfo(
    sk=b'\xe9\x84"\x81\x9fT\x8f\x19\xf3\xa9\xe2\xfb\xde\x17_\xf9k\xa6\xc9'
       b'\xf4\xd9@ \xe3\x04U\x00\x186\x95Pn\x8a\xd35s\xa4\x1beMH\xc4\xa8\x00'
       b'\xe4\xc9\'#\\2\xd3\xe1\xf65\xcbLLw\xa7\xc6\r\x80ZA',
    pk=b"\x8a\xd35s\xa4\x1beMH\xc4\xa8\x00\xe4\xc9'#\\2\xd3\xe1\xf65\xcbLLw"
       b"\xa7\xc6\r\x80ZA",
    address="z1SQSfb2hPHkkKwqgCXvd4ppVGpihXo7zdV")

alice1 = protos.WalletInfo(
    sk=b'\xc6\x95\x9b\xbb6P\xa7\x19\xc8\x04\xfe~\x8f#\xf9\r\x10U\xd1^\xba\x14\x93@5X\x00\xf8\xe2o\xaa\xfe\xcaaI\xbb.\xc2\xda\x0c\xe0\xe8\x84\t\xb7\xae,\xb0\xc1\xe6@\xd0\x05\xe5\x88z\xa5\xa7\xed\x04P\xea2\x98',
    pk=b'\xcaaI\xbb.\xc2\xda\x0c\xe0\xe8\x84\t\xb7\xae,\xb0\xc1\xe6@\xd0\x05\xe5\x88z\xa5\xa7\xed\x04P\xea2\x98',
    address="z1TjR2C15hTraD7WcMhix2pSRBpnFLPq1K5"
)
bob1 = protos.WalletInfo(
    sk=b"7N]\xc0\x91\xf9\xe0\xbd\xa0nI\xe2T\xfc\x99I\xabR\xaf:\x05\xf9\x06\x93c\x12y\xad1\x7fi\x0f\xd1\x86(Vv\xa3\xab?\x14\x8fm\xa6\xd9)\x97T\x85\xe5z\xe2\xe1\xe6)\x96c\x9bm\x13'|\xc1<",
    pk=b"\xd1\x86(Vv\xa3\xab?\x14\x8fm\xa6\xd9)\x97T\x85\xe5z\xe2\xe1\xe6)\x96c\x9bm\x13'|\xc1<",
    address="z1hgjwXfjj9uzi7JMFadUtTgXJ8EgXFHnPc"
)


@validate_response
def init_scenairo():
    declare_itx = protos.DeclareTx(moniker='anchor1')
    tx = utils.build_unsigned_tx(
        itx=utils.encode_to_any('fg:t:declare', declare_itx),
        chain_id=abt_chain.config.chain_id,
        wallet=anchor)
    sig = utils.sign_tx(wallet=anchor, tx=tx, round=1)
    tx.signature = sig

    abt_chain.rpc.send_tx(tx)

    app_chain.rpc.declare(moniker='custodian', wallet=custodian)
    abt_chain.rpc.declare(moniker='custodian', wallet=custodian)
    app_chain.rpc.declare(moniker='alice', wallet=alice1)
    abt_chain.rpc.declare(moniker='alice', wallet=alice1)
    app_chain.rpc.declare(moniker='bobby', wallet=bob1)
    abt_chain.rpc.declare(moniker='bobby', wallet=bob1)

    res = abt_chain.rpc.stake_for_node(to=anchor.address,
                                       value=utils.to_unit(deposit_cap),
                                       wallet=custodian)
    return res


if not abt_chain.rpc.get_single_account_state(custodian.address):
    logging.info("Initiating users....")
init_scenairo()


class ForgeCrossChainTest(unittest.TestCase):

    def test(self):
        res2, tether_address, deposit_tx = self.deposit_tether()
        logging.info(
            f'alice {alice1.address} has depoisted. hash: {res2.hash}')
        logging.info(f'tether address is : {tether_address}')

        res3, exchange_tether_tx, tether_address = self.exchange_tether(
            tether_address, deposit_tx)
        logging.info(
            f'alice {alice1.address} and bob1 {bob1.address} '
            f'has depoisted. hash: {res3.hash}')

        res4 = self.withdraw_tether(exchange_tether_tx, tether_address)
        logging.info(
            f'bob {bob1.address} has send the withdraw request. '
            f'hash: '
            f'{res4.hash}')

    def deposit_tether(self):
        deposit_params = {
            'value': utils.to_unit(3),
            'commission': utils.to_unit(2),
            'charge': utils.to_unit(1),
            'target': app_chain.config.chain_id,
            'withdrawer': bob1.address,
            'locktime': deposit_locktime,
        }
        alice_signed_tx = abt_chain.rpc.prepare_deposit_tether_tx(
            alice1,
            **deposit_params)
        custodian_signed_tx = abt_chain.rpc.finalize_deposit_tether_tx(
            alice_signed_tx, custodian)
        res = abt_chain.rpc.send_tx(custodian_signed_tx)
        tether_address = did.get_tether_address(res.hash)

        return res, tether_address, custodian_signed_tx

    def exchange_tether(self, tether_address, deposit_tether_tx):
        res, asset_addr = app_chain.rpc.create_asset(type_url='test',
                                                     asset=str(uuid.uuid4()),
                                                     wallet=bob1)

        bob1_signed_tx = app_chain.rpc.prepare_exchange_tether(
            wallet=bob1,
            sender=protos.ExchangeInfo(assets=[asset_addr]),
            receiver=protos.TetherExchangeInfo(
                deposit=deposit_tether_tx
            ),
            expired_at=deposit_locktime)
        final_exchange_tx = app_chain.rpc.finalize_exchange_tether_tx(
            tx=bob1_signed_tx,
            wallet=alice1)

        res = app_chain.rpc.send_tx(final_exchange_tx)

        return res, final_exchange_tx, tether_address

    @validate_response
    def withdraw_tether(self, exchange_tether_tx, tether_address):
        itx = utils.parse_to_proto(
            exchange_tether_tx.itx.value,
            protos.ExchangeTetherTx)
        params = {
            'from': getattr(exchange_tether_tx, "from"),
            'nonce': exchange_tether_tx.nonce,
            'chain_id': exchange_tether_tx.chain_id,
            'pk': exchange_tether_tx.pk,
            'sender': itx.sender,
            'receiver': protos.TetherTradeInfo(
                value=itx.receiver.value,
                assets=itx.receiver.assets,
                tether=tether_address
            ),
            'expired_at': itx.expired_at,
            'signatures': exchange_tether_tx.signatures,
            'signature': exchange_tether_tx.signature,
            'data': itx.data,
        }
        assert exchange_tether_tx.pk == bob1.pk
        withdraw_tether_tx = protos.WithdrawTetherTx(**params)

        tx = abt_chain.rpc.build_signed_tx(itx=withdraw_tether_tx,
                                           wallet=bob1,
                                           type_url='fg:t:withdraw_tether')

        res = abt_chain.rpc.send_tx(tx)
        return res

    def test_approve_tether(self):
        return

    def test_revoke_tether(self):
        return
