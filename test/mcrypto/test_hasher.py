import base64
import unittest

from forge_sdk.mcrypto import Hasher


class HasherTest(unittest.TestCase):

    def setUp(self):
        self.data = b'hello'

    def test_sha256(self):
        hash_helper = Hasher('sha2')
        result = base64.b16encode(hash_helper.hash(b''))
        assert (
            result == b'5DF6E0E2761359D30A8275058E299FCC0381534545F55CF43E41983F5D4C9456')

    def test_sha256_data(self):
        hash_helper = Hasher('sha2')
        result = base64.b16encode(hash_helper.hash(self.data))
        print(result)
        assert (
            result == b'9595C9DF90075148EB06860365DF33584B75BFF782A510C6CD4883A419833D50')

    def test_sha256_data_round1(self):
        hash_helper = Hasher('sha2', round=1)
        result = base64.b16encode(hash_helper.hash(self.data))
        print(result)
        assert (result ==
                b'2CF24DBA5FB0A30E26E83B2AC5B9E29E1B161E5C1FA7425E73043362938B9824')

    def test_sha384_data(self):
        hash_helper = Hasher('sha2_384')
        result = base64.b16encode(hash_helper.hash(self.data))
        assert (
            result == b'D47D89FFD5071E8260CD6FCA1A4668605871AF5FBEDBED7375A1117C8C14C82D3CEAC2344DD1E03035AE1C5E755CF5F2')

    def test_sha3_256_data(self):
        hash_helper = Hasher('sha3')
        result = base64.b16encode(hash_helper.hash(self.data))
        print(result)
        assert (
            result == b'3338BE694F50C5F338814986CDF0686453A888B84F424D792AF4B9202398F392')

    def test_keccak_256_data(self):
        hash_helper = Hasher('keccak_256')
        result = base64.b16encode(hash_helper.hash(self.data))
        print(result)
        assert (
            result == b'1C8AFF950685C2ED4BC3174F3472287B56D9517B9C948127319A09A7A36DEAC8')

    def test_keccak_data(self):
        hash_helper = Hasher('keccak')
        result = base64.b16encode(hash_helper.hash(self.data))
        print(result)
        assert (
            result == b'1C8AFF950685C2ED4BC3174F3472287B56D9517B9C948127319A09A7A36DEAC8')

    def test_keccak_384_data(self):
        hash_helper = Hasher('keccak_384')
        result = base64.b16encode(hash_helper.hash(self.data))
        print(result)
        assert (
            result == b'DCEF6FB7908FD52BA26AABA75121526ABBF1217F1C0A31024652D134D3E32FB4CD8E9C703B8F43E7277B59A5CD402175')
