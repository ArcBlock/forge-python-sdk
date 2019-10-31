import logging
import json
from uuid import uuid4
from forge_sdk import utils


def validate_response(func):
    def inner(*args, **kwargs):
        res = func(*args, **kwargs)
        if res.code != 0:
            logging.error(f'{func.__name__} errors with {res}')
        assert (res.code == 0)
        return res

    return inner

def create_users(forge):
    w1 = forge.create_wallet(moniker="alice")
    w2 = forge.create_wallet(moniker="bobby")
    w3 = forge.create_wallet(moniker="claire")
    return w1, w2, w3


def create_asset(owner, forge):
    old_laptop = json.dumps({'name': 'old laptop',
                             'serial': str(uuid4())})
    data = utils.to_any(old_laptop)
    res = forge.create_asset(data=data, wallet=owner)
    itx = utils.create_asset_itx(data=data)
    address = itx.address
    assert res.code == 0
    return address
