import ed25519
import secp256k1


class Signer:
    def __init__(self, name='ed25519'):
        self.signer = Ed25519Signer

        if name == 'secp256k1':
            self.signer = Secp256k1Signer

        self.keypair = self.signer.keypair
        self.sk_to_pk = self.signer.sk_to_pk
        self.sign = self.signer.sign
        self.verify = self.signer.verify


class Ed25519Signer:

    @staticmethod
    def keypair():
        return ed25519.create_keypair()

    @staticmethod
    def sk_to_pk(sk):
        secret_key = ed25519.SigningKey(sk)
        public_key = secret_key.get_verifying_key()
        return public_key

    @staticmethod
    def sign(data, sk):
        secret_key = ed25519.SigningKey(sk)
        signature = secret_key.sign(data)
        return signature

    @staticmethod
    def verify(data, signature, pk):
        public_key = ed25519.VerifyingKey(pk)
        result = public_key.verify(signature, data)
        return result


class Secp256k1Signer:

    @staticmethod
    def keypair():
        return

    @staticmethod
    def sk_to_pk(sk):
        secret_key = secp256k1.PrivateKey(sk)
        public_key = secret_key._gen_public_key(secret_key)
        return public_key

    @staticmethod
    def sign(data, sk):
        secret_key = secp256k1.PrivateKey(sk)
        signature = secret_key.ecdsa_sign(data)
        return signature

    @staticmethod
    def verify(data, signature, pk):
        public_key = secp256k1.PublicKey(pk)
        result = public_key.ecdsa_verify(data, signature)
        return result
