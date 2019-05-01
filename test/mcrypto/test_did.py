import base64
import unittest

from forge_sdk.did import AbtDid
from forge_sdk.mcrypto import Signer


class DidTest(unittest.TestCase):

    def setUp(self):
        self.sk, self.pk = Signer().keypair()
        self.did = AbtDid()

    # Test did to bytes
    def test_did_to_bytes(self):
        res = self.did.type_to_bytes()
        print(res)
        assert (res == bytes([0, 1]))

    def test_did_to_bytes_1(self):
        did = AbtDid(hash_type='sha3_512')
        res = did.type_to_bytes()
        print(res)
        assert (res == bytes([0, 5]))

    def test_did_to_bytes_2(self):
        did = AbtDid(role_type='application', key_type='secp256k1',
                     hash_type='sha3_512')
        res = did.type_to_bytes()
        print(res)
        assert (base64.b16encode(res) == b'0C25')

    # Test bytes to did
    def test_bytes_to_did(self):
        did = AbtDid.__bytes_to_type(bytes([0, 1]))
        assert (did.role_type == self.did.role_type)
        assert (did.key_type == self.did.key_type)
        assert (did.hash_type == self.did.hash_type)

    # Test did general actions

    def test_sk_to_did(self):
        sk = base64.b16decode(
            '3E0F9A313300226D51E33D5D98A126E86396956122E97E3'
            '2D31CEE2277380B83FF47B3022FA503EAA1E9FA4B20FA8B'
            '16694EA56096F3A2E9109714062B3486D9')
        did = self.did.sk_to_did(sk)
        print(did)
        assert (did == "did:abt:z1ioGHFYiEemfLa3hQjk4JTwWTQPu1g2YxP")

    def test_match_pk(self):
        did = self.did.pk_to_did(self.pk)
        assert (AbtDid.is_match_pk(did, self.pk))

        false_did = "z2ioGHFYiEemfLa3hQjk4JTwWTQPu1g2YxP"
        assert (not AbtDid.is_match_pk(false_did, self.pk))

    def test_is_valid(self):
        assert (AbtDid.is_valid("did:abt:z1muQ3xqHQK2uiACHyChikobsiY5kLqtShA"))
        assert (AbtDid.is_valid("z1muQ3xqHQK2uiACHyChikobsiY5kLqtShA"))
        assert (not AbtDid.is_valid("z2muQ3xqHQK2uiACHyChikobsiY5kLqtShA"))
        assert (not AbtDid.is_valid("z1muQ3xqHQK2uiACHyChikobsiY5kLqtSha"))

    def test_gen_and_sign(self):
        token = self.did.gen_and_sign(self.sk, {'origin': 'testdata'})

        assert (AbtDid.verify(token, self.pk))

    def test_gen_and_sign2(self):
        sk = base64.b16decode(
            'D67C071B6F51D2B61180B9B1AA9BE0DD0704619F0E30453AB4A'
            '592B036EDE644E4852B7091317E3622068E62A5127D1FB0D4AE2'
            'FC50213295E10652D2F0ABFC7')
        pk = Signer().sk_to_pk(sk)
        token = self.did.gen_and_sign(sk, {'origin': 'testdata'})
        assert (AbtDid.verify(token, pk))
