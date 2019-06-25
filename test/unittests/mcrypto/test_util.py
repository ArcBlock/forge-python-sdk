import unittest

from forge_sdk import did
from forge_sdk import protos


class DIDUtilTest(unittest.TestCase):

    def test_get_asset_address(self):
        itx = protos.CreateAssetTx()
        asset_address = did.get_asset_address(itx)
        assert asset_address == "zjdtErp27MYs7BuaoQWBF6DSg6jU4DrE1VQ2"

    def test_get_stake_address(self):
        res = did.get_stake_address("hello", "world")
        assert res == "zrjtQieLzC4nr33wDNaMyohiLWGoKoEtGXhH"

    def test_get_tether_address(self):
        res = did.get_tether_address(
            "E8C984E80EB10A1A9F531A061DB8C03B5BFB532E8B371A0F3BD8866E3E315ABA")
        assert res == "z2MCBKjy5m6LGwZuJ7o7975EnYywmkKPAGBFb"
