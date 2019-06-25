import random

from forge_sdk import did
from forge_sdk.protos import protos

RANDOM_NONCE = random.randint(1, 10000)


def build_unsigned_tx(itx, chain_id, nonce=RANDOM_NONCE, wallet=None, pk=None,
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


def sign_tx(wallet, tx, round=None):
    did_type = did.AbtDid.parse_type_from_did(wallet.address, round=round)
    tx_hash = did_type.hasher.hash(tx.SerializeToString())
    signature = did_type.signer.sign(tx_hash, wallet.sk)
    return signature


def is_sk_included(wallet):
    return wallet.sk and not wallet.sk == b''



def build_signed_tx_local(itx, wallet,  chain_id, nonce=RANDOM_NONCE):
    tx = build_unsigned_tx(
        itx=itx, wallet=wallet, nonce=nonce, chain_id=chain_id)
    tx.signature = sign_tx(wallet, tx)
    return tx


def build_multisig_tx_local(tx, wallet, data):
    # Prepare tx to be multisigned
    add_multisigs(
        tx, [create_multisig(wallet=wallet, data=data)])

    # Add multisign to tx
    new_multisigs = [create_multisig(
        wallet=wallet, tx=tx, data=data)]
    add_multisigs(tx, new_multisigs)
    return tx
