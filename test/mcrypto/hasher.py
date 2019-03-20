import base64
import unittest

from forge.mcrypto import Hasher


class HasherTest(unittest.TestCase):

    def setUp(self):
        self.data = b'hello'

    def test_sha224(self):
        hash_helper = Hasher('sha2', 224)
        result = hash_helper.hash(b'')
        print(result)

    def test_sha256(self):
        hash_helper = Hasher('sha2')
        result = base64.b16encode(hash_helper.hash(b''))
        assert (
            result == b'5DF6E0E2761359D30A8275058E299FCC0381534545F55CF43E41983F5D4C9456')

    def test_sha256_data(self):
        hash_helper = Hasher('sha2', round=1)
        result = base64.b16encode(hash_helper.hash(self.data))
        assert (
            result == b'9595C9DF90075148EB06860365DF33584B75BFF782A510C6CD4883A419833D50')
