from forge_sdk.did.abt_did import AbtDid
from forge_sdk.did.lib import *
from forge_sdk.mcrypto import Hasher


def get_asset_address(did_address, itx):
    """
    Calculate asset address for specific asset

    Args:
        did_address(string): user's did address to create this asset
        itx(:obj:`google.protobuf.any`): encoded createAssetTx

    Returns:
        asset_address(string)

    """
    data = did_address.encode() + Hasher('sha3').hash(itx.SerializeToString())
    parsed_type = AbtDid.parse_type_from_did(did_address)
    asset_did = AbtDid(role_type='asset', key_type=parsed_type.key_type,
                       hash_type=parsed_type.hash_type)
    asset_address = asset_did.pk_to_did(data).split(":")[-1]
    return asset_address
