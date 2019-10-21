from time import sleep

from forge_sdk import protos
from test.integration import forge


def create_users():
    w1 = forge.create_wallet(moniker="alice", passphrase='abcd1234')
    w2 = forge.create_wallet(moniker="bobby", passphrase='abcd1234')
    w3 = forge.create_wallet(moniker="claire", passphrase='abcd1234')
    return w1.wallet, w2.wallet, w3.wallet


boss, helper, partner = create_users()

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


if __name__ == '__main__':
    test_revoke_delegate()
