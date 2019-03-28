import logging
import os.path as path
from time import sleep

from event_chain.application import app

from forge import ForgeConfig
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
    wait()

    assert (len(bobb.get_state().hosted) == 0)
    assert (len(alice.get_state().unused) == 0)
    assert (len(alice.get_state().used) == 0)
    assert (len(alice.get_state().participated) == 0)

    event_address = app.create_sample_event(bobb, 'Jay Chou Concert')
    logger.info("Event address is {}".format(event_address))
    app.refresh()

    logger.info("Buying first ticket...")
    ticket1_address = app.buy_ticket(event_address, alice)
    logger.info("First ticket is bought successfully.")
    app.refresh()

    assert (alice.get_state().unused[0] == ticket1_address)
    assert (len(alice.get_state().used) == 0)
    assert (len(alice.get_state().participated) == 0)

    logger.info("Buying second ticket...")
    ticket2_address = app.buy_ticket(event_address, frank)
    logger.info("Second ticket is bought successfully.")
    app.refresh()

    assert (frank.get_state().unused[0] == ticket2_address)
    assert (len(frank.get_state().used) == 0)
    assert (len(frank.get_state().participated) == 0)

    ticket1 = app.get_ticket_state(ticket1_address)
    ticket2 = app.get_ticket_state(ticket2_address)

    assert (ticket1.owner == alice.address)
    assert (ticket2.owner == frank.address)

    assert (not ticket1.is_used)
    assert (not ticket1.activated)

    # alice wants to use her ticket for event
    alice_tx = ticket1.gen_activate_asset_tx(alice)
    app.activate(alice_tx, frank)
    logger.info("Ticket has been activated!")
    app.refresh()

    ticket1 = app.get_ticket_state(ticket1_address)
    assert ticket1.is_used
    assert ticket1.activated
    assert (alice.get_state().used[0] == ticket1.address)
    assert (alice.get_state().participated[0] == event_address)
    assert (len(alice.get_state().unused) == 0)

    logger.info("Ticket is used successfully.")


def test_config():
    app_config = path.join(path.dirname(__file__), "config", "forge.toml")
    print(app_config)
    config = ForgeConfig(file_path=app_config)
    print(config.get_app_path())


if __name__ == "__main__":
    test_config()
