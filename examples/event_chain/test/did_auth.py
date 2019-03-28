import ast
import unittest

from event_chain import protos
from event_chain.application import did_auth

from forge.utils import utils as forge_utils


class AuthRequestTest(unittest.TestCase):

    def setUp(self):
        args = {
            'from': 'z1bdvuibh8L9wG8Re5CZmyzrMYo7rjrV3i7',
            'nonce': 1,
            'pk': b'fakepk',
        }
        self.sample_tx = protos.Transaction(**args)

    def test_require_multisig(self):
        user_did = "z1bdvuibh8L9wG8Re5CZmyzrMYo7rjrV3i7"
        args = {
            'user_did': user_did,
            'tx': self.sample_tx,
            'url': 'http: // sample_url',
            'description': 'this is a test',
            'workflow': 'work-flow-test',
            'action': 'requestAuth'
        }

        response = did_auth.response_require_multisig(**args)

        body = forge_utils.b64encoded_to_dict(
            ast.literal_eval(response).get('authInfo').split('.')[1])

        assert (body.get('url') == 'http: // sample_url')
        assert(body.get('action') == 'requestAuth')
