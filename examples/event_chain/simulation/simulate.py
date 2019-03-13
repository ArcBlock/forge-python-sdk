import json
import logging
import os
import time

import event_chain.application.app as app
from event_chain import db

logger = logging.getLogger('ec-simulator')

DATA_PATH = os.path.join(os.path.dirname(__file__), "sample_data.json")

with open(DATA_PATH, "r") as read_file:
    data = json.load(read_file)


def set_up_db():
    db.init.initialized_app_folder()
    conn = db.init.reset_db()
    return conn


def simulate(conn):
    users = data.get('users')
    events = data.get('events')

    test_user = None

    logger.info("Creating Users...")
    for user in users:
        test_user = app.register_user(
            user.get('moniker'),
            user.get('passphrase'), conn,
        )

    time.sleep(5)
    logger.info("Users are created.")

    logger.info("Creating Events...")
    for event in events:
        app.create_event(test_user, conn, **event)
    logger.info("Events are created.")

    time.sleep(5)


if __name__ == '__main__':
    conn = set_up_db()
    logger.info("DB has been initialized.")

    simulate(conn)
    logger.info("Data has been simulated.")
