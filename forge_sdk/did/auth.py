import json

from forge_sdk import rpc
from forge_sdk import utils
from forge_sdk.config import config
from forge_sdk.did.abt_did import AbtDid


def require_sig(**kwargs):
    user_did_type = AbtDid.parse_type_from_did(kwargs.get('user_did'))

    claim = {
        'type': "signature",
        'data': utils.multibase_b58encode(
                user_did_type.hasher.hash(
                    kwargs.get('tx').SerializeToString())),
        'meta': {
            'description': kwargs.get('description')
        },
        'method': user_did_type.hash_type,
        'origin': utils.multibase_b58encode(
            kwargs.get('tx').SerializeToString()),
    }

    return build_claims([claim], **kwargs)


def require_asset(**kwargs):
    claim = {
        'type': "did",
        'meta': {
            'description': kwargs.get('description')
        },
        'did_type': 'asset',
        'target': kwargs.get('target'),
    }

    return build_claims([claim], **kwargs)


def require_profile(**kwargs):
    claim = {
        'type': 'profile',
        'meta': {
            'description': kwargs.get('description')
        },
        'items': ["fullName", "email"]
    }
    return build_claims([claim], **kwargs)


def build_claims(claims, **kwargs):
    chain_info = rpc.get_chain_info().info
    forge_token = rpc.get_forge_token()
    extra = {
        'url': kwargs.get('url'),
        'action': kwargs.get('action'),
        'appInfo': {
            'chainHost': kwargs.get('chain_host'),
            'chainId': chain_info.network,
            'chainVersion': chain_info.version,
            'chain_token': forge_token.symbol,
            'decimals': forge_token.decimal,
            'description': kwargs.get('app_description', "forge-python-app"),
            'icon': kwargs.get('app_icon', "http://eventchain.arcblock.co:5000/static/images"
                               "/eventchain_h_2.png"),
            'name': kwargs.get('app_name', 'forge-python-app'),
            'subtitle': kwargs.get('app_subtitle', 'This is a decentralized application'),
        },
        'requestedClaims': claims,
        'workflow': {
            'description': kwargs.get('workflow')
        }
    }
    app_did_type = AbtDid.parse_type_from_did(kwargs.get('app_addr'))
    res = {
        'appPk': utils.multibase_b58encode(kwargs.get('app_pk')),
        'authInfo': app_did_type.gen_and_sign(
            kwargs.get('app_sk'), extra)
    }

    return json.dumps(res)
