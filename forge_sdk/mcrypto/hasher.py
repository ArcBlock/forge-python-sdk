import hashlib

import sha3


def is_sha2(name):
    return name.startswith('sha2')


def parse_hash_type(name):
    if name == 'sha2':
        return 'sha256'
    elif name.startswith('sha2_'):
        return name.replace('sha2_', 'sha')
    elif name == 'sha3':
        return 'sha3_256'
    elif name == 'keccak':
        return 'keccak_256'
    else:
        return name


class Hasher:
    sizes = [224, 256, 384, 512]
    types = ['sha2', 'sha3', 'keccak']

    def __init__(self, name, round=None):
        self.name = name
        self.supported_hash = [t + '_' + str(z) for t in Hasher.types
                               for z in Hasher.sizes] + Hasher.types

        if is_sha2(name) and not round:
            self.round = 2
        else:
            self.round = round if round else 1

    def is_supported(self, name):
        if name in self.supported_hash:
            return True
        else:
            return False

    def init_hasher(self, name):
        if not self.is_supported(name):
            raise NameError("{} hash type is not supported.".format(name))

        hash_type = parse_hash_type(name)
        if '_' not in hash_type:
            res = getattr(hashlib, hash_type)
        else:
            res = getattr(sha3, hash_type)
        return res()

    def hash(self, data_bytes):
        """
        Create hash of provided data

        Args:
            data_bytes(bytes): data needs to be hashed

        Returns: string

        """
        res = data_bytes
        for i in range(0, self.round):
            hash_helper = self.init_hasher(self.name)
            hash_helper.update(res)
            res = hash_helper.digest()
        return res
