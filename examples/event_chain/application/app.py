import logging
from datetime import datetime
from time import sleep

import event_chain.config.config as config
import event_chain.db.utils as db
from event_chain.application import models
from event_chain.utils import helpers

from forge import ForgeSdk

logger = logging.getLogger('ec-app')

forgeSdk = ForgeSdk(config=config.forge_config)
forgeRpc = forgeSdk.rpc


def connect(db_path):
    conn = db.create_connection()
    logger.info("DB connected: {}.".format(db_path))
    return conn


def register_user(moniker, passphrase, conn=None):
    user = models.User(moniker, passphrase)
    logger.info("User {} created successfully!".format(moniker))
    if conn:
        db.insert_user(conn, user.address, moniker, passphrase)
    return user


def load_user(moniker, passphrase, conn=None, address=None):
    address = address if address else db.select_address_by_moniker(
        conn,
        moniker,
    )
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


def parse_date(str_date):
    logger.debug(str_date)
    data = str_date.split('/')
    return datetime(
        int(data[0]),
        int(data[1]),
        int(data[2]),
    )


def create_event(user, conn=None, **kwargs):
    event_info = models.EventInfo(
        wallet=user.get_wallet(),
        token=user.token,
        title=kwargs.get('title'),
        total=int(kwargs.get('total')),
        description=kwargs.get('description'),
        start_time=parse_date(kwargs.get('start_time')),
        end_time=parse_date(kwargs.get('end_time')),
        ticket_price=int(kwargs.get('ticket_price')),
        location=kwargs.get('location'),
    )
    if event_info.finished and conn:
        db.insert_event(conn, event_info.address, user.address)
        logger.debug(
            'Event {} has been added to database!'.format(
                event_info.address,
            ),
        )
    return event_info.address


def list_events(conn):
    addr_list = db.select_all_events(conn)
    event_states = []
    for addr in addr_list:
        state = get_event_state(addr)
        if state:
            event_states.append(state)
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
    logger.debug('ticket list:{}'.format(lst))
    ticket_states = [get_ticket_state(row['address']) for row in lst]
    return ticket_states


def list_unused_tickets(user_address):
    user_state = get_participant_state(user_address)
    if not user_state:
        return []
    else:
        addr_list = user_state.unused
        ticket_states = [
            get_ticket_state(addr) for addr in addr_list if
            get_ticket_state(addr) is not None
        ]
        return ticket_states


def get_event_state(event_address):
    return models.get_event_state(event_address)


def get_ticket_state(ticket_address):
    return models.get_ticket_state(ticket_address)


def get_participant_state(address):
    return models.get_participant_state(address)


def buy_ticket(event_address, user, conn=None):
    event_asset = get_event_state(event_address)
    logger.debug('user wallet: {}'.format(user.get_wallet()))
    logger.debug('user token: {}'.format(user.token))
    ticket_address, create_hash, exchange_hash = event_asset.buy_ticket(
        user.get_wallet(), user.token,
    )
    logger.debug("Tick is bought. create hash:{}, exchange hash{}".format(
        create_hash, exchange_hash,
    ))
    if ticket_address and conn:
        db.insert_ticket(
            conn, ticket_address, event_address, user.address,
            create_hash, exchange_hash,
        )
        return ticket_address
    else:
        return None


def buy_ticket_mobile(event_address, address, signature):
    # wallet_response = helpers.WalletResponse(response)
    # address = wallet_response.get_address()
    # logger.debug('mobile wallet address:{}'.format(address))
    #
    # signature = wallet_response.get_signature()
    # logger.debug('mobile wallet signature:{}'.format(signature))
    state = get_event_state(event_address)
    ticket_address = state.buy_ticket_mobile(
        address, signature,
    )
    return ticket_address


def get_wallet_address(response):
    wallet_response = helpers.WalletResponse(response)
    address = wallet_response.get_address()
    return address


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


def consume(ticket_address, user):
    logger.debug("Consuming ticket {}".format(ticket_address))
    ticket = get_ticket_state(ticket_address)
    logger.debug("Event is  {}".format(ticket.ticket_info.event_address))
    consume_tx = get_event_state(
        ticket.ticket_info.event_address,
    ).event_info.consume_tx
    if not consume_tx:
        return None

    logger.debug("consume tx: {}".format(consume_tx))

    res = ticket.consume(consume_tx, user.get_wallet(), user.token)

    if res.code != 0 or res.hash is None:
        logger.error(res)
        logger.error('Fail to consume ticket {}'.format(ticket_address))
    else:
        logger.info(
            "ConsumeTx has been sent by tx: {}!".format(res.hash),
        )
    return res.hash


def consume_ticket_mobile(ticket, consume_tx, address, signature):
    res = ticket.consume_mobile(consume_tx, address, signature)

    if res.code != 0 or res.hash is None:
        logger.error(res)
        logger.error(
            'Fail to consume ticket by mobile {}'.format(ticket.address),
        )
    else:
        logger.info("Mobile ConsumeTx has been sent by tx: {}!".format(
            res.hash,
        ))
    return res.hash


def list_ticket_exchange_tx(event_address):
    res = forgeRpc.list_asset_transactions(event_address)
    if res.code != 0:
        logger.error(
            "Fail to get transactions for event {}".format(event_address),
        )
        logger.error(res)
        return []
    elif len(res.transactions) == 0:
        logger.debug("rpc returned Empty exchange txs for event {}".format(
            event_address,
        ))
        return []
    else:
        return [tx for tx in res.transactions if tx.type == 'exchange']


def verify_event_address(event_address):
    try:
        state = get_event_state(event_address)
    except Exception:
        logger.error('exception in verifying event_address ')
        raise TypeError("{} is not an event address.".format(event_address))
    if not state:
        logger.error('Event {} does not exist.'.format(event_address))
        raise ValueError('Event {} does not exist'.format(event_address))
    if state.type_url != 'ec:s:event_info':
        logger.error(
            'This asset should be type ec:s:event_info, but provided '
            'type_url is : {}'.format(
                state.type_url,
            ),
        )
        raise ValueError(
            '{} is not a valid event address. Type_url for this asset '
            'is {}'.format(
                event_address, state.type_url,
            ),
        )


def verify_ticket_address(ticket_address):
    try:
        state = get_ticket_state(ticket_address)
    except Exception:
        logger.error('Error in checking ticket')
        raise TypeError("{} is not an ticket address.".format(ticket_address))

    if not state:
        logger.error(u'Ticket {} does not exist.'.format(ticket_address))
        raise ValueError('Ticket {} does not exist'.format(ticket_address))
    if state.type_url != 'ec:s:ticket_info':
        logger.error('This asset type should be ec:s:ticket_info,'
                     ' but the provided url is: {}'.format(state.type_url))
        raise ValueError(
            '{} is not a valid ticket address. Type_url for this asset '
            'is {}'.format(
                ticket_address, state.type_url,
            ),
        )


def refresh():
    sleep(5)
