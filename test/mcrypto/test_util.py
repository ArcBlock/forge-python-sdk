import unittest

from forge_sdk import protos
from forge_sdk import utils


class DIDUtilTest(unittest.TestCase):

    def test_get_asset_address(self):
        itx = protos.CreateAssetTx()
        asset_address = utils.to_asset_address(itx)
        assert asset_address == "zjdtErp27MYs7BuaoQWBF6DSg6jU4DrE1VQ2"

    def test_get_stake_address(self):
        res = utils.to_stake_address("hello", "world")
        assert res == "zrjtQieLzC4nr33wDNaMyohiLWGoKoEtGXhH"

