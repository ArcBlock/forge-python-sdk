import unittest
from datetime import datetime as dt
from datetime import timedelta
from time import sleep

from google.protobuf.any_pb2 import Any

from forge_sdk import did
from forge_sdk import rpc
from forge_sdk.protos import protos


def verify(res):
    if res.code != 0:
        raise ValueError(f'rpc call fails with error {res}')


class StatisticsTest(unittest.TestCase):
    def setUp(self):
        self.yesterday = str((dt.now() - timedelta(2)).date())
        self.test_account = rpc.create_wallet(moniker='alice',
                                              passphrase='abc123')

        res, self.asset_address = rpc.create_asset('test', 'test',
                                                   self.test_account.wallet,
                                                   self.test_account.token)
        verify(res)

    def test_get_forge_stats(self):
        day_info = protos.ByDay(start_date=self.yesterday,
                                end_date=self.yesterday)
        res = rpc.get_forge_stats(day_info=day_info)
        verify(res)

    def test_list_transactions(self):
        res = rpc.list_transactions()
        verify(res)

    def test_get_stakes(self):
        res = rpc.list_stakes()
        verify(res)

    def test_get_top_accounts(self):
        res = rpc.list_top_accounts()
        verify(res)
        assert res.accounts

    def test_list_asset_transactions(self):
        sleep(5)
        res = rpc.list_asset_transactions(self.asset_address)
        verify(res)

    def test_list_blocks(self):
        res = rpc.list_blocks()
        verify(res)

    def test_list_assets(self):
        sleep(5)
        res = rpc.list_assets(owner_address=self.test_account.wallet.address)
        verify(res)
        assert (res.assets[0].address == self.asset_address)

    def test_get_health_status(self):
        res = rpc.get_health_status()
        verify(res)
