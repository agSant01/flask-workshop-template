"""
Create User Table
"""

from yoyo import step

__depends__ = {"myproject_20220327_01_deMvy-enable-pgcrypto"}


def apply_step(conn):
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE users ( \
            userID SERIAL, \
            firstName VARCHAR(40) NOT NULL, \
            middleName VARCHAR(40) NULL, \
            lastName VARCHAR(40) NOT NULL, \
            email VARCHAR(100) NOT NULL, \
            password TEXT NOT NULL \
        )"
    )


def rollback_step(conn):
    cursor = conn.cursor()
    cursor.execute("DROP TABLE users")


steps = [step(apply_step, rollback_step)]
