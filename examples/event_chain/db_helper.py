import logging
import os.path as path
import sqlite3
from sqlite3 import Error

from examples.event_chain.config import config

logger = logging.getLogger('db-helper')


def create_connection(db_path):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except Error as e:
        print(e)
    return None


def init_db(conn):
    c = conn
    c.execute("drop table if exists events;")
    c.execute("drop table if exists tickets;")
    c.execute("drop table if exists users;")

    c.execute('''create table events
                  (address text, owner text);''')

    c.execute('''create table tickets
                  (address text,
                  event_address text,
                  owner text,
                  create_hash,
                  exchange_hash);''')

    c.execute('''create table users
                  (address text, moniker text, passphrase text);''')

    conn.commit()


def insert_ticket(conn, ticket, event, owner, create_hash, exchange_hash):
    if create_hash:
        conn.execute(
            ''' INSERT INTO tickets
                    (address, event_address, owner, create_hash, exchange_hash)
                    VALUES(?,?,?,?,?);''',
            (ticket, event, owner, create_hash, exchange_hash),
        )
    else:
        conn.execute(
            '''
                    UPDATE ticket_txs
                    SET exchange_hash=?
                    WHERE address=?
                    ''', (ticket, exchange_hash),
        )
    conn.commit()


def select_tickets(conn, owner=None, event=None):
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    if owner and event:
        c.execute(
            '''select * from tickets
                        WHERE owner = ? and event_address=?''', (owner, event),
        )
    elif owner:
        c.execute(
            '''select * from tickets
                        WHERE owner = ? ''', [owner],
        )
    elif event:
        c.execute(
            '''select * from tickets
                        WHERE event = ? ''', [event],
        )
    return to_dict(c.fetchall())


def select_ticket_hash(conn, ticket):
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute(
        '''
            select create_hash, exchange_hash from tickets
            where address=?''', [ticket],
    )
    row = c.fetchone()
    return {item[0]: item[1] for item in list(zip(row.keys(), row))}


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
        '''SELECT address from Users where moniker=?''',
        [moniker],
    )
    res = c.fetchone()
    if res:
        return c.fetchone()[0]
    else:
        logger.error("User name doesn't exist for {}".format(moniker))


def select_all_events(conn):
    c = conn.cursor()
    c.execute('''select address from events;''')
    return [row[0] for row in c.fetchall()]


def select_all_users(conn):
    c = conn.cursor()
    c.execute('''select * from Users;''')
    return c.fetchall()


def select_events_by_creator(conn, creator):
    c = conn.cursor()
    c.execute("select * from Events where owner=?", creator)
    return c.fetchall()


def select_user_address(conn, name, passphrase):
    c = conn.cursor()
    c.execute(
        "select address from Users where moniker=? and passphrase=?",
        (name, passphrase),
    )
    return c.fetchone()[0]


if __name__ == '__main__':
    print(config.db_path)
    if not path.exists(config.db_path):
        conn = create_connection(config.db_path)
        init_db(conn)
        conn.close()
