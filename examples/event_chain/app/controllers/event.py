import logging
from datetime import datetime

from event_chain.app import models

from forge_sdk import rpc as forge_rpc

logger = logging.getLogger('controller-event')


def parse_date(str_date):
    logger.debug(str_date)
    data = str_date.split('/')
    return datetime(
        int(data[0]),
        int(data[1]),
        int(data[2]),
    )


def create_event(user, conn=None, **kwargs):
    random_img = 'https://unsplash.it/800/450/'
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
        img_url=kwargs.get('img_url', random_img)
    )
    if event_info.finished and conn:
        logger.debug(
            'Event {} has been added to database!'.format(
                event_info.address,
            ),
        )
    return event_info


def verify_event_address(event_address):
    try:
        state = models.get_event_state(event_address)
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


def get_tx_info(hash):
    info = forge_rpc.get_single_tx_info(hash)
    if info:
        return models.TransactionInfo(info)
