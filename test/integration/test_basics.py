import json
from time import sleep
from uuid import uuid4

from forge_sdk import utils
from test.integration import forge


def create_users():
    w1 = forge.create_wallet(moniker="alice", passphrase='abcd1234')
    w2 = forge.create_wallet(moniker="bobby", passphrase='abcd1234')
    return w1.wallet, w2.wallet


def create_asset(owner):
    old_laptop = json.dumps({'name': 'old laptop', 'serial': str(uuid4())})
    data = utils.to_any(old_laptop)
    res, addr = forge.create_asset(data=data, wallet=owner)
    assert res.code == 0
    return addr


w1, w2 = create_users()
asset1 = create_asset(w1)
asset2 = create_asset(w1)
value = forge.to_unit(55)

sleep(5)


def test_create_users():
    assert w1.address
    assert w1.pk
    assert w1.sk
    assert w2.address


def test_create_asset():
    assert asset1
    asset_state = forge.fetch_asset(asset1)
    data = utils.from_any(asset_state.data)
    assert asset_state.owner == w1.address
    assert data.get('name') == 'old laptop'


def test_update_asset():
    laptop = json.dumps({'name': 'old laptop',
                         'color': 'red',
                         'serial': str(uuid4())})
    data = utils.to_any(laptop)
    res = forge.update_asset(data=data,
                             address=asset1,
                             wallet=w1,
                             commit=True)
    assert res.code == 0
    asset_state = forge.fetch_asset(asset1)
    data = utils.from_any(asset_state.data)
    assert asset_state.owner == w1.address
    assert data.get('color') == 'red'


def test_transfer():
    w2_bal = forge.fetch_balance(w2.address)
    res = forge.transfer(to=w2.address, value=value,
                         wallet=w1, commit=True)
    assert res.code == 0
    assert forge.fetch_balance(w2.address) - w2_bal == value


def test_exchange():
    sender = utils.exchange_info(assets=[asset1])
    receiver = utils.exchange_info(value=20)
    tx = forge.prepare_exchange(sender=sender, receiver=receiver, wallet=w1)
    res = forge.finalize_exchange(tx=tx, wallet=w2, commit=True)
    assert res.code == 0

    asset_state = forge.fetch_asset(asset1)
    assert asset_state.owner == w2.address


def test_consume_asset():
    forge.transfer(to=w2.address, assets=[asset2], wallet=w1, commit=True)
    old_state = forge.fetch_asset(asset2)
    assert old_state.owner == w2.address
    assert old_state.transferrable

    tx = forge.prepare_consume_asset(issuer=w1.address, wallet=w1)
    res = forge.finalize_consume_asset(tx=tx, wallet=w2, data=asset2,
                                       commit=True)
    assert res.code == 0
    new_state = forge.fetch_asset(asset2)
    assert not new_state.transferrable


if __name__ == '__main__':
    test_consume_asset()
