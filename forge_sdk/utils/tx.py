from forge_sdk.protos import protos
from forge_sdk.utils.crypto import hash_data, sign_data


def sign_tx(tx, wallet, rd=None):
    signed_tx = protos.Transaction()
    signed_tx.CopyFrom(tx)
    tx_hash = hash_data(tx.SerializeToString(), wallet, rd=rd)
    signature = sign_data(tx_hash, wallet, rd=rd)
    signed_tx.signature = signature
    return signed_tx


def multisign_tx(tx, wallet, multisig_data=None, delegatee=None):
    res_tx = add_multisigs(
            tx, [build_multisig(wallet=wallet,
                                multisig_data=multisig_data,
                                delegatee=delegatee)])

    signed_multisig = build_multisig(
            wallet=wallet,
            multisig_data=multisig_data,
            tx=res_tx,
            delegatee=delegatee)
    res_tx = add_multisigs(tx, [signed_multisig])
    return res_tx


def build_multisig(wallet, **kwargs):
    tx = kwargs.get('tx')
    delegatee = kwargs.get('delegatee')
    if tx:
        tx_hash = hash_data(tx.SerializeToString(), wallet,
                            rd=kwargs.get('rd'))
        signature = sign_data(tx_hash, wallet, rd=kwargs.get('rd'))
    else:
        signature = None
    return protos.Multisig(
            signer=delegatee if delegatee else wallet.address,
            pk=wallet.pk,
            signature=signature,
            data=kwargs.get('multisig_data'),
            delegator=wallet.address if delegatee else None,
    )


def add_multisigs(tx, multisigs):
    res_tx = protos.Transaction()
    res_tx.CopyFrom(tx)

    del res_tx.signatures[:]
    res_tx.signatures.extend(multisigs)

    return res_tx
