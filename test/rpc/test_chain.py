import unittest

from forge_sdk import ForgeConn
from forge_sdk import utils
from forge_sdk.protos import protos
from test.lib import validate_response

forge = ForgeConn()


class ChainRpcTest(unittest.TestCase):

    def setUp(self):
        self.wallet1 = self.init_wallet('wallet1')
        self.wallet2 = self.init_wallet('wallet2')
        self.trans_itx = utils.transfer_itx(
                to=self.wallet2.wallet.address,
                value=1,
        )

    def init_wallet(self, moniker):
        res = forge.create_wallet(
                moniker=moniker,
                passphrase='abc123',
        )
        return res

    def test_get_tx(self):
        tx_hash = self.test_send_tx().hash

        hash_list = [tx_hash]

        res = forge.get_tx(tx_hash=hash_list)
        for i in res:
            assert (i.code == 0)

    def test_get_block(self):
        height_list = [1, 2, 3]
        res = forge.get_block(height=height_list)
        for i in res:
            assert (i.code == 0)

    @validate_response
    def test_get_blocks(self):
        args = {"from": 2, "to": 5}
        range_filter = protos.RangeFilter(**args)
        return forge.get_blocks(height_filter=range_filter,
                                empty_excluded=True)

    @validate_response
    def test_send_tx(self):
        kwargs = {
            'itx': self.trans_itx,
            'wallet': self.wallet1.wallet,
        }
        tx = forge.build_tx(**kwargs)
        return forge.send_tx(tx=tx)

    @validate_response
    def test_get_chain_info(self):
        return forge.get_chain_info()

    @validate_response
    def test_forge_state(self):
        return forge.get_forge_state()
