import logging

from . import protos as protos
from forge import ForgeSdk
from forge import Signer
from forge import utils

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('ec-models')
forgeRpc = ForgeSdk().rpc


def is_asset_exist(address):
    state = forgeRpc.get_single_asset_state(address)
    return True if state else False


def gen_ticket_token(id, wallet):
    signer = Signer()
    ticket_info = protos.TicketInfo(id=id)
    token = signer.sign(ticket_info.SerializeToString(), wallet.sk)
    return token


def create_ticket_itx(id, wallet):
    token = gen_ticket_token(id, wallet)
    ticket = protos.TicketInfo(id=id, token=token)
    ticket_itx = protos.CreateAssetTx(
        data=utils.encode_to_any(
            'ec:s:ticket',
            ticket,
        ),
    )
    return ticket_itx


def gen_exchange_tx(value, asset_address):
    receiver = protos.ExchangeInfo(
        value=protos.BigUint(value=bytes(value)),
    )
    sender = protos.ExchangeInfo(assets=[asset_address])
    exchange_tx = protos.ExchangeTx(
        sender=sender,
        receiver=receiver,
    )
    return exchange_tx


class EventInfo:
    def __init__(self, wallet, token, **kwargs):
        self.wallet = wallet
        self.token = token

        self.title = kwargs.get('title')
        self.total = kwargs.get('total')
        self.remaining = self.total
        self.start_time = kwargs.get('start_time')
        self.end_time = kwargs.get('end_time')
        self.ticket_price = kwargs.get('ticket_price')
        self.description = kwargs.get('description', 'No description :(')
        self.tickets = []
        self.gen_tickets()
        self.participants = []
        # calculate event address
        self.address = ''
        self.type_url = 'ec:s:event_info'

    def create(self):
        event_info = protos.EventInfo(
            title=self.title,
            total=self.total,
            start_time=self.start_time,
            end_time=self.end_time,
            ticket_price=self.ticket_price,
            tickets=self.tickets,
            participants=self.participants,
        )
        create_asset_itx = protos.CreateAssetTx(
            data=utils.encode_to_any(self.type_url, event_info),
        )
        self.address = forgeRpc.get_asset_address(
            sender_address=self.wallet.address,
            itx=create_asset_itx,
            wallet_type=self.wallet.type,
        ).asset_address
        res = forgeRpc.create_asset(
            self.type_url, event_info, self.wallet,
            self.token,
        )
        assert (res.code == 0)
        logger.info(
            "Event '{}' has been created successfully!".format(
                self.title,
            ),
        )
        logger.debug("Event asset address is : {}".format(self.address))
        return res

    def gen_tickets(self):
        logger.info("Generating tickets for event '{}...".format(self.title))
        for ticket_id in range(1, self.total + 1):
            ticket_holder = self.gen_ticket_holder(ticket_id)
            self.tickets.append(ticket_holder)
        logger.info(
            "All {} tickets have been generated properly!".format(
                self.total,
            ),
        )

    def add_participant(self, address):
        self.participants.append(address)

    def gen_ticket_holder(self, ticket_id):
        create_asset_itx = create_ticket_itx(ticket_id, self.wallet)
        asset_address = forgeRpc.get_asset_address(
            sender_address=self.wallet.address,
            itx=create_asset_itx,
            wallet_type=self.wallet.type,
        ).asset_address
        ticket_create_tx = forgeRpc.create_tx(
            itx=utils.encode_to_any(
                type_url='fg:t:create_asset',
                data=create_asset_itx,
            ),
            from_address=self.wallet.address,
            token=self.token,
        )

        exchange_tx = gen_exchange_tx(self.ticket_price, asset_address)
        ticket_exchange_tx = forgeRpc.create_tx(
            itx=utils.encode_to_any(
                type_url='fg:t:exchange',
                data=exchange_tx,
            ),
            from_address=self.wallet.address,
            wallet=self.wallet, token=self.token,
        )

        ticket_holder = protos.TicketHolder(
            ticket_create=ticket_create_tx.tx,
            ticket_exchange=ticket_exchange_tx.tx,
            executed=False,
            id=ticket_id,
            address=asset_address,
        )
        return ticket_holder


class EventAssetState:
    def __init__(self, asset_state):
        self.address = asset_state.address
        self.owner = asset_state.owner
        self.moniker = asset_state.moniker
        self.readonly = asset_state.readonly
        self.context = asset_state.context
        self.stake = asset_state.stake
        self.event_info = utils.parse_to_proto(
            asset_state.data.value,
            protos.EventInfo,
        )
        self.remaining = self.event_info.remaining
        self.tickets = self.event_info.tickets
        self.participants = self.event_info.participants
        self.next_ticket_holder = self.get_next_ticket()

    def get_next_ticket(self):
        if len(self.tickets) > 0:
            return self.tickets[0]
        else:
            logger.error("No tickets left!")

    def create_ticket(self):
        ticket_holder = self.next_ticket_holder
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
        ticket_holder = self.next_ticket_holder
        exchange_tx = ticket_holder.ticket_exchange
        buyer_signed = forgeRpc.multisig(
            exchange_tx, buyer_wallet,
            buyer_token,
        ).tx
        res = forgeRpc.send_tx(buyer_signed)
        logger.debug("executing-ticket:ticket_exchange_tx has been sent.")
        if res.code != 0:
            logger.error(res)

    def update_token(self, buyer_wallet, buyer_token=''):
        ticket_info = protos.TicketInfo(
            id=self.next_ticket_holder.id,
            token=gen_ticket_token(
                self.next_ticket_holder.id,
                buyer_wallet,
            ),
        )
        res = forgeRpc.update_asset(
            'ec:s:ticket_info', self.next_ticket_holder.address,
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
            stake=self.stake,
            context=self.context,
            data=utils.encode_to_any(
                'ec:s:event_info',
                event_info,
            ),
        )
        return state

    def execute_next_ticket_holder(self, buyer_wallet, buyer_token):
        if len(self.tickets) < 1:
            raise ValueError("There is no ticket left for this event!")
        else:
            if not is_asset_exist(self.next_ticket_holder.address):
                self.create_ticket()
            self.exchange_ticket(buyer_wallet, buyer_token)
            self.update_token(buyer_wallet, buyer_token)
            forgeRpc.send_itx(
                'ec:t:update_event',
                protos.UpdateEventTx(address=self.address),
                buyer_wallet,
                buyer_token,
            )
            logger.debug("Update_Event itx has been sent.")

    def buy_ticket(self, wallet, token):
        logger.info("User {user} is buying ticket {address}".format(
            address=self.next_ticket_holder.address,
            user=wallet.address,
        ))
        self.execute_next_ticket_holder(wallet, token)
        logger.info(
            "Ticket {} is bought successfully.".format(wallet.address),
        )
        return self.next_ticket_holder.address

    def pop_executed_ticket(self):
        logger.debug("Number before pop ticket: {}".format(len(self.tickets)))
        self.tickets = self.tickets[1:]
        logger.debug("Number after pop ticket: {}".format(len(self.tickets)))
        return self.to_state()


class TicketAssetState:
    def __init__(self, asset_state):
        self.address = asset_state.address
        self.owner = asset_state.owner
        self.moniker = asset_state.moniker
        self.readonly = asset_state.readonly
        self.context = asset_state.context
        self.stake = asset_state.stake

        self.ticket_info = utils.parse_to_proto(
            asset_state.data.value,
            protos.TicketInfo,
        )
        self.id = self.ticket_info.id
        self.token = self.ticket_info.token
        self.is_used = self.ticket_info.is_used

    def _verify_owner(self, wallet):
        token = gen_ticket_token(self.id, wallet)
        if token == self.token:
            return True
        else:
            return False

    def use(self, wallet, token):
        if self._verify_owner(wallet):
            logger.info("Ticket owner has been verified successfully.")
            self.is_used = True
            self.update(wallet, token)
        else:
            logger.error(
                "Ticket owner verified failed. {user} doesn't not own ticket "
                "{ticket}".format(
                    user=wallet.address,
                    ticket=self.address,
                ),
            )

    def update(self, wallet, token):
        logger.info("Updating ticket state as used...")
        ticket_info = protos.TicketInfo(
            id=self.id,
            token=self.token,
            is_used=self.is_used,
        )
        res = forgeRpc.update_asset(
            'ec:s:ticket',
            self.address, ticket_info, wallet, token,
        )
        logger.info("Ticket state has been changed to used.")
        if (res.code != 0):
            logger.error(res)
        assert (res.code == 0)


class DeclaredUser:
    def __init__(self, moniker, passphrase='abcde1234', wallet=None, token=''):
        self.moniker = moniker
        self.passphrase = passphrase
        if not wallet:
            self.wallet = self.init_wallet()
        else:
            self.wallet = wallet
        self.address = self.wallet.address
        self.sk = self.wallet.sk
        self.token = token

    def declare(self):
        res = self.declare_wallet()
        self.token = res.token

    def init_wallet(self):
        res = forgeRpc.create_wallet(passphrase=self.passphrase)
        return res.wallet

    def declare_wallet(self):
        res = forgeRpc.recover_wallet(
            passphrase=self.passphrase,
            moniker='EC{}'.format(self.moniker),
            data=self.wallet.sk,
        )
        if not res.code == 0:
            print(res)
        return res

    def refresh(self):
        res = forgeRpc.load_wallet(
            address=self.address, passphrase=self.passphrase,
        )
        self.token = res.token
        if not res.code == 0:
            print(res)
