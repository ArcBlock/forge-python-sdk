import logging
from datetime import datetime
from time import sleep

from . import models
from forge import ForgeSdk

logger = logging.getLogger('ec-app')

forgeSdk = ForgeSdk()
forgeRpc = forgeSdk.rpc

events = []
users = []


def register_user(name, passphrase):
    user = models.DeclaredUser(moniker=name, passphrase=passphrase)
    user.declare()
    logger.info("User {} created successfully!".format(name))
    users.append(user)
    return user


def create_event(wallet, token, **kwargs):
    event_info = models.EventInfo(
        wallet=wallet,
        token=token,
        title=kwargs.get('title'),
        total=kwargs.get('total'),
        description=kwargs.get('description'),
        start_time=kwargs.get('start_time'),
        end_time=kwargs.get('end_time'),
        ticket_price=kwargs.get('ticket_price'),
    )
    events.append(event_info.address)
    return event_info.address


def list_events():
    req_list = [{'address': addr} for addr in events]
    event_states = forgeRpc.get_asset_state(req_list)
    for res in event_states:
        list_event_detail(res.state)


def list_users():
    for user in users:
        print("****************************")
        print("User Name: ", user.moniker)
        print("User Address:", user.address)


def list_event_detail(state):
    event_asset = models.EventAssetState(state)
    event_info = event_asset.event_info
    print("****************************")
    print('Title:', event_info.title)
    print('Total Tickets: ', event_info.total)
    print("Created by: ", event_asset.owner)
    print("Remaining ticket number: ", event_info.remaining)


def list_unused_ticket():
    return


def get_event_state(event_address):
    state = forgeRpc.get_single_asset_state(event_address)
    if not state:
        logger.error("Event {} doesn't exist.".format(event_address))
    else:
        return models.EventAssetState(state)


def get_ticket_state(ticket_address):
    state = forgeRpc.get_single_asset_state(ticket_address)
    if not state:
        logger.error("Ticket {} doesn't exist.".format(ticket_address))
    else:
        return models.TicketAssetState(state)


def buy_ticket(event_address, user):
    state = forgeRpc.get_single_asset_state(event_address)
    if not state:
        logger.error("Event doesn't exist.")
    event_asset = models.EventAssetState(state)
    return event_asset.buy_ticket(user.wallet, user.token)


def use_ticket(ticket_address, user_wallet, user_token):
    state = forgeRpc.get_single_asset_state(ticket_address)
    ticket_asset = models.TicketAssetState(state)
    return ticket_asset.use(user_wallet, user_token)


def create_sample_event(user, title):
    return create_event(
        wallet=user.wallet,
        token=user.token,
        title=title,
        total=2,
        description='This is a sample event created for demo',
        start_time=datetime(2019, 2, 9, 21),
        end_time=datetime(2019, 2, 10, 23),
        ticket_price=188,
    )


def activate(owner_signed_tx, wallet, token):
    tx = forgeRpc.multisig(owner_signed_tx, wallet, token).tx
    res = forgeRpc.send_tx(tx)
    if res.code != 0:
        logger.error(res)
    logger.info("Ticket has been activated!")
    return res


def refresh():
    sleep(5)
