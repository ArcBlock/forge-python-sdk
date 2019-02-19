# from flask import Flask
# from flask import render_template
# app = Flask(__name__)
#
# @app.route('/')
# def hello_world():
#     events = ['event1', 'event2', 'event3']
#     return render_template('event_list.html', events=events)
import models

from forge import ForgeSdk

forgeSdk = ForgeSdk()
forgeRPC = forgeSdk.rpc

events = []
users = []


def register_user(name, passphrase='abcde1234'):
    user = models.DeclaredUser(moniker=name, passphrase=passphrase)
    user.declare()
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
    event_states = forgeRPC.get_asset_state(req_list)
    for res in event_states:
        list_event_detail(res.state)


def list_users():
    print('****************************')
    for user in users:
        print("User Name: ", user.moniker)
        print("User Address:", user.address)
    print('****************************')


def list_event_detail(state):
    event_asset = models.EventAssetState(state)
    print('****************************')
    print('Title:', event_asset.event_info.title)
    print('Start Time:', event_asset.event_info.start_time)
    print('Total Tickets: ', event_asset.event_info.total)
    print("Created by: ", event_asset.owner)
    print('****************************')


def list_unused_ticket():
    return


def buy_ticket(event_address, wallet, token):
    res = forgeRPC.get_single_asset_state(event_address)
    event_asset = models.EventAssetState(res)
    return event_asset.buy_ticket(wallet, token)


def use_ticket():
    return
