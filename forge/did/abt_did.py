import logging

from forge.mcrypto.hasher import Hasher
from forge.mcrypto.signer import Signer
from forge.utils import utils

logger = logging.getLogger('abt-did')


class AbtDid:
    PREFIX = 'did:abt:'
    MIN_30 = 1800
    ROLE_MAP = {
        'account': 0,
        'node': 1,
        'device': 2,
        'application': 3,
        'smart_contract': 4,
        'bot': 5,
        'asset': 6,
        'stake': 7,
        'validator': 8,
        'group': 9,
        'any': 63,
    }

    KEY_MAP = {
        'ed25519': 0,
        'secp256k1': 1,
    }

    HASH_MAP = {
        'keecak': 0,
        'sha3': 1,
        'keccak_384': 2,
        'sha3_384': 3,
        'keccak_512': 4,
        'sha3_512': 5,
    }

    def __init__(self, role_type='account',
                 key_type='ed25519',
                 hash_type='sha3', **kwargs):
        self.role_type = role_type
        assert (role_type in AbtDid.ROLE_MAP.keys())

        self.key_type = key_type
        assert (key_type in AbtDid.KEY_MAP.keys())
        self.signer = Signer(key_type)

        self.hash_type = hash_type
        assert (hash_type in AbtDid.HASH_MAP.keys())
        self.hasher = Hasher(hash_type)

        self.encode = kwargs.get('encode', True)
        self.form = kwargs.get('form', 'long')

    @staticmethod
    def parse_type_from_did(did):
        try:
            did = did.lstrip(AbtDid.PREFIX)
            decoded = utils.multibase_b58decode(did)
            type_bytes = decoded[0:2]
            return AbtDid.bytes_to_type(type_bytes)
        except Exception as e:
            logger.error('Fail to parse type from given did {}'.format(did))
            logger.error(e, exc_info=True)

    def sk_to_did(self, sk):
        pk = self.signer.sk_to_pk(sk)
        return self.pk_to_did(pk)

    def pk_to_did(self, pk):
        type_bytes = self.type_to_bytes()
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
        if did.startswith(AbtDid.PREFIX):
            did = did.lstrip(AbtDid.PREFIX)
        try:
            decoded = utils.multibase_b58decode(did)
            type_bytes = decoded[0:2]
            did_type = AbtDid.bytes_to_type(type_bytes)
            if did == did_type.pk_to_did(pk).lstrip(AbtDid.PREFIX):
                return True
            return False
        except Exception as e:
            logger.error('Fail to match pk {}'.format(pk))
            logger.error(e, exc_info=True)
            return False

    @staticmethod
    def is_valid(did):
        did = did.lstrip('did:abt:')
        try:
            decoded = utils.multibase_b58decode(did)
            type_bytes = decoded[0:2]
            pk_hash = decoded[2:22]
            actual_check_sum = decoded[22:26]

            did_type = AbtDid.bytes_to_type(type_bytes)
            expectued_check_sum = did_type.hasher.hash(type_bytes + pk_hash)[
                0:4]
            if actual_check_sum == expectued_check_sum:
                return True
            return False
        except Exception as e:
            logger.error('Fail to verify did {}'.format(did))
            logger.error(e, exc_info=True)
            return False

    def type_to_bytes(self):
        role_bits = to_six_bits(AbtDid.ROLE_MAP.get(self.role_type))
        key_bits = to_five_bits(AbtDid.KEY_MAP.get(self.key_type))
        hash_bits = to_five_bits(AbtDid.HASH_MAP.get(self.hash_type))

        first_byte = bytes([int((role_bits + key_bits[0:2]), 2)])
        second_byte = bytes([int((key_bits[2:] + hash_bits), 2)])
        return first_byte + second_byte

    @staticmethod
    def bytes_to_type(input_bytes):
        bits = bin(utils.bytes_to_int(input_bytes) | 65536)[3:]
        role_type = get_did_type_key(AbtDid.ROLE_MAP, bits[0:6])
        key_type = get_did_type_key(AbtDid.KEY_MAP, bits[6:11])
        hash_type = get_did_type_key(AbtDid.HASH_MAP, bits[11:16])

        return AbtDid(role_type=role_type,
                      key_type=key_type,
                      hash_type=hash_type)

    def gen_and_sign(self, sk, extra):
        now = utils.current_utc_timestamp()
        middle = utils.clean_dict({'iss': self.sk_to_did(sk),
                                   'iat': now,
                                   'nbf': now,
                                   'exp': now + AbtDid.MIN_30,
                                   **extra,
                                   })
        body = utils.to_json_b64urlsafe(middle)
        data = self.__header() + '.' + body
        signature = utils.b64encode_no_padding(
            self.signer.sign(data.encode(), sk))
        return data + '.' + signature

    def __header(self):
        if self.key_type == 'ed25519':
            alg = 'Ed25519'
        elif self.key_type == 'secp256k1':
            alg = 'ES256K'

        return utils.to_json_b64urlsafe({
            'alg': alg,
            'typ': 'JWT'
        })

    @staticmethod
    def verify(token, pk):
        try:
            header, body, signature = token.split('.')
            alg = utils.b64encoded_to_dict(header).get('alg').lower()
            if alg == 'secp256k1' or alg == 'es256k':
                signer = Signer('secp256k1')
            elif alg == 'ed25519':
                signer = Signer('ed25519')

            sig = utils.b64decode_padding_safe(signature)
            is_sig_valid = signer.verify((header + '.' + body).encode(),
                                         sig, pk)
            did = utils.b64encoded_to_dict(body).get('iss')
            if is_sig_valid and AbtDid.is_match_pk(did, pk):
                return True
            return False
        except Exception as e:
            logger.error(e, exc_info=True)
            logger.error("Fail to verify token {0} and pk {1}"
                         .format(token, pk))
            return False


def get_did_type_key(dic, bits):
    for k, v in dic.items():
        if v == int(b'0b' + bits.encode(), 2):
            return k
    raise ValueError('Bits {} does not have a corresponded type.'.format(bits))


def to_six_bits(num):
    return bin(num | 64)[3:]


def to_five_bits(num):
    return bin(num | 32)[3:]
