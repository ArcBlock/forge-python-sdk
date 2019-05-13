import ast
import json
import logging
from datetime import datetime

from forge_sdk import utils
from forge_sdk.did import lib
from forge_sdk.did.lib import HASH_MAP
from forge_sdk.did.lib import KEY_MAP
from forge_sdk.did.lib import ROLE_MAP
from forge_sdk.mcrypto.hasher import Hasher
from forge_sdk.mcrypto.signer import Signer

logger = logging.getLogger('abt-did')


class AbtDid:
    PREFIX = 'did:abt:'
    MIN_30 = 1800

    def __init__(self, role_type='account',
                 key_type='ed25519',
                 hash_type='sha3', **kwargs):
        """
        Initialize an AbtDid Instance.

        Args:
            role_type(string): role type of this did instance, default is 'account'
            key_type(string): key type of this did instance, default is 'ed25519'
            hash_type: hash type of this did instance, defualt is 'sha3'

        Kwargs:
            encode(bool): if the calculated did address should be encoded.
                Defaults to True.
            form(stirng): can be either 'short' or 'long'. Decides if the did
                address should include the prefix or not. Defaults to be 'long'.

        """
        self.role_type = role_type
        assert (role_type in ROLE_MAP.keys())

        self.key_type = key_type
        assert (key_type in KEY_MAP.keys())
        self.signer = Signer(key_type)

        self.hash_type = hash_type
        assert (hash_type in HASH_MAP.keys())
        self.hasher = Hasher(hash_type)

        self.encode = kwargs.get('encode', True)
        self.form = kwargs.get('form', 'long')

    def new(self):
        """
        Generate a new did address

        Returns:
            string

        """
        sk, pk = self.signer.keypair()
        return self.sk_to_did(sk)

    @staticmethod
    def parse_type_from_did(did):
        """
        Parse the correct DID type used in provided did address
        Args:
            did(string): did address

        Returns:
            :obj:`AbtDid`
        Examples:
            >>> did_type = AbtDid.parse_type_from_did('did:abt:z1jqq6DaT76Q9aTRZ4ndNjh9AthotPBvyEP')
            >>> did_type.hash_type
            'sha3'
            >>> did_type.role_type
            'account'
            >>> did_type.key_type
            'ed25519'

        """
        try:
            did = did.lstrip(AbtDid.PREFIX)
            decoded = utils.multibase_b58decode(did)
            type_bytes = decoded[0:2]
            return AbtDid.__bytes_to_type(type_bytes)
        except Exception as e:
            logger.error('Fail to parse type from given did {}'.format(did))
            logger.error(e, exc_info=True)

    def sk_to_did(self, sk):
        """
        Use provided secret key to create a DID
        Args:
            sk(bytes): secret key

        Returns:
            string

        Examples:
            >>> import base64
            >>> sk = base64.b16decode('3E0F9A313300226D51E33D5D98A126E86396956122E97E32D31CEE2277380B83FF47B3022FA503EAA1E9FA4B20FA8B16694EA56096F3A2E9109714062B3486D9')
            >>> AbtDid().sk_to_did(sk)
            'did:abt:z1ioGHFYiEemfLa3hQjk4JTwWTQPu1g2YxP'

        """
        pk = self.signer.sk_to_pk(sk)
        return self.pk_to_did(pk)

    def pk_to_did(self, pk):
        """
        Use provided public key to create a DID
        Args:
            pk(bytes): public key

        Returns:
            string

        Examples:
            >>> import base64
            >>> pk = base64.b16decode('A5AB55816BB81D2526D5CAE3CE3082F4F2FAF9D658D8938EC085E8BADAFF5B9F')
            >>> AbtDid().pk_to_did(pk)
            'did:abt:z1XEw92uJKkTqyTuMnFFQ1BrgkGinfz72dF'

        """
        type_bytes = self.__type_to_bytes()
        pk_hash = self.hasher.hash(pk)
        extended_hash = type_bytes + pk_hash[0:20]

        did_bytes = extended_hash + self.hasher.hash(extended_hash)[0:4]
        encoded_did = utils.multibase_b58encode(did_bytes)

        if not self.encode:
            return did_bytes
        elif self.form == 'long':
            return AbtDid.PREFIX + encoded_did
        else:
            return encoded_did

    @staticmethod
    def is_match_pk(did, pk):
        """
        check if the provided did is calculated from provided public key

        Args:
            did(string): did address
            pk(bytes): public key

        Returns:
            bool

        Examples:
            >>> import base64
            >>> pk = base64.b16decode('A5AB55816BB81D2526D5CAE3CE3082F4F2FAF9D658D8938EC085E8BADAFF5B9F')
            >>> did_address ='did:abt:z1XEw92uJKkTqyTuMnFFQ1BrgkGinfz72dF'
            >>> AbtDid.is_match_pk(did_address, pk)
            True

        """
        if did.startswith(AbtDid.PREFIX):
            did = did.lstrip(AbtDid.PREFIX)
        try:
            decoded = utils.multibase_b58decode(did)
            type_bytes = decoded[0:2]
            did_type = AbtDid.__bytes_to_type(type_bytes)
            if did == did_type.pk_to_did(pk).lstrip(AbtDid.PREFIX):
                return True
            return False
        except Exception as e:
            logger.error('Fail to match pk {}'.format(pk))
            logger.error(e, exc_info=True)
            return False

    @staticmethod
    def is_valid(did):
        """
        Check is the provided DID address valid

        Args:
            did(string): DID address

        Returns:
            bool

        Examples:
            >>> AbtDid.is_valid('did:abt:z1XEw92uJKkTqyTuMnFFQ1BrgkGinfz72dF')
            True
            >>> AbtDid.is_valid('did:abt:z1XEw92uJKkTqyTuMnFFQ1Brgk72dF')
            False

        """
        did = did.lstrip('did:abt:')
        try:
            decoded = utils.multibase_b58decode(did)
            type_bytes = decoded[0:2]
            pk_hash = decoded[2:22]
            actual_check_sum = decoded[22:26]

            did_type = AbtDid.__bytes_to_type(type_bytes)
            expectued_check_sum = did_type.hasher.hash(type_bytes + pk_hash)[
                0:4]
            if actual_check_sum == expectued_check_sum:
                return True
            return False
        except Exception as e:
            logger.error('Fail to verify did {}'.format(did))
            logger.error(e, exc_info=True)
            return False

    def __type_to_bytes(self):
        role_bits = lib.to_six_bits(ROLE_MAP.get(self.role_type))
        key_bits = lib.to_five_bits(KEY_MAP.get(self.key_type))
        hash_bits = lib.to_five_bits(HASH_MAP.get(self.hash_type))

        first_byte = bytes([int((role_bits + key_bits[0:2]), 2)])
        second_byte = bytes([int((key_bits[2:] + hash_bits), 2)])
        return first_byte + second_byte

    @staticmethod
    def __bytes_to_type(input_bytes):
        bits = bin(utils.bytes_to_int(input_bytes) | 65536)[3:]
        role_type = lib.get_did_type_key(ROLE_MAP, bits[0:6])
        key_type = lib.get_did_type_key(KEY_MAP, bits[6:11])
        hash_type = lib.get_did_type_key(HASH_MAP, bits[11:16])

        return AbtDid(role_type=role_type,
                      key_type=key_type,
                      hash_type=hash_type)

    def gen_and_sign(self, sk, extra):
        """
        Generate and Sign JWT token

        Args:
            sk(bytes): secret key
            extra(dict): additional data to be included in the token

        Returns:
            string

        Examples:
            >>> import base64
            >>> sk = base64.b16decode('5C57BE8571841383774398891CA42917924B244513FB923E201D60D8795F682EF04A5204D6C529FBB3C435F62E042DB4E6D2BBF839A723A83A8B30740F0AD524')
            >>> res = AbtDid().gen_and_sign(sk, {'origin': 'testdata'})
            >>> res.split(".")[0]
            'eyJhbGciOiAiRWQyNTUxOSIsICJ0eXAiOiAiSldUIn0'

        """
        now = round(datetime.utcnow().timestamp())
        middle = lib.clean_dict({'iss': self.sk_to_did(sk),
                                 'iat': now,
                                 'nbf': now,
                                 'exp': now + AbtDid.MIN_30,
                                 **extra,
                                 })
        body = utils.multibase_b64encode(json.dumps(middle))
        data = self.__header() + '.' + body
        signature = utils.multibase_b64encode(
            self.signer.sign(data.encode(), sk))
        return data + '.' + signature

    def __header(self):
        if self.key_type == 'ed25519':
            alg = 'Ed25519'
        elif self.key_type == 'secp256k1':
            alg = 'ES256K'

        return utils.multibase_b64encode(json.dumps({
            'alg': alg,
            'typ': 'JWT'
        }))

    @staticmethod
    def verify(token, pk):
        """
        Verify if the token matches the public key

        Args:
            token(string): JWT token
            pk(bytes): public key

        Returns:
            bool

        Examples:
            >>> import base64
            >>> token='eyJhbGciOiAiRWQyNTUxOSIsICJ0eXAiOiAiSldUIn0.eyJpc3MiOiAiZGlkOmFidDp6MWYyaFB1ZEZnanRhOGNkRVYyeFRZaGRhcjNEb2ZxSGhkNiIsICJpYXQiOiAxNTU2NzcyNDE1LCAibmJmIjogMTU1Njc3MjQxNSwgImV4cCI6IDE1NTY3NzQyMTUsICJvcmlnaW4iOiAidGVzdGRhdGEifQ.sdbRA4_-gtMhlTRqhNzxnqYG-sFl3EGFOpVcsX6sSZ0E_33k6ga8jPTmNMkRz3DdFwnW_M62oK_-nFSw9wJQBw'
            >>> pk =base64.b16decode('F04A5204D6C529FBB3C435F62E042DB4E6D2BBF839A723A83A8B30740F0AD524')
            >>> AbtDid.verify(token, pk)
            True
        """
        try:
            header, body, signature = token.split('.')
            alg = lib.b64decode_to_dict(header).get('alg').lower()
            if alg == 'secp256k1' or alg == 'es256k':
                signer = Signer('secp256k1')
            elif alg == 'ed25519':
                signer = Signer('ed25519')

            sig = utils.multibase_b64decode(signature)
            is_sig_valid = signer.verify((header + '.' + body).encode(),
                                         sig, pk)
            did = lib.b64decode_to_dict(body).get('iss')
            if is_sig_valid and AbtDid.is_match_pk(did, pk):
                return True
            return False
        except Exception as e:
            logger.error(e, exc_info=True)
            logger.error("Fail to verify token {0} and pk {1}"
                         .format(token, pk))
            return False
