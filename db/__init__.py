from configparser import ConfigParser
from flask import g

import psycopg2
from psycopg2 import pool


def __config():
    # create a parser
    _FILENAME = "database.ini"
    _SECTION = "postgresql"

    parser = ConfigParser()
    # read config file
    parser.read(_FILENAME)

    # get section, default to postgresql
    db = {}
    if parser.has_section(_SECTION):
        params = parser.items(_SECTION)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            "Section {0} not found in the {1} file".format(_SECTION, _FILENAME)
        )

    return db


__pool = psycopg2.pool.ThreadedConnectionPool(
    2,
    20,
    **__config(),
)


def get_connection():
    print("GETTING CONN")
    if "db" not in g:
        g.db = __pool.getconn()
    return g.db


def put_connection(connection):
    __pool.putconn(connection)


def get_col_names(cursor):
    return [desc[0] for desc in cursor.description]


def to_json_array(rows, cursor):
    cols = get_col_names(cursor)
    return list(map(lambda x: dict(zip(cols, x)), rows))


def to_json_object(item, cursor):
    cols = get_col_names(cursor)
    return dict(zip(cols, item))
