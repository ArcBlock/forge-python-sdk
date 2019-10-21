import unittest
from datetime import datetime as dt
from datetime import timedelta
from time import sleep
from uuid import uuid4

from forge_sdk import ForgeConn
from forge_sdk import protos, utils
from test.lib import validate_response

forge = ForgeConn()


def verify(res):
    if res.code != 0:
        raise ValueError(f'rpc call fails with error {res}')


class StatisticsforgeTest(unittest.TestCase):

    def setUp(self):
        self.yesterday = str((dt.now() - timedelta(2)).date())

    @validate_response
    def test_get_forge_stats(self):
        day_info = protos.ByDay(start_date=self.yesterday,
                                end_date=self.yesterday)
        return forge.get_forge_stats(day_info=day_info)

    @validate_response
    def test_list_transactions(self):
        return forge.list_transactions()

    @validate_response
    def test_get_stakes(self):
        return forge.list_stakes()

    @validate_response
    def test_get_top_accounts(self):
        res = forge.list_top_accounts()
        assert res.accounts
        return res

    @validate_response
    def test_list_asset_transactions(self):
        self._create_asset()
        sleep(5)
        return forge.list_asset_transactions(self.asset_address)

    @validate_response
    def test_list_blocks(self):
        return forge.list_blocks()

    @validate_response
    def test_list_assets(self):
        self._create_asset()
        sleep(5)
        res = forge.list_assets(owner_address=self.wallet.address)
        assert (res.assets[0].address == self.asset_address)
        return res

    @validate_response
    def test_get_health_status(self):
        return forge.get_health_status()

    def _create_asset(self):
        self.wallet = forge.create_wallet(moniker='alice',
                                          passphrase='abc123').wallet
        res, self.asset_address = forge.create_asset(
                data=utils.to_any(str(uuid4()),
                                  'test_url'),
                wallet=self.wallet,
                commit=True)
        assert (res.code == 0)
        assert self.asset_address
