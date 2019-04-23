import json
import logging
import os
import time

from event_chain.app import controllers
from event_chain.app import create_app
from event_chain.app import db
from event_chain.app.models import EventModel

logger = logging.getLogger('ec-simulator')

DATA_PATH = os.path.join(os.path.dirname(__file__), "sample_data.json")

with open(DATA_PATH, "r") as read_file:
    data = json.load(read_file)

application = create_app()


def reset():
    with application.app_context():
        db.reflect()
        db.drop_all()
        db.create_all(app=application)


def simulate():
    users = data.get('users')
    events = data.get('events')

    test_user = None

    logger.info("Creating Users...")
    for user in users:
        test_user = controllers.register_user(
            user.get('moniker'),
            user.get('passphrase')
        )

    logger.info("Users are created.")

    logger.info("Creating Events...")
    for event in events:
        e = controllers.create_event(test_user, **event)
        if e.finished:
            with application.app_context():
                event_model = EventModel(address=e.address,
                                         owner=test_user.address)
                db.session.add(event_model)
                db.session.commit()
    logger.info("Events are created.")


if __name__ == '__main__':
    reset()
    logger.info("DB has been initialized.")
    simulate()
    logger.info("Data has been simulated.")
