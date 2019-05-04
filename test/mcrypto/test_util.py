import unittest

from google.protobuf.any_pb2 import Any

from forge_sdk import did
from forge_sdk import protos


class DIDUtilTest(unittest.TestCase):

    def test_get_asset_address(self):
        account = "z1cYzB4LHUKs7i6ZYt7BHRVm4eofnHeutoL"
        itx = protos.CreateAssetTx(data=Any(value=b'123'))
        asset_address = did.get_asset_address(account, itx)
        assert (asset_address == "zjdjoBZ8TCyQhbY2q3GZfJFAcWWBbF8ZXrts")
