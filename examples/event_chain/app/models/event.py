import logging
from time import sleep

import event_chain.protos as protos
from event_chain.app import utils
from event_chain.app.models.states.asset import EventAssetState
from google.protobuf.any_pb2 import Any

from forge_sdk import did
from forge_sdk import rpc as forge_rpc
from forge_sdk.utils import utils as forge_utils

logger = logging.getLogger('model-event')


def get_event_state(event_address):
    if event_address:
        state = forge_rpc.get_single_asset_state(event_address)
        if not state:
            logger.error("Event {} doesn't exist.".format(event_address))
        else:
            return EventAssetState(state)


def wait():
    sleep(6)


def is_asset_exist(address):
    state = forge_rpc.get_single_asset_state(address)
    return True if state else False


def create_asset_ticket_info(id, event_address):
    ticket_info = protos.TicketInfo(
        id=id, event_address=event_address,
        is_used=False,
    )
    ticket_itx = protos.CreateAssetTx(
        data=forge_utils.encode_to_any(
            'ec:s:ticket_info',
            ticket_info,
        ),
        readonly=True,
    )
    return ticket_itx


def gen_exchange_tx(value, ticket_address, event_address):
    receiver = protos.ExchangeInfo(
        value=protos.BigUint(value=forge_utils.int_to_bytes(int(value))),
    )
    sender = protos.ExchangeInfo(assets=[ticket_address])
    exchange_tx = protos.ExchangeTx(
        sender=sender,
        receiver=receiver,
        data=Any(
            type_url='ec:x:event_address',
            value=event_address.encode(),
        ),
    )
    return exchange_tx


class EventInfo:
    def __init__(self, wallet, token, **kwargs):
        self.wallet = wallet
        self.token = token

        self.title = kwargs.get('title')
        self.total = kwargs.get('total')
        self.remaining = self.total
        self.start_time = utils.gen_timestamp(kwargs.get('start_time'))
        self.end_time = utils.gen_timestamp(kwargs.get('end_time'))
        self.ticket_price = kwargs.get('ticket_price')
        self.location = kwargs.get('location')
        self.description = kwargs.get('description', 'No description :(')
        self.type_url = 'ec:s:event_info'
        self.consume_tx = self.gen_consume_tx()
        self.img_url = kwargs.get('img_url')
        self.address = self.create()
        self.finished = self.update_generated_tickets()

    def gen_consume_tx(self):
        consume_itx = protos.ConsumeAssetTx(issuer=self.wallet.address)
        res = forge_rpc.create_tx(
            itx=forge_utils.encode_to_any(
                'fg:t:consume_asset',
                consume_itx,
            ),
            from_address=self.wallet.address,
            wallet=self.wallet,
            token=self.token,
        )
        if res.code != 0 or res.tx is None:
            logger.error(u'Fail to generate consume tx for event.')
            return None
        else:
            logger.debug(
                u"Consume tx generated for event {}".format(self.title),
            )
            return res.tx

    def create(self):
        logger.debug(u"Creating event...")
        if not self.consume_tx:
            logger.error(u"Consume tx not generated!")
        event_info = protos.EventInfo(
            title=self.title,
            total=self.total,
            start_time=self.start_time,
            end_time=self.end_time,
            ticket_price=self.ticket_price,
            location=self.location,
            tickets=[],
            participants=[],
            remaining=self.total,
            consume_tx=self.consume_tx,
            img_url=self.img_url,
        )
        create_asset_itx = protos.CreateAssetTx(
            data=forge_utils.encode_to_any(self.type_url, event_info),
        )
        event_address = did.get_asset_address(
            did_address=self.wallet.address,
            itx=create_asset_itx)
        logger.debug(
            u"Event address has been calculated: {}".format(event_address),
        )
        res = forge_rpc.create_asset(
            self.type_url, event_info, self.wallet,
            self.token,
        )
        if res.code != 0 or not res.hash:
            logger.error(res)
        else:
            logger.info(
                u"Event '{0}' has been created successfully by tx {"
                "1}!".format(
                    self.title, res.hash,
                ),
            )
            return event_address

    def gen_tickets(self):
        tickets = []
        logger.info("Generating tickets for event '{}...".format(self.title))
        for ticket_id in range(1, self.total + 1):
            ticket_holder = self.gen_ticket_holder(ticket_id)
            tickets.append(ticket_holder)
        logger.info(
            u"All {} tickets have been generated successfully!".format(
                self.total,
            ),
        )
        return tickets

    def gen_ticket_holder(self, ticket_id):
        create_asset_ticket = create_asset_ticket_info(
            ticket_id,
            self.address,
        )

        ticket__address = did.get_asset_address(
            did_address=self.wallet.address,
            itx=create_asset_ticket,
        )
        ticket_create_tx = forge_rpc.create_tx(
            itx=forge_utils.encode_to_any(
                type_url='fg:t:create_asset',
                data=create_asset_ticket,
            ),
            from_address=self.wallet.address,
            token=self.token,
        )

        exchange_tx = gen_exchange_tx(
            self.ticket_price, ticket__address,
            self.address,
        )
        ticket_exchange_tx = forge_rpc.create_tx(
            itx=forge_utils.encode_to_any('fg:t:exchange', exchange_tx),
            from_address=self.wallet.address,
            wallet=self.wallet, token=self.token,
        )

        ticket_holder = protos.TicketHolder(
            ticket_create=ticket_create_tx.tx,
            ticket_exchange=ticket_exchange_tx.tx,
            id=ticket_id,
            address=ticket__address,
        )
        return ticket_holder

    def update_generated_tickets(self):
        if not self.address:
            logger.error("No event address available.")
        else:
            tickets = self.gen_tickets()
            event_info = protos.EventInfo(
                title=self.title,
                description=self.description,
                total=self.total,
                tickets=tickets,
                start_time=self.start_time,
                end_time=self.end_time,
                ticket_price=self.ticket_price,
                participants=[],
                remaining=self.total,
                location=self.location,
                consume_tx=self.consume_tx,
                img_url=self.img_url,
            )
            res = forge_rpc.update_asset(
                self.type_url,
                self.address,
                event_info,
                self.wallet,
                self.token,
            )

            logger.debug(u"Event has been updated with generated tickets. ")
            logger.info(u"Event {} is ready!".format(self.title))
            if res.hash:
                return True
            else:
                return False
