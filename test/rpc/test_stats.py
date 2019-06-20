import unittest
from datetime import datetime as dt
from datetime import timedelta
from time import sleep
from uuid import uuid4

from forge_sdk import ForgeConn
from forge_sdk.protos import protos
from test.lib import validate_response
forge = ForgeConn()
rpc = forge.rpc


def verify(res):
    if res.code != 0:
        raise ValueError(f'rpc call fails with error {res}')


class StatisticsTest(unittest.TestCase):

    def setUp(self):
        self.yesterday = str((dt.now() - timedelta(2)).date())
        self.test_account = rpc.create_wallet(moniker='alice',
                                              passphrase='abc123')

        res, self.asset_address = rpc.create_asset(type_url='test',
                                                   asset=str(uuid4()),
                                                   wallet=self.test_account.wallet,
                                                   chain_id=forge.config.chain_id)
        assert (res.code == 0)
        assert self.asset_address

    @validate_response
    def test_get_forge_stats(self):
        day_info = protos.ByDay(start_date=self.yesterday,
                                end_date=self.yesterday)
        return rpc.get_forge_stats(day_info=day_info)

    @validate_response
    def test_list_transactions(self):
        return rpc.list_transactions()

    @validate_response
    def test_get_stakes(self):
        return rpc.list_stakes()

    @validate_response
    def test_get_top_accounts(self):
        res = rpc.list_top_accounts()
        assert res.accounts
        return res

    @validate_response
    def test_list_asset_transactions(self):
        sleep(5)
        return rpc.list_asset_transactions(self.asset_address)

    @validate_response
    def test_list_blocks(self):
        return rpc.list_blocks()

    @validate_response
    def test_list_assets(self):
        sleep(5)
        res = rpc.list_assets(owner_address=self.test_account.wallet.address)
        assert (res.assets[0].address == self.asset_address)
        return res

    @validate_response
    def test_get_health_status(self):
        return rpc.get_health_status()
