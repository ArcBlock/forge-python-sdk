import base64
import unittest

from forge_sdk.mcrypto import Signer


class ED25519SignerTest(unittest.TestCase):

    def setUp(self):
        self.signer = Signer()
        self.sk, self.pk = self.signer.keypair()

    def test_ed25519_sk_to_pk(self):
        res_pk = self.signer.sk_to_pk(self.sk)
        assert (res_pk == self.pk)

        new_sk = base64.b16decode('D67C071B6F51D2B61180B9B1AA9BE0DD0704619'
                                  'F0E30453AB4A592B036EDE644E4852B7091317E3'
                                  '622068E62A5127D1FB0D4AE2FC502132'
                                  '95E10652D2F0ABFC7')
        new_pk = base64.b16decode('E4852B7091317E3622068E62A5127D1FB0D4AE2'
                                  'FC50213295E10652D2F0ABFC7')
        assert(self.signer.sk_to_pk(new_sk) == new_pk)

    def test_ed25519_verify(self):
        data = b'1234'
        bad_data = b'12345'
        sig = self.signer.sign(data, self.sk)
        invalid = self.signer.verify(bad_data, sig, self.pk)
        valid = self.signer.verify(data, sig, self.signer.sk_to_pk(self.sk))
        assert not invalid
        assert valid


class Secp256K1SignerTest(unittest.TestCase):

    def setUp(self):
        self.signer = Signer('secp256k1')
        self.sk, self.pk = self.signer.keypair()

    def test_secp256k1_sk_to_pk(self):
        res_pk = self.signer.sk_to_pk(self.sk)
        assert (res_pk == self.pk)

    def test_secp256k1_verify(self):
        data = b'1234'
        bad_data = b'12345'
        sig = self.signer.sign(data, self.sk)
        invalid = self.signer.verify(bad_data, sig, self.pk)
        valid = self.signer.verify(data, sig, self.pk)
        assert not invalid
        assert valid
