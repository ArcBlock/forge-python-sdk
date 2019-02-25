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
    # bobb creates an event, alice buys a ticket, frank buys a ticket,
    # alice uses her ticket, checked by frank
    bobb = app.register_user('bobb', 'abcde1234')
    alice = app.register_user('alice', 'abcde1234')
    frank = app.register_user('frank', 'abcde1234')
    logger.info("User registration Done.")

    assert (len(bobb.account_state.hosted) == 0)
    assert (len(alice.account_state.unused) == 0)
    assert (len(alice.account_state.used) == 0)
    assert (len(alice.account_state.participated) == 0)

    event_address = app.create_sample_event(bobb, 'Jay Chou Concert')
    logger.info("Event address is {}".format(event_address))
    app.refresh()

    assert (bobb.current_state().hosted[0] == event_address)

    logger.info("Buying first ticket...")
    ticket1_address = app.buy_ticket(event_address, alice)
    logger.info("First ticket is bought successfully.")
    app.refresh()

    assert (alice.current_state().unused[0] == ticket1_address)
    assert (len(alice.account_state.used) == 0)
    assert (len(alice.account_state.participated) == 0)

    logger.info("Buying second ticket...")
    ticket2_address = app.buy_ticket(event_address, frank)
    logger.info("Second ticket is bought successfully.")
    app.refresh()

    assert (frank.current_state().unused[0] == ticket2_address)
    assert (len(frank.account_state.used) == 0)
    assert (len(frank.account_state.participated) == 0)

    ticket1 = app.get_ticket_state(ticket1_address)
    ticket2 = app.get_ticket_state(ticket2_address)

    assert (ticket1.owner == alice.address)
    assert (ticket2.owner == frank.address)

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
    assert (alice.current_state().used[0] == ticket1.address)
    assert (alice.account_state.participated[0] == event_address)
    assert (len(alice.account_state.unused) == 0)

    logger.info("Ticket is used successfully.")


if __name__ == "__main__":
    test()
