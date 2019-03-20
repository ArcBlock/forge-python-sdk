import hashlib

import sha3


def gen_hasher_name(name, size):
    return str(name) + "_" + str(size)


class Hasher:
    __supported_size = [224, 256, 384, 512]

    @staticmethod
    def is_size_supported(size):
        if size in Hasher.__supported_size:
            return True
        else:
            return False

    def __init__(self, name='sha3', size=256, round=None):
        self.name = name
        self.size = size
        self.round = round

    def init_hasher(self, name, size=256):
        if Hasher.is_size_supported(size):
            if name == 'sha2':
                res = getattr(hashlib, 'sha' + str(size))
            elif name == 'sha3' or name == 'keccak':
                res = getattr(sha3, name + '_' + str(size))
            else:
                raise NameError(
                    'Please provide a valid hasher type: sha2, sha3, '
                    'or keccak')
            return res()
        else:
            raise NameError(
                "Please provide a valid hash size: 224, 256, 384 or 512.")

    def hash(self, data_bytes):
        if self.name == 'sha2' and not self.round:
            r = 2
        else:
            r = self.round if self.round else 1
        res = data_bytes
        for i in range(0, r):
            hash_helper = self.init_hasher(self.name, self.size)
            hash_helper.update(res)
            res = hash_helper.digest()
        return res
