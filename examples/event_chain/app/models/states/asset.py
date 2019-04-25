import base64
import logging

import event_chain.protos as protos
from event_chain.app import models
from event_chain.app import utils
from google.protobuf.any_pb2 import Any

from forge_sdk import rpc as forge_rpc
from forge_sdk.utils import utils as forge_utils

logger = logging.getLogger('model-state-asset')


class TicketAssetState:
    # TODO: All asset should inheir a base asset state class
    def __init__(self, asset_state):
        self.address = asset_state.address
        self.owner = asset_state.owner
        self.moniker = asset_state.moniker
        self.readonly = asset_state.readonly
        self.transferrable = asset_state.transferrable
        self.ttl = asset_state.ttl
        self.consumed_time = asset_state.consumed_time
        self.issuer = asset_state.issuer
        self.context = asset_state.context
        self.stake = asset_state.stake

        self.ticket_info = forge_utils.parse_to_proto(
            asset_state.data.value,
            protos.TicketInfo,
        )

        self.type_url = asset_state.data.type_url
        self.id = self.ticket_info.id
        self.event_address = self.ticket_info.event_address
        self.is_used = self.ticket_info.is_used

    def to_state(self):
        ticket_info = protos.TicketInfo(
            id=self.id,
            event_address=self.event_address,
            is_used=self.is_used,
        )
        state = protos.AssetState(
            address=self.address,
            owner=self.owner,
            moniker=self.moniker,
            readonly=self.readonly,
            transferrable=self.transferrable,
            ttl=self.ttl,
            consumed_time=self.consumed_time,
            stake=self.stake,
            context=self.context,
            data=forge_utils.encode_to_any(
                'ec:s:ticket_info',
                ticket_info,
            ),
        )
        logger.debug("ticket state about to update...")
        logger.debug("ticket_info state: {}".format(ticket_info))
        logger.debug("state: {}".format(state))
        return state

    def consume(self, consume_tx, wallet, token):
        res = forge_rpc.multisig(
            tx=consume_tx,
            wallet=wallet,
            token=token,
            data=Any(
                type_url='fg:x:address',
                value=self.address.encode(),
            ),
        )
        if res.code != 0 or not res.tx:
            logger.error("Fail to multisig consume tx.")
        else:
            return forge_rpc.send_tx(res.tx)

    def consume_mobile(self, consume_tx, address, signature, user_pk):
        multisig_data = forge_utils.encode_to_any(
            'fg:x:address',
            self.address,
        )

        tx = utils.update_tx_multisig(
            tx=consume_tx, signer=address,
            signature=signature,
            pk=user_pk,
            data=multisig_data,
        )
        return forge_rpc.send_tx(tx)


class EventAssetState:
    def __init__(self, asset_state):
        self.address = asset_state.address
        self.owner = asset_state.owner
        self.moniker = asset_state.moniker
        self.readonly = asset_state.readonly
        self.transferrable = asset_state.transferrable
        self.ttl = asset_state.ttl
        self.consumed_time = asset_state.consumed_time
        self.issuer = asset_state.issuer
        self.context = asset_state.context
        self.stake = asset_state.stake

        self.event_info = forge_utils.parse_to_proto(
            asset_state.data.value,
            protos.EventInfo,
        )
        self.type_url = asset_state.data.type_url
        self.remaining = self.event_info.remaining
        self.tickets = self.event_info.tickets
        self.participants = self.event_info.participants
        self.display_start_time = utils.to_display_time(
            self.event_info.start_time,
        )

        # for front end display purpose
        self.display_end_time = utils.to_display_time(
            self.event_info.end_time,
        )
        self.duration = utils.time_diff(
            self.event_info.start_time,
            self.event_info.end_time,
        ).days
        self.display_price = int(self.event_info.ticket_price / 1e+16)

    def get_next_ticket(self):
        if not self.tickets:
            logger.error("Tickets for event {0} was not generated!")
        elif len(self.tickets) > 0:
            return self.tickets[0]
        else:
            logger.error("No tickets left!")

    def create_ticket(self):
        ticket_holder = self.get_next_ticket()
        create_tx = ticket_holder.ticket_create
        res = forge_rpc.send_tx(create_tx)
        logger.debug(u"About to create ticket with ticketInfo: {info}".format(
            info=forge_utils.data_of_create_asset(
                create_tx,
                protos.TicketInfo,
            ),
        ))
        if res.code != 0:
            logger.error(res)
            logger.error(u'Fail to create ticket: {tx}'.format(tx=create_tx))
        return res.hash

    def exchange_ticket(self, buyer_wallet, buyer_token):
        ticket_holder = self.get_next_ticket()
        exchange_tx = ticket_holder.ticket_exchange
        res1 = forge_rpc.multisig(
            tx=exchange_tx,
            wallet=buyer_wallet,
            token=buyer_token,
        )
        if res1.code != 0:
            logger.error("Buyer multisig failed!")
            logger.error(res1)
            logger.error(exchange_tx)
        else:
            buyer_signed = res1.tx
            res = forge_rpc.send_tx(buyer_signed)
            if res.code != 0:
                logger.error(res)
                return None
            else:
                logger.debug(
                    u"Ticket {} has been exchanged.".format(
                        ticket_holder.address,
                    ),
                )
                return res.hash

    def exchange_ticket_mobile(self, buyer_address, buyer_signature, user_pk):
        logger.debug(u"Preparing to send exchange_tx with mobile data.")
        ticket_holder = self.get_next_ticket()
        exchange_tx = ticket_holder.ticket_exchange
        buyer_signed = utils.add_multi_sig_to_tx(
            exchange_tx,
            buyer_address,
            buyer_signature,
            user_pk
        )
        logger.debug(
            "Buyer multisig kv pair has been inserted into tx "
            "successfully. ",
        )
        logger.debug("url_safe base64 encoded tx: {}".format(
            base64.urlsafe_b64encode(buyer_signed.SerializeToString()),
        ))
        res = forge_rpc.send_tx(buyer_signed)
        if res.code != 0:
            logger.error("Fail to send mobile buyer_signed exchange tx.")
            logger.error(res)
            return None
        else:
            return res.hash

    def update(self, wallet, token, **kwargs):
        event_info = protos.EventInfo(
            title=kwargs.get('title', self.event_info.title),
            start_time=kwargs.get(
                'start_time',
                self.event_info.start_time,
            ),
            end_time=kwargs.get('end_time', self.event_info.end_time),
            ticket_price=kwargs.get(
                'ticket_price',
                self.event_info.ticket_price,
            ),
            description=kwargs.get(
                'description',
                self.event_info.description,
            ),
            tickets=kwargs.get(
                'tickets',
                self.event_info.description,
            ),
            participants=kwargs.get(
                'participants',
                self.event_info.description,
            ),
        )
        forge_rpc.update_asset(
            'ec:s:event_info', self.address, event_info,
            wallet, token,
        )

    def to_state(self):
        event_info = protos.EventInfo(
            title=self.event_info.title,
            description=self.event_info.description,
            total=self.event_info.total,
            start_time=self.event_info.start_time,
            end_time=self.event_info.end_time,
            ticket_price=int(self.event_info.ticket_price),
            remaining=self.remaining,
            tickets=self.tickets,
            participants=self.participants,
            location=self.event_info.location,
            consume_tx=self.event_info.consume_tx,
            img_url=self.event_info.img_url,

        )
        state = protos.AssetState(
            address=self.address,
            owner=self.owner,
            moniker=self.moniker,
            readonly=self.readonly,
            transferrable=self.transferrable,
            ttl=self.ttl,
            consumed_time=self.consumed_time,
            stake=self.stake,
            context=self.context,
            data=forge_utils.encode_to_any(
                'ec:s:event_info',
                event_info,
            ),
        )
        return state

    def execute_next_ticket_holder(self, buyer_wallet, buyer_token):
        ticket = self.get_next_ticket()
        if ticket:
            ticket_address = ticket.address
            if models.is_asset_exist(ticket_address):
                logger.info("Ticket {} already exists.".format(ticket_address))
            else:
                logger.info(
                    "Ticket {} has not been created yet. Creating "
                    "ticket...".format(
                        ticket_address,
                    ),
                )
                self.create_ticket()
            logger.debug("Executing exchange tx...")

            exchange_hash = self.exchange_ticket(buyer_wallet, buyer_token)
            logger.debug("returned exchangeTx hash {}".format(exchange_hash))
            return exchange_hash

    def execute_next_ticket_holder_mobile(
            self, buyer_address,
            buyer_signature, user_pk
    ):
        logger.debug(
            "Executing next ticket holder for event {}".format(
                self.address,
            ),
        )
        logger.debug("mobile buyer address: {}".format(buyer_address))
        logger.debug("mobile buyer signature: {}".format(buyer_signature))
        ticket = self.get_next_ticket()
        ticket_address = None if not ticket else ticket.address
        if not models.is_asset_exist(ticket_address):
            self.create_ticket()

        exchange_hash = self.exchange_ticket_mobile(
            buyer_address,
            buyer_signature, user_pk
        )
        if not exchange_hash:
            logger.error(
                "Fail to process exchange_tx for mobile buy request for "
                "user: {}.".format(buyer_address))
            return ticket_address, None
        else:
            return ticket_address, exchange_hash

    def buy_ticket(self, wallet, token):
        ticket = self.get_next_ticket()
        ticket_address = None if not ticket else ticket.address
        logger.info("User {user} is buying ticket {address}".format(
            address=ticket_address,
            user=wallet.address,
        ))
        exchange_hash = self.execute_next_ticket_holder(
            wallet,
            token,
        )
        if exchange_hash:
            logger.info("Exchange Hash: {}".format(exchange_hash))
            logger.info(
                "Ticket {} is bought successfully.".format(ticket_address),
            )
        else:
            logger.error(
                "Ticket {} exchange TX failed.".format(ticket_address),
            )
        return exchange_hash

    def get_exchange_tx(self):
        ticket = self.get_next_ticket()
        exchange_tx = None if not ticket else ticket.ticket_exchange
        return exchange_tx

    def buy_ticket_mobile(self, buyer_address, buyer_signature, user_pk):
        logger.debug(
            "User {} is buying ticket from mobile.".format(buyer_address),
        )
        ticket_address, exchange_hash = self.execute_next_ticket_holder_mobile(
            buyer_address, buyer_signature, user_pk
        )
        logger.debug(
            "buy_ticket_mobiel is done with addresss{}".format(
                buyer_address),
        )

        return ticket_address, exchange_hash

    def pop_executed_ticket(self):
        logger.debug("Number before pop ticket: {}".format(len(self.tickets)))
        self.tickets = self.tickets[1:]
        self.remaining = self.remaining - 1
        logger.debug("Number after pop ticket: {}".format(len(self.tickets)))
        return self.to_state()
