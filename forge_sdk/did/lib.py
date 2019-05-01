import ast
import logging

from forge_sdk import utils

logger = logging.getLogger('forge_sdk-did')

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
    'tx': 10,
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
    'sha2': 6,
}


def get_did_type_key(dic, bits):
    for k, v in dic.items():
        if v == int(b'0b' + bits.encode(), 2):
            return k
    raise ValueError('Bits {} does not have a corresponded type.'.format(bits))


def to_six_bits(num):
    return bin(num | 64)[3:]


def to_five_bits(num):
    return bin(num | 32)[3:]


def b64decode_to_dict(data):
    try:
        dict_string = utils.multibase_b64decode(data).decode()
        return ast.literal_eval(dict_string)
    except Exception as e:
        logger.error('Error in decoding b64urlsafe '
                     'encoded data to dictionary.')
        logger.error(e, exc_info=True)
        return {}


def clean_dict(d):
    return {k: v for k, v in d.items() if v and v != ''}
