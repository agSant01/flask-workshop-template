"""
create item provider
"""

from yoyo import step

__depends__ = {"myproject_20220327_02_SRtm1-create-user-table"}


def apply_query(conn):
    cursor = conn.cursor()
    # still  missing columns in table
    # suggestion: add them with a new migration that does an ALTER Table
    cursor.execute("Create table Provider( pid SERIAL NOT NULL );")
    cursor.close()


def rollback_query(conn):
    cursor = conn.cursor()
    cursor.execute("DROP TABLE Provider;")
    cursor.close()


steps = [step(apply_query, rollback_query)]
