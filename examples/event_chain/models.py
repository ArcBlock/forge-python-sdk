from google.protobuf.timestamp_pb2 import Timestamp

from . import protos
from .simulators import forgeSdk
from forge import Signer
from forge import utils

forgeRpc = forgeSdk.rpc


def create_ticket_itx(id, wallet, tx=None):
    token = Signer().sign(protos.TicketInfo(id=id), wallet.sk)
    ticket = protos.TicketInfo(id=id, token=token, tx=tx)
    ticket_itx = protos.CreateAssetTx(
        data=utils.encode_to_any(
            'ec:t:ticket',
            ticket,
        ),
    )
    return ticket_itx


def tx_with_sig(wallet, tx):
    signature = Signer().sign(tx, wallet.sk)
    tx = protos.Transaction(
        **{
            'from': getattr(tx, 'from'),
            'nonce': tx.nonce,
            'signature': signature,
            'chain_id': tx.chain_id,
            'signatures': tx.signatures,
            'itx': tx.itx,
        }
    )
    return tx


def to_google_timestamp(timestamp):
    return Timestamp(timestamp)


def gen_exchange_tx(value, asset_address):
    receiver = protos.ExchangeInfo(
        value=protos.BigUint(value=value.to_bytes()),
    )
    sender = protos.ExchangeInfo(assets=[asset_address])
    exchange_tx = protos.ExchangeTx(sender=sender, receiver=receiver)
    return exchange_tx


class Event:
    def __init__(self, wallet=None, token='', **kwargs):
        self.wallet = wallet
        self.token = token

        self.title = kwargs.get('title')
        self.total = kwargs.get('total')
        self.start_time = kwargs.get('start_time')
        self.end_time = kwargs.get('end_time')
        self.ticket_price = kwargs.get('ticket_price', 0)
        self.description = kwargs.get('description', 'No description :(')
        self.ticket_txs = []
        self.gen_tickets()
        self.participants = []

    def event_info_builder(self):
        event_info = protos.EventInfo(
            title=self.title,
            total=self.total,
            start_time=to_google_timestamp(self.start_time),
            end_time=to_google_timestamp(self.end_time),
            ticket_price=self.ticket_price,
            tickets=self.ticket_txs_bytes(),
            participants=self.participants,
        )
        return event_info

    def create(self):
        event_info = self.event_info_builder()
        forgeRpc.create_asset(
            'ec:t:event_info', event_info, self.wallet,
            self.token,
        )

    def update(self, address):
        event_info = self.event_info_builder()
        forgeRpc.update_asset(
            'ec:t:event_info', address, event_info,
            self.wallet,
            self.token,
        )

    def ticket_txs_bytes(self):
        ticket_bytes = []
        for tx in self.ticket_txs:
            ticket_bytes.append(tx.SerializeToString())
        return ticket_bytes

    def gen_tickets(self):
        for id in range(self.total):
            tx = self.gen_create_ticket_tx(id, self.wallet)
            encoded_tx = utils.encode(tx)
            self.ticket_txs.append(encoded_tx)

    def add_participant(self, address):
        # do we limit here?
        self.participants.append(address)

    def gen_create_ticket_tx(self, id, wallet):
        # create ticket asset
        ticket_itx = create_ticket_itx(id, wallet)

        # get asset address
        asset_address = utils.to_asset_address(
            wallet.address,
            ticket_itx,
        )
        # use asset_address to generate exchange_tx
        exchange_tx = gen_exchange_tx(self.ticket_price, asset_address)

        # put exchange_tx back to ticket_itx, and re-generate ticket_itx
        ticket_itx = create_ticket_itx(id, wallet, exchange_tx)

        tx = tx_with_sig(
            wallet, protos.Transaction(
                **{
                    'from': wallet.address,
                    'itx': ticket_itx,
                }
            ),
        )
        return tx


class EventAssetState:
    def __init__(self, asset_state, wallet=None, token=''):
        self.wallet = wallet,
        self.token = token,
        self.address = asset_state.address
        self.owner = asset_state.owner
        self.monier = asset_state.moniker
        self.read_only = asset_state.read_only
        self.context = asset_state.context
        self.stake = asset_state.stake
        self.event_info = utils.parse_to_proto(
            asset_state.data.value,
            protos.EventInfo,
        )

        self.tickets = list(self.event_info.tickets)
        self.participants = list(self.event_info.participants)

    def execute_next_ticket(self):
        if len(self.tickets) < 1:
            raise ValueError("There is not ticket left for this event!")
        else:
            next_tx = utils.parse_to_proto(self.tickets[0], protos.Transaction)
            res = forgeRpc.send_tx(next_tx)
            if res.code == 0:
                self.tickets = self.tickets[1:]
                self.update()

    def update(self, **kwargs):
        event_info = protos.EventInfo(
            title=kwargs.get('title'),
            total=kwargs.get('total'),
            start_time=kwargs.get('start_time'),
            end_time=kwargs.get('end_time'),
            ticket_price=kwargs.get('ticket_price', 0),
            description=kwargs.get('description', 'No description :('),
            tickets=map(
                lambda ticket: ticket.SerializeToString(),
                self.tickets,
            ),
            participants=self.participants,
        )
        forgeRpc.update_asset(
            'ec:s:event_info', self.address, event_info,
            self.wallet, self.token,
        )


class TicketAssetState:
    def __init__(self, asset_state):
        self.ticket_info = utils.decode_to_proto(
            asset_state.data,
            protos.TicketInfo,
        )
        self.id = self.ticket_info.id
        self.is_used = self.ticket_info.is_used
        self.is_bought = False


def create(self):
    forgeRpc.send_tx(self.ticket_info)


def get_exchange_tx(self):
    exchange_tx = utils.parse_to_proto(
        self.ticket_info.tx,
        protos.ExchangeTx,
    )
    return exchange_tx
