import unittest

from forge.mcrypto import Signer


class ED25519SignerTest(unittest.TestCase):

    def setUp(self):
        self.signer = Signer()
        self.sk, self.pk = self.signer.keypair()

    def test_ed25519_sk_to_pk(self):
        res_pk = self.signer.sk_to_pk(self.sk)
        assert (res_pk == self.pk)

    def test_ed25519_verify(self):
        data = b'1234'
        bad_data = b'12345'
        sig = self.signer.sign(data, self.sk)
        invalid = self.signer.verify(bad_data, sig, self.pk)
        valid = self.signer.verify(data, sig, self.pk)
        assert(invalid == False)
        assert(valid == True)


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
        assert (invalid == False)
        assert (valid == True)
