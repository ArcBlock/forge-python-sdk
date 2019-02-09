import hashlib


class Hasher:

    def __init__(self, name='sha3', size=256, round=1):
        self.name = name
        self.size = size
        self.round = round

    # only supports sha3_356() for now
    @staticmethod
    def hash(data_bytes):
        result = hashlib.sha3_256()
        result.update(data_bytes)
        return result.hexdigest()
