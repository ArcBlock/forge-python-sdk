from time import sleep

from forge_sdk import protos, utils
from test.integration import forge
from test import lib

boss, helper, partner = lib.create_users(forge)
asset = lib.create_asset(partner, forge)

value = forge.to_unit(50)
sleep(5)


def test_delegate():
    ops = protos.DelegateOp(
            type_url='fg:t:transfer'
    )
    res = forge.delegate(to=helper.address, ops=[ops], wallet=boss,
                         commit=True)
    assert res.code == 0
    boss_bal = forge.fetch_balance(boss.address)
    helper_bal = forge.fetch_balance(helper.address)
    partner_bal = forge.fetch_balance(partner.address)

    res = forge.transfer(to=partner.address,
                         value=value,
                         wallet=helper,
                         delegatee=boss.address,
                         commit=True)

    assert res.code == 0
    assert forge.fetch_balance(boss.address) + value == boss_bal
    assert forge.fetch_balance(partner.address) - partner_bal == value
    assert forge.fetch_balance(helper.address) == helper_bal


def test_revoke_delegate():
    ops = protos.DelegateOp(
            type_url='fg:t:transfer'
    )
    res = forge.delegate(to=helper.address, ops=[ops], wallet=boss,
                         commit=True)
    assert res.code == 0

    res = forge.revoke_delegate(to=helper.address,
                                type_urls=['fg:t:transfer'],
                                wallet=boss)
    assert res.code == 0

    res = forge.transfer(to=partner.address,
                         value=value,
                         wallet=helper,
                         delegatee=boss.address,
                         commit=True)

    assert res.code == 58


def test_delegate_exchange():
    ops = protos.DelegateOp(
            type_url='fg:t:exchange'
    )
    asset_state = forge.fetch_asset(asset)
    boss_bal = forge.fetch_balance(boss.address)
    partner_bal = forge.fetch_balance(partner.address)

    assert asset_state.owner == partner.address
    res = forge.delegate(to=helper.address, ops=[ops], wallet=boss,
                         commit=True)
    assert res.code == 0

    sender = utils.exchange_info(assets=[asset])
    receiver = utils.exchange_info(value=value)
    tx = forge.prepare_exchange(sender=sender, receiver=receiver,
                                wallet=partner)
    res = forge.finalize_exchange(tx=tx, wallet=helper,
                                  delegatee=boss.address, commit=True)
    assert res.code == 0

    new_state = forge.fetch_asset(asset)
    assert new_state.owner == boss.address
    assert forge.fetch_balance(partner.address) - partner_bal == value
    assert forge.fetch_balance(boss.address) + value == boss_bal


if __name__ == '__main__':
    test_delegate_exchange()
