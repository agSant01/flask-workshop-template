"""
Enable pgcrypto
"""

from yoyo import step

__depends__ = {}


def apply_step(conn):
    cursor = conn.cursor()
    cursor.execute("CREATE EXTENSION IF NOT EXISTS pgcrypto;")


steps = [step(apply_step, ignore_errors="apply")]
