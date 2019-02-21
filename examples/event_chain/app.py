import logging

from . import models
from forge import ForgeSdk

logger = logging.getLogger('Event-Chain')

forgeSdk = ForgeSdk()
forgeRpc = forgeSdk.rpc

events = []
users = []


def register_user(name, passphrase='abcde1234'):
    user = models.DeclaredUser(moniker=name, passphrase=passphrase)
    user.declare()
    logger.info("User {} created successfully!".format(name))
    users.append(user)
    return user


def create_event(
        title, total, start_time, end_time, ticket_price, wallet,
        token,
):
    event_info = models.EventInfo(
        title=title,
        total=total,
        start_time=start_time,
        end_time=end_time,
        ticket_price=ticket_price,
        wallet=wallet,
        token=token,
    )
    event_info.create()
    events.append(event_info.address)


def list_events():
    req_list = [{'address': addr} for addr in events]
    event_states = forgeRpc.get_asset_state(req_list)
    for res in event_states:
        list_event_detail(res.state)


def list_users():
    for user in users:
        print("User Name: ", user.moniker)
        print("User Address:", user.address)


def list_event_detail(state):
    event_asset = models.EventAssetState(state)
    event_info = event_asset.event_info
    print('Title:', event_info.title)
    print('Total Tickets: ', event_info.total)
    print("Created by: ", event_asset.owner)


def list_unused_ticket():
    return


def get_event_state(event_address):
    state = forgeRpc.get_single_asset_state(event_address)
    if not state:
        logger.error("Event {} doesn't exist.".format(event_address))
    else:
        return models.EventAssetState(state)


def get_ticket(ticket_address):
    state = forgeRpc.get_single_asset_state(ticket_address)
    if not state:
        logger.error("Ticket {} doesn't exist.".format(ticket_address))
    else:
        return models.TicketAssetState(state)


def buy_ticket(event_address, wallet, token):
    res = forgeRpc.get_single_asset_state(event_address)
    # if models.is_asset_exist(res):
    #     logger.error("Event doesn't exist.")
    event_asset = models.EventAssetState(res)
    return event_asset.buy_ticket(wallet, token)


def use_ticket(ticket_address, user_wallet, user_token):
    state = forgeRpc.get_single_asset_state(ticket_address)
    ticket_asset = models.TicketAssetState(state)
    return ticket_asset.use(user_wallet, user_token)
