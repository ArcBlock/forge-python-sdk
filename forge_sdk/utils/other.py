import logging

import requests

from forge_sdk import utils as forge_utils

logger = logging.getLogger('forge-util')


def is_response_ok(response):
    if not response:
        logger.error('Response is None.')
        return False
    elif response.code == 0:
        return True
    else:
        logger.error(f'Response is not ok: {response}')


def did_url(url, action, app_pk, app_addr):
    params = {
        'appPk': app_pk,
        'appDid': 'did:abt:' + app_addr,
        'action': action,
        'url': url,
    }
    r = requests.Request('GET', 'https://abtwallet.io/i/',
                         params=params).prepare()

    return r.url
