import unittest
from time import sleep

from forge_sdk import ForgeConn
from forge_sdk import rpc
from forge_sdk import utils
from forge_sdk.protos import protos
from test.lib import validate_response

forge = ForgeConn()
rpc = forge.rpc


class RpcTest(unittest.TestCase):

    def setUp(self):
        self.wallet_type = protos.WalletType(pk=0, hash=1, address=1)
        self.wallet1 = self.init_wallet('wallet1')
        self.wallet2 = self.init_wallet('wallet2')
        self.trans_itx = utils.build_transfer_itx(
            to=self.wallet2.wallet.address,
            value=1,
        )

    def init_wallet(self, moniker):
        res = rpc.create_wallet(
            wallet_type=self.wallet_type,
            moniker=moniker,
            passphrase='abc123',
        )
        return res

    def test_get_tx(self):
        tx_hash = self.test_send_tx().hash

        hash_list = [tx_hash]
        print("hash to get", tx_hash)

        res = rpc.get_tx(tx_hash=hash_list)
        for i in res:
            print(i)
            assert (i.code == 0)

    def test_get_block(self):
        height_list = [1, 2, 3]
        res = rpc.get_block(height=height_list)
        for i in res:
            assert (i.code == 0)
            print(i)

    @validate_response
    def test_send_tx(self):
        kwargs = {
            'itx': self.trans_itx,
            'type_url': 'fg:t:transfer',
            'wallet': self.wallet1.wallet,
            'token': self.wallet1.token,
        }
        tx = rpc.build_signed_tx(**kwargs)
        return rpc.send_tx(tx=tx)

    @validate_response
    def test_get_chain_info(self):
        return rpc.get_chain_info()

    @validate_response
    def test_search(self):
        return rpc.search(key='1', value='2')

    @validate_response
    def test_load_wallet(self):
        return rpc.load_wallet(
            address=self.wallet1.wallet.address,
            passphrase='abc123',
        )

    @validate_response
    def test_recover_wallet(self):
        temp_wallet = rpc.create_wallet(passphrase='abcd123')
        return rpc.recover_wallet(
            wallet_type=self.wallet_type,
            data=temp_wallet.wallet.sk,
            passphrase='abcd123',
            moniker='bobalice',
        )

    @validate_response
    def test_remove_wallet(self):
        return rpc.remove_wallet(address=self.wallet1.wallet.address)

    def test_get_account_state(self):
        sleep(5)

        def verify_result(req):
            res = rpc.get_account_state(req)
            for i in res:
                print(i)
                assert (i.code == 0)
                assert (i.state.moniker == 'wallet1')

        wallet1_addr = self.wallet1.wallet.address

        dict_list = [{'address': wallet1_addr}, {'address': wallet1_addr}]
        single_dict = [{'address': wallet1_addr}]

        verify_result(dict_list)
        verify_result(single_dict)
        res = rpc.get_account_state(dict_list)
        for i in res:
            print(type(i.state.pk))

    @validate_response
    def test_forge_state(self):
        return rpc.get_forge_state()

    @validate_response
    def test_send_itx(self):
        return rpc.send_itx(
            type_url='fg:t:transfer', tx=self.trans_itx,
            wallet=self.wallet1.wallet, token=self.wallet1.token,
        )

    @validate_response
    def test_poke_tx(self):
        return rpc.send_itx(
            tx=utils.build_poke_itx(),
            wallet=self.wallet1.wallet,
            token=self.wallet1.token,
            nonce=0,
        )
