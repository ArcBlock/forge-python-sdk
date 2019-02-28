import logging
import sqlite3
from time import sleep

from flask import flash
from flask import Flask
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask.ext.session import Session
from flask_qrcode import QRcode
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import DataRequired

from examples.event_chain import app
from examples.event_chain import config

application = Flask(__name__)
application.config['SECRET_KEY'] = 'you-will-never-guess'
SESSION_TYPE = 'filesystem'
application.config.from_object(__name__)
Session(application)
QRcode(application)

DB_PATH = config.db_path


class EventForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
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


@application.route("/details/<address>", methods=['GET', 'POST'])
def event_detail(address):
    if address and address != '':
        event = app.get_event_state(address)
        form = EventForm()
    if not session.get('cur_user', None):
        flash('Please register first!')
        return redirect('/register')
    return render_template('event_details.html', event=event, form=form)


@application.route("/buy", methods=['POST'])
def buy():
    form = EventForm()
    address = form.address.data
    g.logger.debug('address: {}'.format(form.address))
    g.logger.debug('submit: {}'.format(form.confirm))
    if not address or address == '':
        g.logger.error("No event address.")
    else:
        app.buy_ticket(address, session['cur_user'], g.db)
    return redirect('/')


@application.route("/activate", methods=['GET', 'POST'])
def use():
    ticket_address = request.args.get('address')
    ticket = app.get_ticket_state(ticket_address)
    activate_tx = ticket.gen_activate_asset_tx(session['cur_user'])
    app.activate(activate_tx, session['cur_user'])
    return redirect('/')


@application.route("/", methods=['GET', 'POST'])
def event_list():
    events = app.list_events(g.db)
    event_lists = chunks(events, 3)
    return render_template(
        'event_list.html', event_lists=event_lists,
        session=session, number=len(events),
    )


@application.route("/tickets")
def ticket_list():
    # unused_tickets = app.list_unused_tickets(session['cur_user']['address'])
    # used_tickets = app.list_used_tickets(session['cur_user']['address'])
    tickets = app.list_tickets(g.db, session['cur_user']['address'])
    ticket_lists = chunks(tickets, 3)
    return render_template(
        'tickets.html', ticket_lists=ticket_lists,
        number=len(tickets),
    )


@application.route("/create", methods=['GET', 'POST'])
def create_event():
    form = EventForm()
    if form.validate_on_submit():
        if not session.get('cur_user', None):
            flash('Please register first!')
            return redirect('/register')
        elif request.method == "POST":
            app.create_sample_event(
                user_info=session['cur_user'],
                title=form.title.data,
                conn=g.db,
            )
            wait()
            return redirect('/')
    return render_template('event_create.html', form=form)


class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    passphrase = StringField('Passphrase', validators=[DataRequired()])
    confirm = SubmitField('Confirm')


@application.route("/register", methods=['POST'])
def register():
    form = RegisterForm()
    g.logger.debug("{}".format(form.name))

    if form.validate_on_submit():
        g.logger.debug("{}".format(form.name))

        user_info = {}
        user = app.register_user(
            form.name.data,
            form.passphrase.data,
            g.db,
        )
        user_info['moniker'] = user.moniker
        user_info['passphrase'] = user.passphrase
        user_info['address'] = user.address
        session['cur_user'] = user_info
        g.logger.debug("form is validated!!")
        return redirect('/')


@application.route("/ticket_details", methods=['GET', 'POST'])
def ticket_detail():
    address = request.args.get('address')
    g.logger.debug('about to get ticket exchange tx for {}'.format(address))
    if address and address != '':
        event = app.get_event_state(address)
        exchange_tx = app.get_ticket_exchange_tx(address, g.db)
        return render_template(
            'ticket_details.html', tx=exchange_tx,
            event=event,
        )


@application.route("/login", methods=['GET', 'POST'])
def login():
    form = RegisterForm()
    if form.validate_on_submit():
        user_info = {}
        user = app.load_user(
            form.name.data,
            form.passphrase.data,
            g.db,
        )
        user_info['moniker'] = user.moniker
        user_info['passphrase'] = user.passphrase
        user_info['address'] = user.address
        session['cur_user'] = user_info
        session['logged_in'] = True
        return redirect('/')
    return render_template('login.html', form=form)


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


if __name__ == '__main__':
    application.debug = True
    application.run()
