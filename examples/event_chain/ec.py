import ast
import json
import logging
import sqlite3
import sys
from time import sleep

import base58
import event_chain.application.app as app
import event_chain.config.config as config
import event_chain.db.utils as db
import requests
from event_chain.utils import helpers
from flask import flash
from flask import Flask
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import Response
from flask import session
from flask_googlemaps import GoogleMaps
from flask_qrcode import QRcode
from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms import StringField
from wtforms import SubmitField
from wtforms import ValidationError
from wtforms import validators
from wtforms.validators import DataRequired

from flask_session import Session
from forge.utils import utils

application = Flask(__name__)
application.config['SECRET_KEY'] = 'hihihihihi'
application.config['WTF_CSRF_ENABLED'] = False
SESSION_TYPE = 'filesystem'
application.config[
    'GOOGLEMAPS_KEY'] = config.googlemaps_key
application.config.from_object(__name__)
Session(application)
QRcode(application)
GoogleMaps(application)

logging.basicConfig(level=logging.DEBUG)
DB_PATH = config.db_path
SERVER_ADDRESS = "http://" + config.app_host + ":5000/"

logging.info('DB: {}'.format(DB_PATH))
logging.info('forge port {}'.format(config.forge_config.get_grpc_socket()))
logging.info('app server address: {}'.format(SERVER_ADDRESS))

APP_SK = 'zyQBXZ7NijYQQRzLUryjkd1Mj4qSpofcnsgEh8a8ZrtbgM1jSKHrC85V' \
         'edZsQ5N3x5M298zpridcq2bKBZtmqroT'
APP_PK = "zExrfT2pXtVqdAqgZwjvdMBo5RpqSqn1fa43Wp93peuSR"
APP_ADDR = "z1UT9an1Z4W1gnmzASneER2J5eqtx5jfwgx"

ARC = 'https://arcwallet.io/i/'


def is_loggedin():
    if session.get('user'):
        return True
    else:
        return redirect('/login')


class EventForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    confirm = SubmitField('Confirm')
    total = IntegerField('Total', validators=[DataRequired(),
                                              validators.number_range(min=1,
                                                                      max=30)
                                              ])
    start_time = StringField("StartTime", validators=[DataRequired()])
    description = StringField("Description")
    end_time = StringField("EndTime", validators=[DataRequired()])
    ticket_price = IntegerField("TicketPrice")
    address = StringField('Address')
    location = StringField('Location', validators=[DataRequired()])


def validate_name(form, field):
    for i in field.data:
        if i == ' ':
            raise ValidationError('Name should not contain white space.')
        if not i.isalnum():
            raise ValidationError(
                'Name should not contain special character',
            )


def validate_passphrase(form, field):
    has_alpha = False
    has_num = False
    for i in field.data:
        if i.isnumeric():
            has_num = True
        if i.isalpha():
            has_alpha = True
    if not has_alpha or not has_num:
        raise ValidationError(
            "Password must have both letters and numbers!",
        )


def verify_ticket(address):
    if not address:
        return response_error("Please provide a valid ticket address.")
    try:
        app.verify_ticket_address(address)
    except Exception as e:
        return response_error(e.args[0])


def verify_event(address):
    if not address:
        return response_error("Please provide a valid event address.")
    try:
        app.verify_event_address(address)
    except Exception as e:
        return response_error(e.args[0])


class RegisterForm(FlaskForm):
    name = StringField(
        'Name', validators=[
            DataRequired(),
            validators.length(min=4, max=20),
            validate_name,
        ],
    )
    passphrase = StringField(
        'Passphrase', validators=[
            DataRequired(),
            validate_passphrase,
        ],
    )
    confirm = SubmitField('Confirm')
    address = StringField('Address')


def wait():
    sleep(5)


def connect_db():
    return sqlite3.connect(DB_PATH)


@application.before_request
def before_request():
    g.db = connect_db()
    g.logger = logging.getLogger('app')
    g.logger.setLevel(level=logging.DEBUG)


@application.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()


def gen_mobile_url(event_address):
    params = {
        'appPk': APP_PK,
        'appDid': 'did:abt:' + APP_ADDR,
        'action': 'requestAuth',
        'url': SERVER_ADDRESS + 'api/mobile-buy-ticket/{}'.format(
            event_address,
        ),
    }
    r = requests.Request('GET', ARC, params=params).prepare()
    g.logger.info(u'Url generated {}'.format(r.url))
    return r.url


def gen_consume_url(event_address):
    url = SERVER_ADDRESS + 'api/mobile-require-asset/{}'.format(
        event_address,
    )
    return gen_did_url(url, 'RequestAuth')


def gen_did_url(url, action):
    g.logger.debug(
        "Generating url for DID call. Call back url provided is {}".format(
            url,
        ),
    )
    params = {
        'appPk': APP_PK,
        'appDid': 'did:abt:' + APP_ADDR,
        'action': action,
        'url': url,
    }
    r = requests.Request('GET', ARC, params=params).prepare()
    return r.url


@application.route("/details/<address>", methods=['GET', 'POST'])
def event_detail(address):
    error = verify_event(address)
    if error:
        return error
    forge_web = 'http://{0}:{1}/node/explorer/txs/'.format(
        config.app_host, config.forge_port
    )

    event = app.get_event_state(address)
    host = app.get_participant_state(event.owner)
    form = EventForm()
    if is_loggedin():
        url = gen_mobile_url(address)
        g.logger.info("Url for mobile buy ticket: {}".format(url))

        consume_url = gen_consume_url(address)
        g.logger.info("Url for mobile consume ticket: {}".format(consume_url))

        txs = app.list_event_exchange_txs(g.db, address)
        num_txs = len(txs)
        tx_lists = chunks(txs, 3)
        g.logger.debug('forgeweb:{}'.format(forge_web))
        return render_template(
            'event_details.html', **locals(),
            to_display_time=helpers.to_display_time
        )
    return redirect('/login')


@application.route("/ticket-detail", methods=['GET', 'POST'])
def ticket_detail():
    form = EventForm()
    address = form.address.data if form.address.data else request.args.get(
        'address',
    )
    view_only = request.args.get('viewonly', False)
    error = verify_ticket(address)
    if error:
        return error
    ticket = app.get_ticket_state(address)
    event = app.get_event_state(ticket.event_address)
    host = app.get_participant_state(event.owner)

    return render_template(
        "ticket_details.html", ticket=ticket, event=event, form=form,
        host=host, view_only=view_only,
    )


@application.route("/buy", methods=['POST'])
def buy():
    if not session.get('user'):
        return redirect('/login')
    refresh_token()
    form = EventForm()
    address = form.address.data
    event = app.get_event_state(address)

    error = verify_event(address)
    if error:
        return error

    hash = app.buy_ticket(address, session.get('user'), g.db)
    if not hash:
        g.logger.error("Fail to buy ticket from web.")
        flash('Oops! Someone is faster than you. Get another ticket!')
        return redirect('/')
    else:
        db.insert_exchange_tx(g.db, event.address, hash)
        g.logger.info("ticket is bought successfully from web.")
        flash(
            'Congratulations! Ticket for Event "{}" is bought '
            'successfully!'.format(
                event.event_info.title), category='info')
    return redirect('/tickets')


@application.route("/activate/<address>", methods=['GET', 'POST'])
def use(address):
    refresh_token()

    error = verify_ticket(address)
    if error:
        return error
    app.consume(address, session['user'])
    sleep(2)
    flash('Your ticket has been checked successfully! Enjoy your event!',
          category='info')
    return redirect('/tickets')


@application.route("/", methods=['GET', 'POST'])
def event_list():
    events = app.list_events(g.db)
    event_lists = chunks(events, 3)
    return render_template(
        'event_list.html', event_lists=event_lists,
        session=session, number=len(events),
    )


def get_event_for_ticket(tickets):
    res = {}
    for ticket in tickets:
        event_address = ticket.ticket_info.event_address
        event = app.get_event_state(event_address)
        res[ticket.address] = event
    return res


@application.route("/logout", methods=['GET', 'POST'])
def logout():
    session['user'] = None
    db.delete_mobile_address(g.db)
    return redirect('/')


@application.route("/tickets")
def ticket_list():
    if not session.get('user'):
        return redirect('login')
    tickets = app.list_unused_tickets(session.get('user').address)
    num_tickets = len(tickets)
    user = app.get_participant_state(session.get('user').address)
    events = get_event_for_ticket(tickets)
    ticket_lists = chunks(tickets, 3)
    return render_template(
        'tickets.html', ticket_lists=ticket_lists, events=events,
        user=user, view_only=False, num_tickets=num_tickets
    )


@application.context_processor
def inject_mobile_address():
    return dict(mobile_address=db.get_last_mobile_address(g.db))


@application.route("/mobile-account", methods=['GET'])
def mobile_account():
    address = db.get_last_mobile_address(g.db)
    if not address:
        flash("Please use your mobile wallet to buy a ticket first!",
              category='info')
        return redirect('/')
    tickets = app.list_unused_tickets(address)
    user = app.get_participant_state(address)
    events = get_event_for_ticket(tickets)
    ticket_lists = chunks(tickets, 3)
    return render_template(
        'tickets.html', ticket_lists=ticket_lists, events=events,
        user=user, view_only=True
    )


@application.route("/create", methods=['GET', 'POST'])
def create_event():
    if not session.get('user'):
        return redirect('/login')
    refresh_token()
    form = EventForm()
    if form.validate_on_submit():
        if request.method == "POST":
            app.create_event(
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
            wait()
            return redirect('/')
    else:
        g.logger.error(form.errors)
        flash_errors(form)
    return render_template('event_create.html', form=form)


def refresh_token():
    user = session.get('user')
    user = app.load_user(
        moniker=user.moniker,
        passphrase=user.passphrase,
        conn=g.db,
        address=user.address,
    )
    session['user'] = user
    g.logger.info("Token refreshed!")


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(
                "Error in the {} field - {}".format(
                    getattr(form, field).label.text,
                    error), 'error',
            )


@application.route("/login", methods=['GET', 'POST'])
def login():
    form = RegisterForm()
    if form.validate_on_submit():
        user = app.load_user(
            moniker=form.name.data,
            passphrase=form.passphrase.data,
            address=form.address.data,
        )
        session['user'] = user
        return redirect('/')
    else:
        flash_errors(form)
    return render_template('login.html', form=form)


@application.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = app.register_user(
            form.name.data,
            form.passphrase.data,
            g.db,
        )
        session['user'] = user
        g.logger.debug(
            'New User registered! wallet: {}, token: {}'.format(
                user.wallet,
                user.token,
            ),
        )
        g.logger.debug("form is validated!!")
        wait()
    else:
        flash_errors(form)
        return render_template('login.html', form=form)
    return redirect('/')


def send_did_request(
        url, description, endpoint, workflow, tx=None,
        target=None,
):
    if tx:
        base58_encoded = (b'z' + base58.b58encode(
            tx.SerializeToString(),
        )).decode()
        g.logger.debug(
            u"Sending request to DID with base58 encoded tx: {} and"
            u" url {}".format(base58_encoded, url),
        )
    else:
        base58_encoded = None

    params = {
        'sk': APP_SK,
        'pk': APP_PK,
        'address': APP_ADDR,
        'tx': base58_encoded,
        'description': description,
        'target': target,
        'url': url,
        'workflow': workflow,
    }
    headers = {'content-type': 'application/json'}
    call_url = 'http://localhost:4000/api/' + endpoint
    g.logger.debug('call url : {}'.format(call_url))
    response = requests.post(
        call_url,
        json=params,
        headers=headers,
    )
    g.logger.info("Response from did: {}".format(response.content.decode()))
    return Response(
        response.content.decode(), status=200,
        mimetype='application/json',
    )


@application.route(
    "/api/mobile-buy-ticket/<event_address>",
    methods=['GET', 'POST'],
)
def mobile_buy_ticket(event_address):
    try:
        error = verify_event(event_address)
        if error:
            return error
        if request.method == 'GET':
            g.logger.debug("Receives get request for mobile-buy-ticket.")
            user_did = request.args.get('userDid')
            user_pk = utils.multibase_b58decode(request.args.get('userPk'))
            if not user_did:
                return response_error("Please provide a valid user did.")
            user_address = user_did.split(":")[2]
            g.logger.debug(
                "user address parsed from request {}".format(user_address),
            )

            event = app.get_event_state(event_address)
            updated_exchange_tx = helpers.update_tx_multisig(
                event.get_exchange_tx(),
                user_address,
                user_pk
            )
            g.logger.debug('new tx {}:'.format(updated_exchange_tx))
            call_back_url = SERVER_ADDRESS + "api/mobile-buy-ticket/"
            des = 'Confirm the purchase below.'

            did_request_params = {
                'user_did': user_did,
                'tx': updated_exchange_tx,
                'url': call_back_url,
                'description': des,
                'action': 'responseAuth',
                'workflow': 'buy-ticket',
            }
            response = app.did_auth_require_multisig(**did_request_params)
            g.logger.debug('did auth response: {}'.format(response))
            return response

        elif request.method == 'POST':
            g.logger.debug("Receives post request for mobile-buy-ticket.")
            try:
                req_data = request.get_data(as_text=True)
                g.logger.debug("Receives data from wallet {}".format(req_data))
                req = ast.literal_eval(req_data)
                wallet_response = helpers.WalletResponse(req)
            except Exception as e:
                g.logger.error(e, exc_info=True)
                return response_error("Error in parsing wallet data.")

            user_address = wallet_response.get_address()
            participant_state = app.get_participant_state(user_address)
            if not participant_state:
                return response_error(
                    "user {} doesn't exist.".format(user_address))

            ticket_address, hash = app.buy_ticket_mobile(
                event_address,
                user_address,
                wallet_response.get_signature(),
                wallet_response.get_user_pk(),
            )

            if ticket_address and hash:
                g.logger.info("Ticket {} is bought successfully "
                              "by mobile.".format(ticket_address))

                db.insert_mobile_address(g.db, user_address)
                db.insert_exchange_tx(g.db, event_address, hash)
                base58_encoded = helpers.base58_encode_tx(
                    helpers.update_tx_multisig(
                        app.get_event_state(
                            event_address).get_exchange_tx(),
                        user_address,
                        wallet_response.get_user_pk(),
                    ))
                js = json.dumps({'ticket': ticket_address,
                                 'hash': hash,
                                 'tx': base58_encoded})
                g.logger.debug('success response: {}'.format(str(js)))
                resp = Response(js, status=200, mimetype='application/json')
                return resp
            else:
                g.logger.error(
                    'Fail to buy ticket. ticket '
                    'address: {0}, hash : {1}.'.format(ticket_address,
                                                       hash))
                return response_error('Please try buying the ticket again.')
    except Exception as e:
        g.logger.error(e, exc_info=True)
        return response_error('Exception in buying ticket.')


def response_error(msg):
    error = json.dumps({'error': msg})
    return Response(error, status=400, mimetype='application/json')


@application.route("/error", methods=['GET', 'POST'])
def error():
    return "Sorry there's something wrong in purchasing your ticket."


@application.route(
    "/api/mobile-require-asset/<event_address>",
    methods=['GET', 'POST'],
)
def mobile_require_asset(event_address):
    try:
        error = verify_event(event_address)
        if error:
            return error
        event = app.get_event_state(event_address)

        if request.method == 'GET':
            call_back_url = SERVER_ADDRESS + "api/mobile-require-asset/"
            des = 'Select a ticket for event.'
            target = event.event_info.title
            did_request_params = {
                'url': call_back_url,
                'description': des,
                'action': 'responseAuth',
                'workflow': 'use-ticket',
                'target': target,
            }
            response = app.did_auth_require_asset(**did_request_params)
            return response

        if request.method == 'POST':
            try:
                req_data = request.get_data(as_text=True)
                g.logger.debug("Receives data from wallet {}".format(req_data))
                req = ast.literal_eval(req_data)
                wallet_response = helpers.WalletResponse(req)
            except Exception as e:
                g.logger.error(
                    "error in parsing wallet data, error:{}".format(e),
                )
                g.logger.error(e, exc_info=True)
                return response_error("Error in parsing wallet data. Original "
                                      "data received is {}".format(req))

            asset_address = wallet_response.get_asset_address()
            if not asset_address:
                g.logger.error(
                    "No available asset address in wallet response.",
                )
                return response_error("Please provide an asset address.")

            error = verify_ticket(asset_address)
            if error:
                g.logger.error(
                    "ticket address in wallet response is not valid.",
                )
                return response_error("Please provide a valid ticket address.")

            user_address = wallet_response.get_address()
            call_back_url = SERVER_ADDRESS + "api/mobile-consume/{}".format(
                asset_address,
            )
            des = 'Confirm to use the ticket.'
            consume_tx = event.event_info.consume_tx
            multisig_data = helpers.encode_string_to_any(
                'fg:x:address',
                asset_address,
            )

            new_tx = helpers.update_tx_multisig(
                tx=consume_tx, signer=user_address,
                pk=wallet_response.get_user_pk(),
                data=multisig_data,
            )

            did_request_params = {
                'user_did': user_address,
                'tx': new_tx,
                'url': call_back_url,
                'description': des,
                'action': 'responseAuth',
                'workflow': 'use-ticket',
            }
            response = app.did_auth_require_multisig(**did_request_params)
            return response

    except Exception as e:
        g.logger.error(e, exc_info=True)
        return response_error("Exception in requesting asset.")


@application.route(
    "/api/mobile-consume/<ticket_address>", methods=['POST'],
)
def mobile_consume(ticket_address):
    try:
        error = verify_ticket(ticket_address)
        if error:
            return error

        ticket = app.get_ticket_state(ticket_address)
        event = app.get_event_state(ticket.event_address)

        if request.method == 'POST':
            try:
                req_data = request.get_data(as_text=True)
                g.logger.debug("Receives data from wallet {}".format(req_data))
                req = ast.literal_eval(req_data)
                wallet_response = helpers.WalletResponse(req)
            except Exception as e:
                g.logger.error(e, exc_info=True)
                return response_error("Error in parsing wallet data. Original "
                                      "data received is {}".format(req))

            hash = app.consume_ticket_mobile(
                ticket,
                event.event_info.consume_tx,
                wallet_response.get_address(),
                wallet_response.get_signature(),
                wallet_response.get_user_pk(),
            )
            multisig_data = helpers.encode_string_to_any(
                'fg:x:address',
                ticket_address,
            )
            base58_tx = helpers.base58_encode_tx(helpers.update_tx_multisig(
                tx=event.event_info.consume_tx,
                signer=wallet_response.get_address(),
                pk=wallet_response.get_user_pk(),
                data=multisig_data
            ))
            if hash:
                g.logger.info("ConsumeTx has been sent.")
                js = json.dumps({'hash': hash,
                                 'tx': base58_tx})
                g.logger.debug('success response: {}'.format(js))
                resp = Response(js, status=200, mimetype='application/json')
                return resp
            else:
                g.logger.error('Fail to consume ticket.')
                return response_error('Your ticket might have been '
                                      'checked out before. '
                                      'Please wait and try again.')
    except Exception as e:
        g.logger.error(e, exc_info=True)
        return response_error("Exception in consuming ticket.")


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


if __name__ == '__main__':
    run_type = sys.argv[1]
    application.jinja_env.auto_reload = True
    application.config['TEMPLATES_AUTO_RELOAD'] = True
    if run_type == 'debug':
        application.run(debug=True, host='0.0.0.0')
    else:
        application.run(
            debug=False, host='0.0.0.0'
        )
