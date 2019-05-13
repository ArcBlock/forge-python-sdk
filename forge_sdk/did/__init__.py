from forge_sdk.did.abt_did import AbtDid
from forge_sdk.did.lib import *
from forge_sdk.mcrypto import Hasher


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
    asset_did = AbtDid(role_type='asset')
    asset_address = asset_did.pk_to_did(data).split(":")[-1]
    return asset_address
