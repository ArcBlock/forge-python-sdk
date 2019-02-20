from time import sleep

import app
import helpers
import models

from forge import ForgeSdk

forgeSdk = ForgeSdk()
rpc = forgeSdk.rpc


def create_concert_event(user):
    event_concert = models.EventInfo(
        title='sundayday las Vegas',
        total=2,
        description='This is a concert for Jay Chou!!!jjjjj!',
        start_time=helpers.gen_timestamp(2019, 2, 9, 21),
        end_time=helpers.gen_timestamp(2019, 2, 10, 23),
        ticket_price=188,
        wallet=user.wallet,
        token=user.token,
    )
    event_concert.create()
    return event_concert.address


def test():
    bobb = app.register_user('bobb')
    alice = app.register_user('alice')
    frank = app.register_user('frank')
    sleep(5)

    event_address = create_concert_event(bobb)

    sleep(5)

    ticket1_address = app.buy_ticket(event_address, alice.wallet, alice.token)
    sleep(5)
    ticket2_address = app.buy_ticket(event_address, frank.wallet, frank.token)
    sleep(5)

    print('bob address', bobb.address)
    print('alice address', alice.address)
    res = rpc.get_single_asset_state(ticket1_address)

    print('ticket1 owner', res.owner)
    print('ticket2 owner', rpc.get_single_asset_state(ticket2_address))


if __name__ == "__main__":
    test()
