import logging

import event_chain.config.config as config
from event_chain.app import utils
from flask import Flask
from flask_googlemaps import GoogleMaps
from flask_qrcode import QRcode
from flask_sqlalchemy import SQLAlchemy

from flask_session import Session

SESSION_TYPE = 'filesystem'

db = SQLAlchemy()
starters = [db, Session(), QRcode(), GoogleMaps()]

logging.basicConfig(level=logging.DEBUG)
DB_PATH = config.db_path
logging.info('DB: {}'.format(DB_PATH))
logging.info('forge port {}'.format(config.forge_config.get_grpc_socket()))
logging.info('app server address: {}'.format(config.SERVER_ADDRESS))


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hihihihihi'
    app.config['WTF_CSRF_ENABLED'] = False
    app.config[
        'GOOGLEMAPS_KEY'] = config.googlemaps_key
    app.config[
        'SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + config.db_path
    app.config.from_object(__name__)

    initialize_extensions(app)
    register_blueprints(app)

    return app


def initialize_extensions(app):
    for starter in starters:
        starter.init_app(app)


def register_blueprints(app):
    from event_chain.app import views
    from event_chain.app import apis

    app.register_blueprint(views.admin, url_prefix='/admin')
    app.register_blueprint(views.events, url_prefix='/events')
    app.register_blueprint(views.tickets, url_prefix='/tickets')
    app.register_blueprint(apis.api_ticket, url_prefix='/api/ticket')
    app.register_blueprint(apis.api_mobile, url_prefix='/api/mobile')
