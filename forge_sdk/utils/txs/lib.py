from forge_sdk import did
from forge_sdk.protos import protos


def build_unsigned_tx(itx, chain_id, nonce=2, wallet=None, pk=None,
                      address=None):
    params = {
        'from': address if address else wallet.address,
        'nonce': nonce,
        'chain_id': chain_id,
        'pk': pk if pk else wallet.pk,
        'itx': itx
    }
    return protos.Transaction(**params)


def add_multisigs(tx, multisigs):
    del tx.signatures[:]
    tx.signatures.extend(multisigs)


def create_multisig(wallet, tx=None, data=None):
    signature = sign_tx(wallet, tx) if tx else None
    return protos.Multisig(
        signer=wallet.address,
        pk=wallet.pk,
        signature=signature,
        data=data
    )


def sign_tx(wallet, tx):
    did_type = did.AbtDid.parse_type_from_did(wallet.address)
    tx_hash = did_type.hasher.hash(tx.SerializeToString())
    signature = did_type.signer.sign(tx_hash, wallet.sk)
    return signature
