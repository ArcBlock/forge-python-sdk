import os.path as path
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
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import DataRequired

from examples.event_chain import app

application = Flask(__name__)
application.config['SECRET_KEY'] = 'you-will-never-guess'
SESSION_TYPE = 'filesystem'
application.config.from_object(__name__)
Session(application)

DB_PATH = path.join(path.dirname(__file__), "priv", "sqlite.db")


def wait():
    sleep(5)


def connect_db():
    return sqlite3.connect(DB_PATH)


@application.before_request
def before_request():
    g.db = connect_db()


@application.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()


@application.route("/details", methods=['GET', 'POST'])
def event_detail():
    event_address = request.args.get('address')
    event = app.get_event_state(event_address)
    if not session.get('cur_user', None):
        flash('Please register first!')
        return redirect('/register')
    if request.method == "POST" and 'Buy' in request.form:
        app.buy_ticket(event_address, session['cur_user'], g.db)
        return redirect('/')
    return render_template('event_details.html', event=event)


@application.route("/", methods=['GET', 'POST'])
def event_list():
    events = app.list_events(g.db)
    event_lists = chunks(events, 3)
    return render_template('event_list.html', event_lists=event_lists)


@application.route("/tickets")
def ticket_list():
    if not session.get('cur_user', None):
        flash('Please register first!')
        return redirect('/register')
    tickets = app.list_unused_tickets(session['cur_user']['address'])
    return render_template('tickets.html', tickets=tickets)


class EventCreateForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    confirm = SubmitField('Confirm')


@application.route("/create", methods=['GET', 'POST'])
def create_event():
    form = EventCreateForm()
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


@application.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
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
        return redirect('/')
    return render_template('register.html', form=form)


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
        return redirect('/')
    return render_template('login.html', form=form)


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


if __name__ == '__main__':
    application.debug = True
    application.run()
