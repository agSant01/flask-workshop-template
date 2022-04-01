from db import Connection, get_connection


class BaseModel:
    def __init__(self) -> None:
        self._connection: Connection = get_connection()
