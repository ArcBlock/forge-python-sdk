import unittest
from time import sleep

from forge_sdk import ForgeConn
from forge_sdk import rpc
from forge_sdk import utils
from forge_sdk.protos import protos
from test.lib import validate_response

forge = ForgeConn()


class WalletRpcTest(unittest.TestCase):

    def setUp(self):
        self.wallet_type = protos.WalletType(pk=0, hash=1, address=1)
        self.wallet1 = self.init_wallet('wallet1').wallet
        self.wallet2 = self.init_wallet('wallet2').wallet

    def init_wallet(self, moniker):
        res = forge.create_wallet(
            wallet_type=self.wallet_type,
            moniker=moniker,
            passphrase='abc123',
        )
        return res

    @validate_response
    def test_load_wallet(self):
        return forge.load_wallet(
            address=self.wallet1.address,
            passphrase='abc123',
        )

    @validate_response
    def test_recover_wallet(self):
        temp_wallet = forge.create_wallet(passphrase='abcd123')
        return forge.recover_wallet(
            data=temp_wallet.wallet.sk,
            passphrase='abcd123',
            moniker='bobalice',
        )

    @validate_response
    def test_remove_wallet(self):
        return forge.remove_wallet(address=self.wallet1.address)
