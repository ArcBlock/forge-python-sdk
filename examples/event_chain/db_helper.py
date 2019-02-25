import os.path as path
import sqlite3
from sqlite3 import Error

from examples.event_chain.config import config


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
    c.execute("drop table if exists Events")
    c.execute("drop table if exists Tickets")
    c.execute("drop table if exists Users")

    c.execute('''create table Events
                  (address text, owner text);''')

    c.execute('''create table Tickets
                  (address text, event_address text, owner text);''')

    c.execute('''create table Users
                  (address text, moniker text, passphrase text);''')

    conn.commit()


def insert_event(conn, event, owner):
    c = conn
    c.execute(
        ''' INSERT INTO Events(address, owner) VALUES(?,?);''',
        (event, owner),
    )
    conn.commit()


def insert_ticket(conn, ticket_address, event_address, owner):
    c = conn
    c.execute(
        ''' INSERT INTO Tickets(address, event_address, owner) VALUES(?,?,
            ?); ''',
        (ticket_address, event_address, owner),
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


def select_all_events(conn):
    c = conn.cursor()
    c.execute('''select address from Events;''')
    return [row[0] for row in c.fetchall()]


def select_all_users(conn):
    c = conn.cursor()
    c.execute('''select * from Users;''')
    return c.fetchall()


def select_tickets_by_owner(conn, owner):
    c = conn.cursor()
    c.execute("select address from Tickets where owner=?", owner)
    return [row[0] for row in c.fetchall()]


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
