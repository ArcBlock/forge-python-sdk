import logging
import sys
from time import sleep

from . import app
from . import helpers
from . import models
from forge import ForgeSdk

forgeSdk = ForgeSdk()
rpc = forgeSdk.rpc
logger = logging.getLogger("Flow-Test")


def wait():
    sleep(5)


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
    logger.info("User registration Done.")
    wait()

    event_address = create_concert_event(bobb)
    wait()

    logger.info("Buying first ticket...")
    ticket1_address = app.buy_ticket(event_address, alice.wallet, alice.token)
    logger.info("First ticket is bought successfully.")
    wait()

    logger.info("Buying second ticket...")
    ticket2_address = app.buy_ticket(event_address, frank.wallet, frank.token)
    logger.info("Second ticket is bought successfully.")
    wait()

    ticket1_state = rpc.get_single_asset_state(ticket1_address)
    ticket2_state = rpc.get_single_asset_state(ticket2_address)

    assert (ticket1_state.owner == alice.address)
    assert (ticket2_state.owner == frank.address)

    ticket1 = app.get_ticket(ticket1_address)
    assert (not ticket1.is_used)
    app.use_ticket(ticket1_address, alice.wallet, alice.token)
    wait()
    ticket1 = app.get_ticket(ticket1_address)
    assert (ticket1.is_used)
    logger.info("Ticket is used successfully.")


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    test()
