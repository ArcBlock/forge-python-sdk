from datetime import datetime as dt
from datetime import timedelta
from time import sleep

from forge_sdk import ForgeConn
from forge_sdk import protos
from test.lib import create_asset, create_users
from test.lib import validate_response

forge = ForgeConn()

yesterday = str((dt.now() - timedelta(2)).date())
w1, w2, w3 = create_users(forge)
address = create_asset(w1, forge)
sleep(7)


@validate_response
def test_get_forge_stats():
    day_info = protos.ByDay(start_date=yesterday,
                            end_date=yesterday)
    return forge.get_forge_stats(day_info=day_info)


@validate_response
def test_list_transactions():
    return forge.list_transactions()


@validate_response
def test_get_stakes():
    return forge.list_stakes()


@validate_response
def test_get_top_accounts():
    res = forge.list_top_accounts()
    assert res.accounts
    return res


@validate_response
def test_list_asset_transactions():
    return forge.list_asset_transactions(address)


@validate_response
def test_list_blocks():
    return forge.list_blocks()


@validate_response
def test_list_assets():
    res = forge.list_assets(owner_address=w1.address)
    assert (res.assets[0].address == address)
    return res


@validate_response
def test_get_health_status():
    return forge.get_health_status()
