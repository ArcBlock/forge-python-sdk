import logging
from time import sleep

from . import app
from forge import ForgeSdk

logging.basicConfig(level=logging.DEBUG)
forgeSdk = ForgeSdk()
rpc = forgeSdk.rpc
logger = logging.getLogger("Test")


def wait():
    sleep(5)


def test():
    bobb = app.register_user('bobb', 'abcde1234')
    alice = app.register_user('alice', 'abcde1234')
    frank = app.register_user('frank', 'abcde1234')
    logger.info("User registration Done.")
    app.refresh()

    event_address = app.create_sample_event(bobb, 'Jay Chou Concert')
    app.refresh()

    logger.info("Buying first ticket...")
    ticket1_address = app.buy_ticket(event_address, alice)
    logger.info("First ticket is bought successfully.")
    app.refresh()

    logger.info("Buying second ticket...")
    ticket2_address = app.buy_ticket(event_address, frank)
    logger.info("Second ticket is bought successfully.")
    app.refresh()

    ticket1_state = rpc.get_single_asset_state(ticket1_address)
    ticket2_state = rpc.get_single_asset_state(ticket2_address)

    assert (ticket1_state.owner == alice.address)
    assert (ticket2_state.owner == frank.address)

    ticket1 = app.get_ticket_state(ticket1_address)
    assert (not ticket1.is_used)
    assert (not ticket1.activated)

    # alice wants to use her ticket for event
    alice_tx = ticket1.gen_activate_asset_tx(alice.wallet, alice.token)
    app.activate(alice_tx, frank.wallet, frank.token)
    logger.info("Ticket has been activated!")
    app.refresh()
    ticket1 = app.get_ticket_state(ticket1_address)
    assert ticket1.is_used
    assert ticket1.activated
    logger.info("Ticket is used successfully.")


if __name__ == "__main__":
    test()
