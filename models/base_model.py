from db import get_connection


class BaseModel:
    def __init__(self) -> None:
        self._connection = get_connection()
