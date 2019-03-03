import logging
from datetime import datetime
from time import sleep

import examples.event_chain.config as config
from . import db_helper as db
from . import helpers
from . import models
from forge import ForgeSdk

logger = logging.getLogger('ec-app')

forgeSdk = ForgeSdk(config=config.forge_config)
forgeRpc = forgeSdk.rpc


def register_user(moniker, passphrase, conn=None):
    user = models.User(moniker, passphrase)
    logger.info("User {} created successfully!".format(moniker))
    if conn:
        db.insert_user(conn, user.address, moniker, passphrase)
    return user


def load_user(moniker, passphrase):
    address = db.select_address_by_moniker(moniker)
    user = models.User(moniker=moniker, passphrase=passphrase, address=address)
    logger.info("User {} loaded successfully!".format(moniker))
    return user


def recover_user(data, passphrase, moniker, conn=None):
    user = models.User(moniker=moniker, passphrase=passphrase, data=data)
    if conn:
        db.insert_user(conn, user.address, moniker, passphrase)
    return user


def get_user_from_info(user_info):
    return models.User(
        user_info['moniker'], user_info['passphrase'],
    )


def create_event(user, conn=None, **kwargs):
    event_info = models.EventInfo(
        wallet=user.get_wallet(),
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


class TransactionInfo:
    def __init__(self, state):
        self.height = state.height
        self.hash = state.hash
        self.tx = state.tx


def get_tx_info(hash):
    info = forgeRpc.get_single_tx_info(hash)
    return TransactionInfo(info)


def get_ticket_exchange_tx(ticket_address, conn):
    row = db.select_ticket_hash(conn, ticket_address)
    hash = row['exchange_hash']
    logger.debug('Exchange hash for ticket {} is {}'.format(
        ticket_address,
        row[
            'exchange_hash'
        ],
    ))
    return get_tx_info(hash)


def list_tickets(conn, user):
    lst = db.select_tickets(conn, owner=user.address)
    logger.debug("Ticket list: {}".format(lst))
    ticket_states = [get_ticket_state(row['address']) for row in lst]
    return ticket_states


def list_unused_tickets(user_address):
    user_state = get_participant_state(user_address)
    addr_list = user_state.unused
    ticket_states = [get_ticket_state(addr) for addr in addr_list]
    return ticket_states


def list_used_tickets(user_address):
    user_state = get_participant_state(user_address)
    addr_list = user_state.used
    ticket_states = [get_ticket_state(addr) for addr in addr_list]
    return ticket_states


def get_event_state(event_address):
    return models.get_event_state(event_address)


def get_ticket_state(ticket_address):
    return models.get_ticket_state(ticket_address)


def get_participant_state(address):
    return models.get_participant_state(address)


def buy_ticket(event_address, user, conn=None):
    state = forgeRpc.get_single_asset_state(event_address)
    if not state:
        logger.error("Event doesn't exist.")
    event_asset = models.EventAssetState(state)
    ticket_address, create_hash, exchange_hash = event_asset.buy_ticket(
        user.get_wallet(), user.token,
    )
    if conn:
        db.insert_ticket(
            conn, ticket_address, event_address, user.address,
            create_hash, exchange_hash,
        )
    return ticket_address


def buy_ticket_mobile(event_address, response, conn=None):
    wallet_response = helpers.WalletResponse(response)
    address = wallet_response.get_address()
    signature = wallet_response.get_signature()
    state = forgeRpc.get_single_asset_state(event_address)
    if not state:
        logger.error("Event doesn't exist.")
    event_asset = models.EventAssetState(state)
    ticket_address, create_hash, exchange_hash = event_asset.buy_ticket_mobile(
        address, signature,
    )
    if conn:
        db.insert_ticket(
            conn, ticket_address, event_address, address,
            create_hash, exchange_hash,
        )
    return ticket_address


def create_sample_event(user, title, conn=None):
    return create_event(
        user=user,
        conn=conn,
        title=title,
        total=20,
        description='This is a sample event created for demo',
        start_time=datetime(2019, 2, 9, 21),
        end_time=datetime(2019, 2, 10, 23),
        ticket_price=188,
    )


def activate(owner_signed_tx, user):
    tx = forgeRpc.multisig(owner_signed_tx, user.get_wallet(), user.token).tx
    res = forgeRpc.send_tx(tx)
    if res.code != 0:
        logger.error(res)
    logger.info("Ticket has been activated!")
    return res


def refresh():
    sleep(5)
