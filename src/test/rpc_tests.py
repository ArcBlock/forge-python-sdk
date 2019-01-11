import unittest

from rpc import ForgeRpc


class RpcTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(RpcTest, self).__init__(*args, **kwargs)
        self.rpc = ForgeRpc("127.0.0.1:28210")
        self.wallet1 = None
        self.wallet2 = None

    def test_get_chain_info(self):
        res = self.rpc.get_chain_info()
        assert (res.code == 0)

    def test_search(self):
        res = self.rpc.search(key='1', value='2')
        assert (res.code == 0)

    def test_create_wallet(self):
        res = self.rpc.create_wallet(passphrase='abc123')
        print(res)
        assert (res.code == 0)
