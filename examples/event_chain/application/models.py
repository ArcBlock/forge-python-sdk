import base64
import logging
from datetime import datetime
from time import sleep

import event_chain.protos as protos
import event_chain.utils.helpers as helpers
from google.protobuf.any_pb2 import Any

from forge import Signer
from forge import utils
from forge.rpc import rpc as forge_rpc

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('ec-models')


def wait():
    sleep(6)


def is_asset_exist(address):
    state = forge_rpc.get_single_asset_state(address)
    return True if state else False


def gen_ticket_token(id, wallet):
    signer = Signer()
    ticket_info = protos.TicketInfo(id=id)
    token = signer.sign(ticket_info.SerializeToString(), wallet.sk)
    return token


def create_asset_ticket_info(id, event_address):
    ticket_info = protos.TicketInfo(
        id=id, event_address=event_address,
        is_used=False,
    )
    ticket_itx = protos.CreateAssetTx(
        data=utils.encode_to_any(
            'ec:s:ticket_info',
            ticket_info,
        ),
        readonly=True,
    )
    return ticket_itx


def gen_exchange_tx(value, ticket_address, event_address):
    receiver = protos.ExchangeInfo(
        value=protos.BigUint(value=utils.int_to_bytes(int(value))),
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
        self.start_time = helpers.gen_timestamp(kwargs.get('start_time'))
        self.end_time = helpers.gen_timestamp(kwargs.get('end_time'))
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
            itx=utils.encode_to_any(
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
            data=utils.encode_to_any(self.type_url, event_info),
        )
        event_address = forge_rpc.get_asset_address(
            sender_address=self.wallet.address,
            itx=create_asset_itx,
            wallet_type=self.wallet.type,
        ).asset_address
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

        ticket__address = forge_rpc.get_asset_address(
            sender_address=self.wallet.address,
            itx=create_asset_ticket,
            wallet_type=self.wallet.type,
        ).asset_address
        ticket_create_tx = forge_rpc.create_tx(
            itx=utils.encode_to_any(
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
            itx=utils.encode_to_any('fg:t:exchange', exchange_tx),
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

        self.event_info = utils.parse_to_proto(
            asset_state.data.value,
            protos.EventInfo,
        )
        self.type_url = asset_state.data.type_url
        self.remaining = self.event_info.remaining
        self.tickets = self.event_info.tickets
        self.participants = self.event_info.participants
        self.display_start_time = helpers.to_display_time(
            self.event_info.start_time,
        )

        # for front end display purpose
        self.display_end_time = helpers.to_display_time(
            self.event_info.end_time,
        )
        self.duration = helpers.time_diff(
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
            info=utils.data_of_create_asset(
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
        buyer_signed = helpers.add_multi_sig_to_tx(
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
            data=utils.encode_to_any(
                'ec:s:event_info',
                event_info,
            ),
        )
        return state

    def execute_next_ticket_holder(self, buyer_wallet, buyer_token):
        ticket = self.get_next_ticket()
        if ticket:
            ticket_address = ticket.address
            create_hash = None
            if is_asset_exist(ticket_address):
                logger.info("Ticket {} already exists.".format(ticket_address))
            else:
                logger.info(
                    "Ticket {} has not been created yet. Creating "
                    "ticket...".format(
                        ticket_address,
                    ),
                )
                create_hash = self.create_ticket()
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
        if not is_asset_exist(ticket_address):
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

        self.ticket_info = utils.parse_to_proto(
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
            data=utils.encode_to_any(
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
        multisig_data = helpers.encode_string_to_any(
            'fg:x:address',
            self.address,
        )

        tx = helpers.update_tx_multisig(
            tx=consume_tx, signer=address,
            signature=signature,
            pk=user_pk,
            data=multisig_data,
        )
        return forge_rpc.send_tx(tx)


class User:
    def __init__(self, moniker, passphrase, address=None, data=None):
        self.moniker = moniker
        self.passphrase = passphrase
        if data:
            logger.debug("Recovering wallet for {}".format(moniker))
            self.address, self.wallet, self.token = self.__recover_wallet(
                passphrase, moniker, data,
            )
        elif address:
            logger.debug("Loading wallet for {}".format(moniker))
            self.wallet, self.token = self.__load_wallet(address, passphrase)
            self.address = address
        else:
            logger.debug("creating wallet for {}".format(moniker))
            self.address, self.wallet, self.token = self.__init_wallet()
        logger.debug("wallet: {}".format(self.wallet))
        logger.debug("token: {}".format(self.token))
        logger.debug("address: {}".format(self.address))

    def __recover_wallet(self, passphrase, moniker, data):
        res = forge_rpc.recover_wallet(
            passphrase=passphrase,
            moniker=moniker,
            data=data,
        )
        if res.code != 0:
            logger.error("Recovering wallet failed!")
            logger.error(res)
        return res.wallet.address, res.wallet.SerializeToString(), res.token

    def get_wallet(self):
        wallet = protos.WalletInfo()
        wallet.ParseFromString(self.wallet)
        return wallet

    def __init_wallet(self):
        res = forge_rpc.create_wallet(
            moniker=self.moniker,
            passphrase=self.passphrase,
        )
        if res.code != 0:
            logger.error("Creating wallet failed!")
            logger.error(res)
        return res.wallet.address, res.wallet.SerializeToString(), res.token

    def __load_wallet(self, address, passphrase):
        res = forge_rpc.load_wallet(address, passphrase)
        if res.code != 0:
            logger.error(
                "Reloading wallet failed! Please check your passphrase.",
            )
            logger.error(res)
        return res.wallet.SerializeToString(), res.token

    def get_state(self):
        state = get_participant_state(self.address)
        return state

    def poke(self):
        pokeTx = protos.PokeTx(date=str(datetime.utcnow().date()),
                               address='zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz')
        res = forge_rpc.send_itx(type_url='fg:t:poke',
                                 itx=pokeTx,
                                 wallet=self.get_wallet(),
                                 token=self.token,
                                 nonce=0)

        if res.code != 0:
            logger.error("Poke Failed.")
            logger.error(res)
        else:
            logger.debug('Poke successfully.hash: {}'.format(res.hash))


class ParticipantAccountState:

    def __init__(self, state):
        self.balance = state.balance
        self.nonce = state.nonce
        self.num_txs = state.num_txs
        self.address = state.address
        self.pk = state.pk
        self.type = state.type
        self.moniker = state.moniker
        self.issuer = state.issuer
        self.context = state.context
        self.migrated_to = state.migrated_to
        self.migrated_from = state.migrated_from
        self.num_assets = state.num_assets
        self.stake = state.stake
        self.pinned_files = state.pinned_files

        self.display_balance = utils.bytes_to_int(self.balance.value) / 1e16

        self.participant_info = utils.parse_to_proto(
            state.data.value,
            protos.ParticipantInfo,
        )
        self.hosted = self.participant_info.hosted
        self.participated = self.participant_info.participated
        self.unused = self.participant_info.unused
        self.used = self.participant_info.used

    def to_state(self):
        participant_info = protos.ParticipantInfo(
            hosted=self.hosted,
            participated=self.participated,
            unused=self.unused,
            used=self.used,
        )

        state = protos.AccountState(
            balance=self.balance,
            nonce=self.nonce,
            num_txs=self.num_txs,
            address=self.address,
            pk=self.pk,
            type=self.type,
            moniker=self.moniker,
            issuer=self.issuer,
            context=self.context,
            migrated_to=self.migrated_to,
            migrated_from=self.migrated_from,
            num_assets=self.num_assets,
            stake=self.stake,
            pinned_files=self.pinned_files,
            data=utils.encode_to_any(
                'ec:s:participant_info',
                participant_info,
            ),
        )
        return state

    def add_participated(self, address):
        self.participated = helpers.add_to_proto_list(
            address,
            self.participated,
        )

    def add_unused_ticket(self, address):
        self.unused = helpers.add_to_proto_list(address, self.unused)

    def remove_unused_ticket(self, address):
        self.unused = helpers.remove_from_proto_list(address, self.unused)

    def add_used_ticket(self, address):
        self.used = helpers.add_to_proto_list(address, self.used)


def get_event_state(event_address):
    if event_address:
        state = forge_rpc.get_single_asset_state(event_address)
        if not state:
            logger.error("Event {} doesn't exist.".format(event_address))
        else:
            return EventAssetState(state)


def get_ticket_state(ticket_address):
    state = forge_rpc.get_single_asset_state(ticket_address)
    if not state:
        logger.error("Ticket {} doesn't exist.".format(ticket_address))
    else:
        return TicketAssetState(state)


def get_participant_state(participant_address):
    state = forge_rpc.get_single_account_state(participant_address)
    if not state:
        logger.error(
            "Participant {} doesn't exist.".format(participant_address),
        )
    else:
        return ParticipantAccountState(state)
