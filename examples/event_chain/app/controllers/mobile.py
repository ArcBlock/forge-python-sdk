import logging
from datetime import datetime

from event_chain import protos
from event_chain.app import db
from event_chain.app import models
from event_chain.app import utils
from event_chain.config import config

from forge_sdk import rpc as forge_rpc
from forge_sdk.utils import utils as forge_utils

logger = logging.getLogger('controller-mobile')


def buy_ticket_mobile(event_address, address, signature, user_pk):
    state = models.get_event_state(event_address)
    ticket_address, hash = state.buy_ticket_mobile(
        address, signature, user_pk
    )
    if hash:
        utils.insert_to_sql(db, models.ExchangeHashModel(
            event_address=event_address,
            hash=hash))
    return ticket_address, hash


def consume_ticket_mobile(ticket, consume_tx, address, signature, user_pk):
    res = ticket.consume_mobile(consume_tx, address, signature, user_pk)

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


def gen_poke_tx(address, pk):
    poke_itx = protos.PokeTx(
        date=str(
            datetime.now().date()),
        address='zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz',
    )
    itx = forge_utils.encode_to_any('fg:t:poke', poke_itx)
    params = {
        'from': address,
        'chain_id': config.chain_id,
        'nonce': 0,
        'pk': pk,
        'itx': itx
    }
    return protos.Transaction(**params)


def send_poke_tx(poke_tx, signature):
    complete_tx = utils.update_tx_signature(poke_tx, signature)
    res = forge_rpc.send_tx(complete_tx)
    if res.code != 0:
        logger.error('Fail to send poke tx.')
        logger.error(res)
    else:
        return res.hash
