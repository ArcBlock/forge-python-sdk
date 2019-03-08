import logging
import os
import sqlite3

from event_chain.config import config
from event_chain.db.utils import init_db

logger = logging.getLogger('ec-db-init')


def initialized_app_folder():
    app_path = config.app_path
    if not os.path.exists(app_path):
        os.mkdir(app_path)
        logger.info("{} created.".format(app_path))
    else:
        logger.info("{} already exists.".format(app_path))


if __name__ == '__main__':

    initialized_app_folder()

    logger.info('Connecting to db {}'.format(config.db_path))
    conn = sqlite3.connect(config.db_path)
    init_db(conn)
    logger.info('db {} initialized.'.format(config.db_path))
    conn.close()
