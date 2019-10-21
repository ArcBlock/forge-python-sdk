from forge_sdk import ForgeConn, utils
from uuid import uuid4
import json

forge = ForgeConn()

def create_users():
    w1 = forge.create_wallet(moniker="alice", passphrase='abcd1234')
    w2 = forge.create_wallet(moniker="bobby", passphrase='abcd1234')
    w3 = forge.create_wallet(moniker="claire", passphrase='abcd1234')
    return w1.wallet, w2.wallet, w3.wallet


def create_asset(owner):
    old_laptop = json.dumps({'name': 'old laptop', 'serial': str(uuid4())})
    data = utils.to_any(old_laptop)
    res, addr = forge.create_asset(data=data, wallet=owner)
    assert res.code == 0
    return addr