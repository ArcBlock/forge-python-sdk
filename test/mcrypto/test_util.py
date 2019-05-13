import unittest

from google.protobuf.any_pb2 import Any

from forge_sdk import did
from forge_sdk import protos


class DIDUtilTest(unittest.TestCase):

    def test_get_asset_address(self):
        itx = protos.CreateAssetTx()
        asset_address = did.get_asset_address(itx)
        assert asset_address == "zjdtErp27MYs7BuaoQWBF6DSg6jU4DrE1VQ2"
