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
                to=self.wallet2.address,
                value=1,
        )

    def init_wallet(self, moniker):
        res = forge.create_wallet(moniker=moniker)
        return res

    def test_get_tx(self):
        tx_hash = self.test_send_tx().hash

        res = forge.get_tx(tx_hash=[tx_hash])
        for i in res:
            assert (i.code == 0)

        res = forge.get_tx(tx_hash=tx_hash)
        for i in res:
            assert (i.code == 0)

    def test_get_block(self):
        res = forge.get_block(height=[1, 2, 3])
        for i in res:
            assert (i.code == 0)

        res = forge.get_block(height=2)
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
            'wallet': self.wallet1,
        }
        tx = forge.build_tx(**kwargs)
        return forge.send_tx(tx=tx)

    @validate_response
    def test_get_chain_info(self):
        return forge.get_chain_info()

    @validate_response
    def test_forge_state(self):
        return forge.get_forge_state()
