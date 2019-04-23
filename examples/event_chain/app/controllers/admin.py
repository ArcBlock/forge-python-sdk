import logging

from event_chain.app import models

logger = logging.getLogger('controller-admin')


def register_user(moniker, passphrase):
    user = models.User(moniker, passphrase)
    logger.info("User {} created successfully!".format(moniker))
    user.poke()
    return user


def load_user(moniker, passphrase, address):
    user = models.User(moniker=moniker, passphrase=passphrase, address=address)
    logger.info("User {} loaded successfully!".format(moniker))
    return user
