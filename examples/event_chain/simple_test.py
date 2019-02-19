from time import sleep

import app
import helpers
import models

from forge import ForgeSdk
from forge import protos

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


test_user = models.DeclaredUser(
    moniker='alice',
    passphrase='abcde1234',
    wallet=protos.WalletInfo(
        type=protos.WalletType(pk=0, hash=1, address=1),
        sk=b'\225u\314\210\006\326_\255\"\336\307\'\027\332\324'
        b'\300pQ\342\203g\256\rH1fy\263\207\255\355\213tw\247\202'
        b'\365\260\252\371Z\210\220\025\241u\265\230\000\337'
        b'\"\240\356\014jMkh\357\032\323g\346\200',
        pk=b'tw\247\202\365\260\252\371Z\210\220\025\241u\265\230'
        b'\000\337\"\240\356\014jMkh\357\032\323g\346\200',
        address="z1kURat74D7WBd2XzJ49rGg5bz5K8EqoDJR",
    ),
    token="dec2d1bcfd8f86e70707ed9aaa0b08ea",
)


def test():
    bobb = app.register_user('bobb')
    alice = app.register_user('alice')
    sleep(5)
    event_address = create_concert_event(bobb)

    sleep(5)
    ticket_address = app.buy_ticket(event_address, alice.wallet, alice.token)
    res = rpc.get_single_asset_state(ticket_address)
    print(res)


if __name__ == "__main__":
    test()
