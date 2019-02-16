from google.protobuf.timestamp_pb2 import Timestamp

from . import protos
from .simulators import forgeSdk
from forge import Signer
from forge import utils

forgeRpc = forgeSdk.rpc


def gen_ticket_token(id, wallet):
    token = Signer().sign(protos.TicketInfo(id=id), wallet.sk)
    return token


def create_ticket_itx(id, wallet, tx=None):
    token = gen_ticket_token(id, wallet)
    ticket = protos.TicketInfo(id=id, token=token, tx=tx)
    ticket_itx = protos.CreateAssetTx(
        data=utils.encode_to_any(
            'ec:t:ticket',
            ticket,
        ),
    )
    return ticket_itx


def to_google_timestamp(timestamp):
    return Timestamp(timestamp)


def gen_exchange_tx(value, asset_address, wallet, token):
    receiver = protos.ExchangeInfo(
        value=protos.BigUint(value=value.to_bytes()),
    )
    sender = protos.ExchangeInfo(assets=[asset_address])
    exchange_tx = protos.ExchangeTx(sender=sender, receiver=receiver)
    res = forgeRpc.create_tx(
        itx=exchange_tx, from_address=wallet.address,
        token=token,
    )
    if res.code == 0:
        return exchange_tx


class Event:
    def __init__(self, wallet, token, **kwargs):
        self.wallet = wallet
        self.token = token

        self.title = kwargs.get('title')
        self.total = kwargs.get('total')
        self.start_time = kwargs.get('start_time')
        self.end_time = kwargs.get('end_time')
        self.ticket_price = kwargs.get('ticket_price', 0)
        self.description = kwargs.get('description', 'No description :(')
        self.tickets = []
        self.gen_tickets()
        self.participants = []

    def create(self):
        event_info = protos.EventInfo(
            title=self.title,
            total=self.total,
            start_time=to_google_timestamp(self.start_time),
            end_time=to_google_timestamp(self.end_time),
            ticket_price=self.ticket_price,
            tickets=self.tickets,
            participants=self.participants,
        )
        forgeRpc.create_asset(
            'ec:t:event_info', event_info, self.wallet,
            self.token,
        )

    def gen_tickets(self):
        for ticket_id in range(self.total):
            ticket_holder = self.gen_ticket_holder(ticket_id)
            self.tickets.append(ticket_holder)

    def add_participant(self, address):
        # do we limit here?
        self.participants.append(address)

    def gen_ticket_holder(self, ticket_id):
        create_asset_itx = create_ticket_itx(ticket_id, self.wallet)
        asset_address = utils.to_asset_address(
            self.wallet.address,
            create_asset_itx,
        )
        ticket_create_tx = forgeRpc.create_tx(
            itx=create_asset_itx,
            from_address=self.wallet.address,
            token=self.token,
        )

        exchange_tx = gen_exchange_tx(self.ticket_price, asset_address)
        ticket_exchange_tx = forgeRpc.create_tx(
            itx=exchange_tx,
            from_address=self.wallet.address,
            wallet=self.wallet, token=self.token,
        )

        ticket_holder = protos.TicketHolder(
            ticket_create=ticket_create_tx,
            ticket_exchange=ticket_exchange_tx,
        )
        return ticket_holder


class EventAssetState:
    def __init__(self, asset_state):
        self.address = asset_state.address
        self.owner = asset_state.owner
        self.moniker = asset_state.moniker
        self.read_only = asset_state.read_only
        self.context = asset_state.context
        self.stake = asset_state.stake
        self.event_info = utils.parse_to_proto(
            asset_state.data.value,
            protos.EventInfo,
        )

        self.tickets = list(self.event_info.tickets)
        self.participants = list(self.event_info.participants)

    def execute_next_ticket(self, buy_wallet):
        if len(self.tickets) < 1:
            raise ValueError("There is not ticket left for this event!")
        else:
            self.create_ticket()
            self.exchange_ticket()
            self.update_token()
            tx = utils.parse_to_proto(self.tickets[0], protos.Transaction)
            # ticket_creation
            res = forgeRpc.send_tx(tx)
            if res.code == 0:
                self.tickets = self.tickets[1:]
                self.update()
            # exchange_tx and multisig
            # itx = utils.parse_to_proto(tx.itx.value, protos.CreateAssetTx)
            # ticket_info = utils.parse_to_proto(
            #     itx.data.value,
            #     protos.TicketInfo,
            # )
            # # exchange_tx = utils.parse_to_proto(
            # #     ticket_info.tx,
            # #     protos.Transaction,
            # # )

    def update(self, wallet, token, **kwargs):
        event_info = protos.EventInfo(
            title=kwargs.get('title', self.event_info.title),
            # total=kwargs.get('total', self.event_info.total),
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
            tickets=map(
                lambda ticket: ticket.SerializeToString(),
                self.tickets,
            ),
            participants=self.participants,
        )
        forgeRpc.update_asset(
            'ec:s:event_info', self.address, event_info,
            wallet, token,
        )


class TicketAssetState:
    def __init__(self, asset_state):
        self.address = asset_state.address
        self.owner = asset_state.owner
        self.monier = asset_state.moniker
        self.read_only = asset_state.read_only
        self.context = asset_state.context
        self.stake = asset_state.stake
        self.ticket_info = utils.decode_to_proto(
            asset_state.data.value,
            protos.TicketInfo,
        )
        self.id = self.ticket_info.id
        self.token = self.ticket_info.token
        self.is_used = self.ticket_info.is_used

    def verify_owner(self, wallet):
        token = gen_ticket_token(self.id, wallet)
        if token == self.token:
            return True
        else:
            return False

    def use(self, wallet, token):
        if self.verify_owner(wallet):
            self.is_used = True
            self.update(wallet, token)

    def update(self, wallet, token):
        ticket_info = protos.TicketInfo(
            id=self.id,
            token=self.token,
            used=self.is_used,
        )
        forgeRpc.update(
            'ec:s:ticket',
            self.address, ticket_info, wallet, token,
        )
