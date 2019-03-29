import logging
import sqlite3
from sqlite3 import Error

from event_chain.config import config

logger = logging.getLogger('db-helper')


def create_connection():
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(config.db_path)
        return conn
    except Error as e:
        logger.error(e)
    return None


def init_db(conn):
    c = conn.cursor()
    try:
        c.execute("drop table if exists events;")
        c.execute("drop table if exists tickets ;")
        c.execute("drop table if exists users;")
        c.execute("drop table if exists mobile_address;")
        c.execute("drop table if exists exchange_txs;")

        c.execute('''create table events
                          (address text, owner text);''')

        c.execute('''create table tickets
                          (address text,
                          event_address text,
                          owner text,
                          create_hash text,
                          exchange_hash text);''')

        c.execute(
            '''create table users (address text, moniker text, passphrase
                            text);'''
        )

        c.execute(
            '''create table mobile_address (address text);'''
        )

        c.execute(
            '''create table exchange_txs (event_address text,
                                                tx_hash text);'''
        )

        conn.commit()
    except Error as e:
        logger.error(e)


def insert_exchange_tx(conn, event_address, tx_hash):
    conn.execute(
        ''' INSERT INTO exchange_txs (event_address, tx_hash)
                                VALUES(?,?);''',
        [event_address, tx_hash])
    conn.commit()


def to_dict(all_rows):
    res = []
    for row in all_rows:
        params = {item[0]: item[1] for item in list(zip(row.keys(), row))}
        res.append(params)
    return res


def insert_event(conn, event, owner):
    c = conn
    c.execute(
        ''' INSERT INTO Events(address, owner) VALUES(?,?);''',
        (event, owner),
    )
    conn.commit()


def insert_user(conn, address, moniker, passphrase):
    c = conn
    c.execute(
        ''' INSERT INTO Users(address, moniker, passphrase) VALUES(?,?,
                                    ?); ''',
        (address, moniker, passphrase),
    )
    conn.commit()


def if_moniker_exists(conn, moniker):
    c = conn.cursor()
    c.execute(
        '''SELECT * from Users where moniker=?''',
        [moniker],
    )
    if c.fetchone():
        return True
    else:
        return False


def select_address_by_moniker(conn, moniker):
    c = conn.cursor()
    c.execute(
        '''SELECT address from users where moniker=?''',
        [moniker],
    )
    res = c.fetchone()
    if res:
        return res[0]
    else:
        logger.error("User name doesn't exist for {}".format(moniker))


def select_all_events(conn):
    c = conn.cursor()
    c.execute('''select address from events;''')
    return [row[0] for row in c.fetchall()]


def select_exchange_txs(conn, event_address):
    c = conn.cursor()
    c.execute('''SELECT DISTINCT tx_hash from exchange_txs where event_address=?''',
              [event_address])
    return [row[0] for row in c.fetchall()]


def insert_mobile_address(conn, address):
    c = conn.cursor()
    c.execute("select * from mobile_address;")
    if c.fetchone():
        c.execute('''delete from mobile_address''')
    c.execute('''insert into mobile_address (address) values (?)''',
              [address], )
    conn.commit()


def delete_mobile_address(conn):
    conn.execute("delete from mobile_address")
    conn.commit()


def get_last_mobile_address(conn):
    c = conn.cursor()
    c.execute("select * from mobile_address;")
    res = c.fetchone()
    if res:
        return res[0]


if __name__ == '__main__':
    db = config.db_path
    logger.info('Connecting to db {}'.format(db))
    conn = sqlite3.connect(db)
    init_db(conn)
    conn.close()
