import logging
from datetime import datetime

from event_chain import protos
from event_chain.app import db
from event_chain.app import models
from event_chain.app import utils
from event_chain.config import config

from forge_sdk import rpc as forge_rpc
from forge_sdk.utils import utils as forge_utils

logger = logging.getLogger('controller-ticket')


def list_unused_tickets(user_address):
    user_state = models.get_participant_state(user_address)
    if not user_state:
        return []
    else:
        addr_list = user_state.unused
        ticket_states = [
            models.get_ticket_state(addr) for addr in addr_list if
            models.get_ticket_state(addr) is not None
        ]
        return ticket_states


def buy_ticket(event_address, user, conn=None):
    event_asset = models.get_event_state(event_address)
    logger.debug('user wallet: {}'.format(user.get_wallet()))
    logger.debug('user token: {}'.format(user.token))
    exchange_hash = event_asset.buy_ticket(
        user.get_wallet(), user.token,
    )
    logger.debug("Buy ticket process is completed. exchange hash{}".format(
        exchange_hash,
    ))
    if exchange_hash and conn:
        db.insert_exchange_tx(conn, event_address, exchange_hash)
    return exchange_hash


def consume(ticket_address, user):
    logger.debug("Consuming ticket {}".format(ticket_address))
    ticket = models.get_ticket_state(ticket_address)
    logger.debug("Event is  {}".format(ticket.ticket_info.event_address))
    consume_tx = models.get_event_state(
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


def verify_ticket_address(ticket_address):
    try:
        state = models.get_ticket_state(ticket_address)
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
