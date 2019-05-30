import json

from forge_sdk import rpc
from forge_sdk import utils
from forge_sdk.config import config
from forge_sdk.did.abt_did import AbtDid


def require_sig(**kwargs):
    user_did_type = AbtDid.parse_type_from_did(kwargs.get('user_did'))

    claim = {
        'data': utils.multibase_b58encode(
            user_did_type.hasher.hash(
                kwargs.get('tx').SerializeToString())),
        'meta': {
            'description': kwargs.get('description')
        },
        'method': user_did_type.hash_type,
        'origin': utils.multibase_b58encode(
            kwargs.get('tx').SerializeToString()),
        'type': "signature",
    }

    return response([claim], **kwargs)


def require_asset(**kwargs):
    claim = {
        'meta': {
            'description': kwargs.get('description')
        },
        'did_type': 'asset',
        'target': kwargs.get('target'),
        'type': "did",
    }

    return response([claim], **kwargs)


def response(claims, **kwargs):
    chain_info = rpc.get_chain_info().info
    forge_token = rpc.get_forge_token()
    extra = {
        'url': kwargs.get('url'),
        'action': kwargs.get('action'),
        'appInfo': {
            'chainHost': 'http://{0}:{1}/api'.format(config.get_app_host(),
                                                     config.get_forge_port()),
            'chainId': chain_info.network,
            'chainVersion': chain_info.version,
            'chain_token': forge_token.symbol,
            'decimals': forge_token.decimal,
            'description': 'Create and join events on Event Chain',
            'icon': "http://eventchain.arcblock.co:5000/static/images"
                    "/eventchain_h_2.png",
            'name': 'Event Chain',
            'subtitle': 'A decentralized solution for events',
        },
        'requestedClaims': claims,
        'workflow': {
            'description': kwargs.get('workflow')
        }
    }
    app_did_type = AbtDid.parse_type_from_did(kwargs.get('APP_ADDR'))
    res = {
        'appPk': utils.multibase_b58encode(kwargs.get('APP_PK')),
        'authInfo': app_did_type.gen_and_sign(
            kwargs.get('APP_SK'), extra)
    }

    return json.dumps(res)
