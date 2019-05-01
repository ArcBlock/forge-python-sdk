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

    @staticmethod
    def parse_type_from_did(did):
        """
        Parse the correct DID type used in provided did address
        Args:
            did(string): did address

        Returns: did_type(:obj:`AbtDid`)

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

        Returns: did(string)

        """
        pk = self.signer.sk_to_pk(sk)
        return self.pk_to_did(pk)

    def pk_to_did(self, pk):
        """
        Use provided public key to create a DID
        Args:
            pk(bytes): public key

        Returns: string

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

        Returns: boolean

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

        Returns: boolean

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

        Returns: string

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

        Returns: boolean

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
