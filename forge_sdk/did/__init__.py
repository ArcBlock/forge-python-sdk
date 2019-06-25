from forge_sdk.did.abt_did import AbtDid
from forge_sdk.did.auth import *
from forge_sdk.did.lib import *
from forge_sdk.did.mobile import WalletResponse
from forge_sdk.mcrypto import Hasher

PREFIX = "did:abt:"


def get_asset_address(itx):
    """
    Calculate asset address for provided CreateAssetTx

    Args:
        did_address(string): user's did address to create this asset
        itx(:obj:`google.protobuf.any`): encoded createAssetTx

    Returns:
        asset_address(string)

    Examples:
        >>> from forge_sdk import protos, utils
        >>> itx = protos.CreateAssetTx(data=utils.encode_to_any(None,b'123'))
        >>> res = get_asset_address(itx)

    """
    data = itx.SerializeToString()
    asset_did = AbtDid(role_type='asset', form='short')
    asset_address = asset_did.pk_to_did(data)
    return asset_address


def get_stake_address(addr1, addr2):
    hasher = Hasher('sha3')
    hash = hasher.hash((addr1+addr2).encode())
    stake_did = AbtDid(role_type='stake', form='short')
    stake_address = stake_did.hash_to_did(hash)
    return stake_address


def get_tether_address(hash):
    tether_did = AbtDid(role_type='tether',
                        hash_type='sha2', round=1, form='short')
    return tether_did.hash_to_did(hash)
