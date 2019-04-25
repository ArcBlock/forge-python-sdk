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


def get_did_type_key(dic, bits):
    for k, v in dic.items():
        if v == int(b'0b' + bits.encode(), 2):
            return k
    raise ValueError('Bits {} does not have a corresponded type.'.format(bits))


def to_six_bits(num):
    return bin(num | 64)[3:]


def to_five_bits(num):
    return bin(num | 32)[3:]
