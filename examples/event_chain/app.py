import logging
from datetime import datetime
from time import sleep

from examples.event_chain import db_helper as db
from examples.event_chain import models
from forge import ForgeSdk

logger = logging.getLogger('ec-app')

forgeSdk = ForgeSdk()
forgeRpc = forgeSdk.rpc


def register_user(name, passphrase, conn=None):
    user = models.User(moniker=name, passphrase=passphrase)
    user.declare()
    logger.info("User {} created successfully!".format(name))
    if conn:
        db.insert_user(conn, user.address, name, passphrase)
    return user


def get_user_from_info(user_info):
    return models.User(
        user_info['moniker'], user_info['passphrase'],
        address=user_info['address'],
    )


def create_event(user_info, conn=None, **kwargs):
    user = get_user_from_info(user_info)
    event_info = models.EventInfo(
        wallet=user.wallet,
        token=user.token,
        title=kwargs.get('title'),
        total=kwargs.get('total'),
        description=kwargs.get('description'),
        start_time=kwargs.get('start_time'),
        end_time=kwargs.get('end_time'),
        ticket_price=kwargs.get('ticket_price'),
    )
    if conn:
        db.insert_event(conn, event_info.address, user.address)
        logger.debug(
            'Event {} has been added to database!'.format(
                event_info.address,
            ),
        )
    return event_info.address


def list_events(conn):
    addr_list = db.select_all_events(conn)
    event_states = [get_event_state(addr) for addr in addr_list]
    return event_states


def list_event_detail(addr):
    event = get_event_state(addr)
    event_info = event.event_info
    print("****************************")
    print('Title:', event_info.title)
    print('Address', event.address)
    print('Total Tickets: ', event_info.total)
    print("Created by: ", event.owner)
    print("Remaining ticket number: ", event_info.remaining)


def load_user(name, passphrase, conn=None):
    addr = db.select_user_address(conn, name, passphrase)
    user = models.User(name, passphrase, addr)
    return user


def list_unused_tickets(user_address):
    user_state = get_participant_state(user_address)
    addr_list = user_state.unused
    ticket_states = [get_ticket_state(addr) for addr in addr_list]
    return ticket_states


def get_event_state(event_address):
    return models.get_event_state(event_address)


def get_ticket_state(ticket_address):
    return models.get_ticket_state(ticket_address)


def get_participant_state(address):
    return models.get_participant_state(address)


def buy_ticket(event_address, user_info, conn=None):
    user = get_user_from_info(user_info)
    state = forgeRpc.get_single_asset_state(event_address)
    if not state:
        logger.error("Event doesn't exist.")
    event_asset = models.EventAssetState(state)
    ticket_address = event_asset.buy_ticket(user.wallet, user.token)
    if conn:
        db.insert_ticket(conn, ticket_address, event_address, user.address)
    return


def create_sample_event(user_info, title, conn=None):
    return create_event(
        user_info=user_info,
        conn=conn,
        title=title,
        total=2,
        description='This is a sample event created for demo',
        start_time=datetime(2019, 2, 9, 21),
        end_time=datetime(2019, 2, 10, 23),
        ticket_price=188,
    )


def activate(owner_signed_tx, wallet, token):
    tx = forgeRpc.multisig(owner_signed_tx, wallet, token).tx
    res = forgeRpc.send_tx(tx)
    if res.code != 0:
        logger.error(res)
    logger.info("Ticket has been activated!")
    return res


def refresh():
    sleep(5)
