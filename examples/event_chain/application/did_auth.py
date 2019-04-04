import json

from event_chain.config import config
from event_chain.utils import helpers

from forge import AbtDid
from forge.rpc import rpc as forge_rpc
from forge.utils import utils as forge_utils

APP_SK = b'0\243\016\303\017\r\305\026#~\301\227\033;\274\303pl\243 \004,' \
         b'\224c\003\261\2629&G\345\020\317w\007P\234\211g\246Q\264P\325\346' \
         b'/}E\020\304\365\216\242\033o\302\206v\203\303+\206n\212'

APP_PK = b'\317w\007P\234\211g\246Q\264P\325\346/}E\020\304\365\216\242\033o' \
         b'\302\206v\203\303+\206n\212'
APP_ADDR = "z1UT9an1Z4W1gnmzASneER2J5eqtx5jfwgx"
APP_DID_TYPE = AbtDid.parse_type_from_did(APP_ADDR)


def response_require_multisig(**kwargs):
    user_did_type = AbtDid.parse_type_from_did(kwargs.get('user_did'))

    claim = {
        'data': forge_utils.multibase_b58encode(
            user_did_type.hasher.hash(
                kwargs.get('tx').SerializeToString())),
        'meta': {
            'description': kwargs.get('description')
        },
        'method': user_did_type.hash_type,
        'origin': helpers.base58_encode_tx(kwargs.get('tx')),
        'type': "signature",
    }

    return response([claim], **kwargs)


def response_require_asset(**kwargs):
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
    chain_info = forge_rpc.get_chain_info().info
    extra = {
        'url': kwargs.get('url'),
        'action': kwargs.get('action'),
        'appInfo': {
            'chainHost': 'http://{0}:{1}/api'.format(config.app_host,
                                                     config.forge_port),
            'chainId': chain_info.network,
            'chainVersion': chain_info.version,
            'chain_token': 'TBA',
            'decimals': 16,
            'description': 'Create and join events on Event Chain',
            'icon': "http://did-workshop.arcblock.co:5000/static/images"
                    "/eventchain.png",
            'name': 'Event Chain',
            'subtitle': 'A decentralized solution for events',
        },
        'requestedClaims': claims,
        'workflow': {
            'description': kwargs.get('workflow')
        }
    }
    res = {
        'appPk': forge_utils.multibase_b58encode(APP_PK),
        'authInfo': APP_DID_TYPE.gen_and_sign(APP_SK, extra)
    }

    return json.dumps(res)
