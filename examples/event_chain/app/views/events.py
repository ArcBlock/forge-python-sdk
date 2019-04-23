import logging

import requests
from event_chain.app import controllers
from event_chain.app import db
from event_chain.app import models
from event_chain.app import utils
from event_chain.app.forms.event import EventForm
from event_chain.app.models import EventModel
from event_chain.app.models import ExchangeHashModel
from event_chain.config import config
from event_chain.config.config import APP_ADDR
from event_chain.config.config import APP_PK
from event_chain.config.config import ARC
from event_chain.config.config import SERVER_ADDRESS
from flask import Blueprint
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for

events = Blueprint(
    'events',
    __name__,
    template_folder='templates',
)

logger = logging.getLogger('view-event')


@events.route("/all", methods=['GET', 'POST'])
def all():
    def list_events():
        addr_list = [model.address for model in EventModel.query.all()]
        event_states = []
        for addr in addr_list:
            state = models.get_event_state(addr)
            if state:
                event_states.append(state)
        return event_states

    all_events = list_events()
    event_lists = utils.chunks(all_events, 3)

    return render_template(
        'events/event_list.html', event_lists=event_lists,
        session=session, number=len(all_events)
    )


@events.route("/detail/<address>", methods=['GET', 'POST'])
def detail(address):
    error = utils.verify_event(address)
    if error:
        return error
    forge_web = 'http://{0}:{1}/node/explorer/txs/'.format(
        config.app_host, config.forge_port
    )

    event = models.get_event_state(address)
    host = models.get_participant_state(event.owner)
    form = EventForm()
    if is_loggedin():
        url = gen_mobile_url(address)
        logger.info("Url for mobile buy ticket: {}".format(url))

        consume_url = gen_consume_url(address)
        logger.info("Url for mobile consume ticket: {}".format(consume_url))

        txs = list_event_exchange_txs(address)
        num_txs = len(txs)
        tx_lists = utils.chunks(txs, 3)
        logger.debug('forgeweb:{}'.format(forge_web))
        return render_template(
            'events/event_details.html', **locals(),
            to_display_time=utils.to_display_time,
            shorten_hash=utils.shorten_hash,
            to_short_time=utils.to_short_time
        )
    return redirect(url_for('admin.login'))


@events.route("/create", methods=['GET', 'POST'])
def create():
    if not session.get('user'):
        return redirect(url_for('admin.login'))
    utils.refresh_token()
    form = EventForm()
    if form.validate_on_submit():
        if request.method == "POST":
            event = controllers.create_event(
                user=session.get('user'),
                title=form.title.data,
                total=form.total.data,
                description=form.description.data,
                start_time=form.start_time.data,
                end_time=form.end_time.data,
                ticket_price=form.ticket_price.data * 1e+16,
                location=form.location.data,
                conn=g.db,
            )
            if event.finished:
                db.session.add(EventModel(address=event.address,
                                          owner=session.get('user')
                                          .get_wallet().address))
                db.session.commit()
            utils.wait()
            return redirect('/')
    else:
        logger.error(form.errors)
        utils.flash_errors(form)
    return render_template('events/event_create.html', form=form)


def list_event_exchange_txs(event_address):
    hashes = [[model.hash for model in ExchangeHashModel.query.filter(
        ExchangeHashModel.event_address == event_address)]]
    tx_list = []
    for hash in hashes:
        tx = controllers.get_tx_info(hash)
        if tx:
            tx_list.append(tx)
    return tx_list


def is_loggedin():
    if session.get('user'):
        return True
    else:
        return redirect('/login')


def gen_consume_url(event_address):
    url = SERVER_ADDRESS + url_for(
        'api_mobile.require_asset', event_address=event_address),
    return utils.gen_did_url(url, 'RequestAuth')


def gen_mobile_url(event_address):
    params = {
        'appPk': APP_PK,
        'appDid': 'did:abt:' + APP_ADDR,
        'action': 'requestAuth',
        'url': SERVER_ADDRESS + url_for(
            'api_mobile.buy_ticket', event_address=event_address),
    }
    r = requests.Request('GET', ARC, params=params).prepare()
    logger.info(u'Url generated {}'.format(r.url))
    return r.url
