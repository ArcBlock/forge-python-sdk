from forge_sdk import did
from forge_sdk import utils
from forge_sdk.protos import protos


def build_create_asset_itx(type_url, asset, encoded=True, **kwargs):
    encoded_asset = utils.encode_to_any(type_url, asset)
    params = {
        'moniker': kwargs.get('moniker'),
        'readonly': kwargs.get('readonly'),
        'transferrable': kwargs.get('transferrable'),
        'ttl': kwargs.get('ttl'),
        'parent': kwargs.get('parent'),
        'data': encoded_asset,
    }

    itx_no_address = protos.CreateAssetTx(**params)
    asset_address = did.get_asset_address(itx_no_address)
    params['address'] = asset_address
    itx = protos.CreateAssetTx(**params)

    res = itx if not encoded else utils.encode_to_any('fg:t:create_asset', itx)

    return res
