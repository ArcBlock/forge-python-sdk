from time import sleep

from test.lib import validate_response
from test.rpc import forge

w1 = forge.create_wallet(moniker='alice')
w2 = forge.create_wallet(moniker='bobby')
sleep(6)


def test_single_account():
    res = forge.get_account_state({'address': w1.address})
    for r in res:
        assert r.code == 0
        assert r.state.address == w1.address


def test_multiple_account():
    queries = [{'address': w1.address}, {'address': w2.address}]
    res = forge.get_account_state(queries)
    accounts = []
    for r in res:
        assert r.code == 0
        accounts.append(r.state.address)

    assert w1.address in accounts
    assert w2.address in accounts


@validate_response
def test_get_forge_state():
    return forge.get_forge_state()
