import os.path as path
import sqlite3
from sqlite3 import Error

DB_PATH = path.join(path.dirname(__file__), "priv", "sqlite.db")


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


if __name__ == '__main__':
    print(DB_PATH)

    create_connection(DB_PATH)
