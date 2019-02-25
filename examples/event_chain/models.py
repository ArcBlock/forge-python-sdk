import logging
from time import sleep

from google.protobuf.any_pb2 import Any

from examples.event_chain import helpers
from examples.event_chain import protos as protos
from forge import ForgeSdk
from forge import Signer
from forge import utils

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('ec-models')
forgeRpc = ForgeSdk().rpc


def wait():
    sleep(6)


def is_asset_exist(address):
    state = forgeRpc.get_single_asset_state(address)
    return True if state else False


def gen_ticket_token(id, wallet):
    signer = Signer()
    ticket_info = protos.TicketInfo(id=id)
    token = signer.sign(ticket_info.SerializeToString(), wallet.sk)
    return token


def create_asset_ticket_info(id, event_address, expire_time):
    ticket_info = protos.TicketInfo(
        id=id, event_address=event_address,
        is_used=False,
    )
    ticket_itx = protos.CreateAssetTx(
        data=utils.encode_to_any(
            'ec:s:ticket',
            ticket_info,
        ),
        readonly=True,
        expired_at=expire_time,
    )
    return ticket_itx


def gen_exchange_tx(value, ticket_address, event_address):
    receiver = protos.ExchangeInfo(
        value=protos.BigUint(value=bytes(value)),
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
        self.description = kwargs.get('description', 'No description :(')
        self.type_url = 'ec:s:event_info'
        self.address = self.create()
        self.update_generated_tickets()

    def create(self):
        logger.debug("Creating event...")
        event_info = protos.EventInfo(
            title=self.title,
            total=self.total,
            start_time=self.start_time,
            end_time=self.end_time,
            ticket_price=self.ticket_price,
            tickets=[],
            participants=[],
            remaining=self.total,
        )
        create_asset_itx = protos.CreateAssetTx(
            data=utils.encode_to_any(self.type_url, event_info),
        )
        event_address = forgeRpc.get_asset_address(
            sender_address=self.wallet.address,
            itx=create_asset_itx,
            wallet_type=self.wallet.type,
        ).asset_address
        res = forgeRpc.create_asset(
            self.type_url, event_info, self.wallet,
            self.token,
        )
        if res.code != 0:
            logger.error(res)
        logger.info(
            "Event '{}' has been created successfully!".format(
                self.title,
            ),
        )
        # wait()
        # update_hosted_itx = protos.UpdateHostedTx(address=event_address)
        # res = forgeRpc.send_itx(
        #         'ec:t:update_hosted', update_hosted_itx,
        #         self.wallet, self.token,
        # )
        # if res.code != 0:
        #     logger.error(res)
        # logger.debug("Sender hosted events has been updated!")
        return event_address

    def gen_tickets(self):
        tickets = []
        logger.info("Generating tickets for event '{}...".format(self.title))
        for ticket_id in range(1, self.total + 1):
            ticket_holder = self.gen_ticket_holder(ticket_id)
            tickets.append(ticket_holder)
        logger.info(
            "All {} tickets have been generated successfully!".format(
                self.total,
            ),
        )
        return tickets

    def gen_ticket_holder(self, ticket_id):
        create_asset_ticket = create_asset_ticket_info(
            ticket_id,
            self.address,
            self.end_time,
        )

        ticket__address = forgeRpc.get_asset_address(
            sender_address=self.wallet.address,
            itx=create_asset_ticket,
            wallet_type=self.wallet.type,
        ).asset_address
        ticket_create_tx = forgeRpc.create_tx(
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
        ticket_exchange_tx = forgeRpc.create_tx(
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
        tickets = self.gen_tickets()
        # TODO: interface to initialize event_info
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
        )
        res = forgeRpc.update_asset(
            self.type_url,
            self.address,
            event_info,
            self.wallet,
            self.token,
        )
        assert (res.code == 0)
        logger.debug("Event has been updated with generated tickets. ")
        logger.info("Event {} is ready!".format(self.title))


class EventAssetState:
    def __init__(self, asset_state):
        self.address = asset_state.address
        self.owner = asset_state.owner
        self.moniker = asset_state.moniker
        self.readonly = asset_state.readonly
        self.activated = asset_state.activated
        self.expired_at = asset_state.expired_at
        self.context = asset_state.context
        self.stake = asset_state.stake
        self.event_info = utils.parse_to_proto(
            asset_state.data.value,
            protos.EventInfo,
        )
        self.remaining = self.event_info.remaining
        self.tickets = self.event_info.tickets
        self.participants = self.event_info.participants

    def get_next_ticket(self):
        if len(self.tickets) > 0:
            return self.tickets[0]
        else:
            logger.error("No tickets left!")

    def create_ticket(self):
        ticket_holder = self.get_next_ticket()
        create_tx = ticket_holder.ticket_create
        res = forgeRpc.send_tx(create_tx)
        logger.debug("About to create ticket with ticketInfo: {info}".format(
            info=utils.data_of_create_asset(
                create_tx,
                protos.TicketInfo,
            ),
        ))
        logger.debug("executing-ticket: ticket_create_tx has been sent.")
        if res.code != 0:
            logger.error(res)
            logger.error('Error ticket tx: {tx}'.format(tx=create_tx))
            assert (res.code == 0)

    def exchange_ticket(self, buyer_wallet, buyer_token):
        ticket_holder = self.get_next_ticket()
        exchange_tx = ticket_holder.ticket_exchange
        buyer_signed = forgeRpc.multisig(
            exchange_tx, buyer_wallet,
            buyer_token,
        ).tx
        res = forgeRpc.send_tx(buyer_signed)
        logger.debug("executing-ticket: ticket_exchange_tx has been sent.")
        if res.code != 0:
            logger.error(res)

    def update_token(self, buyer_wallet, buyer_token=''):
        next_ticket = self.get_next_ticket()
        ticket_info = protos.TicketInfo(
            id=next_ticket.id,
            token=gen_ticket_token(
                next_ticket.id,
                buyer_wallet,
            ),
        )
        res = forgeRpc.update_asset(
            'ec:s:ticket_info', next_ticket.address,
            ticket_info,
            buyer_wallet, buyer_token,
        )
        logger.debug(
            "executing-ticket: ticket has been updated with the new "
            "token.",
        )
        if res.code != 0:
            logger.error(res)

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
        forgeRpc.update_asset(
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
            ticket_price=self.event_info.ticket_price,
            remaining=self.remaining,
            tickets=self.tickets,
            participants=self.participants,
        )
        state = protos.AssetState(
            address=self.address,
            owner=self.owner,
            moniker=self.moniker,
            readonly=self.readonly,
            activated=self.activated,
            expired_at=self.expired_at,
            stake=self.stake,
            context=self.context,
            data=utils.encode_to_any(
                'ec:s:event_info',
                event_info,
            ),
        )
        return state

    def execute_next_ticket_holder(self, buyer_wallet, buyer_token):
        next_ticket = self.get_next_ticket()
        if len(self.tickets) < 1:
            logger.error("There is no ticket left for this event!")
        else:
            if not is_asset_exist(next_ticket.address):
                self.create_ticket()
            self.exchange_ticket(buyer_wallet, buyer_token)
            logger.debug("Update_Event itx has been sent.")

    def buy_ticket(self, wallet, token):
        logger.info("User {user} is buying ticket {address}".format(
            address=self.get_next_ticket().address,
            user=wallet.address,
        ))
        self.execute_next_ticket_holder(wallet, token)
        logger.info(
            "Ticket {} is bought successfully.".format(wallet.address),
        )
        return self.get_next_ticket().address

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
        self.context = asset_state.context
        self.activated = asset_state.activated
        self.expired_at = asset_state.expired_at
        self.stake = asset_state.stake

        self.ticket_info = utils.parse_to_proto(
            asset_state.data.value,
            protos.TicketInfo,
        )
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
            activated=self.activated,
            expired_at=self.expired_at,
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

    def gen_activate_asset_tx(self, wallet, token):
        itx = utils.encode_to_any(
            'fg:t:activate_asset',
            protos.ActivateAssetTx(address=self.address),
        )
        res = forgeRpc.create_tx(itx, wallet.address, wallet, token)
        logger.debug(
            "ticket_activate tx is generated successfully "
            "for ticket {}".format(self.address),
        )
        if res.code != 0:
            logger.error(res)
        return res.tx

    def activate(self):
        self.is_used = True
        self.activated = True


class User:
    def __init__(self, moniker, passphrase, address=None):
        self.moniker = moniker
        self.passphrase = passphrase
        if not address:
            self.wallet, self.token = self.__init_wallet()
            self.address = self.wallet.address
            self.account_state = None
        else:
            self.address = address
            self.wallet = None
            self.token = None
            self.account_state = None
            self.refresh()

    def declare(self):
        res = self.__declare_wallet()
        self.token = res.token
        wait()
        self.account_state = self.__get_state()

    def __init_wallet(self):
        res = forgeRpc.create_wallet(passphrase=self.passphrase)
        return res.wallet, res.token

    def __declare_wallet(self):
        res = forgeRpc.recover_wallet(
            passphrase=self.passphrase,
            moniker='EC{}'.format(self.moniker),
            data=self.wallet.sk,
        )
        if not res.code == 0:
            print(res)
        return res

    def __get_state(self):
        state = forgeRpc.get_single_account_state(self.address)
        return ParticipantAccountState(state)

    def refresh(self):
        res = forgeRpc.load_wallet(
            address=self.address, passphrase=self.passphrase,
        )
        self.token = res.token
        self.wallet = res.wallet
        self.account_state = self.__get_state()
        if not res.code == 0:
            print(res)

    def current_state(self):
        state = get_participant_state(self.address)
        self.account_state = state
        return state


class ParticipantAccountState:

    def __init__(self, state):
        self.balance = state.balance
        self.nonce = state.nonce
        self.num_txs = state.num_txs
        self.address = state.address
        self.pk = state.pk
        self.type = state.type
        self.moniker = state.moniker
        self.context = state.context
        self.migrated_to = state.migrated_to
        self.migrated_from = state.migrated_from
        self.num_assets = state.num_assets
        self.stake = state.stake
        self.pinned_files = state.pinned_files

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

    def add_hosted(self, address):
        self.hosted = helpers.add_to_proto_list(address, self.hosted)

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
    state = forgeRpc.get_single_asset_state(event_address)
    if not state:
        logger.error("Event {} doesn't exist.".format(event_address))
    else:
        return EventAssetState(state)


def get_ticket_state(ticket_address):
    state = forgeRpc.get_single_asset_state(ticket_address)
    if not state:
        logger.error("Ticket {} doesn't exist.".format(ticket_address))
    else:
        return TicketAssetState(state)


def get_participant_state(participant_address):
    state = forgeRpc.get_single_account_state(participant_address)
    if not state:
        logger.error(
            "Participant {} doesn't exist.".format(participant_address),
        )
    else:
        return ParticipantAccountState(state)
