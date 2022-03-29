from .base_model import BaseModel
from db import to_json_array, to_json_object
import psycopg2


class UserModel(BaseModel):
    def __init__(self) -> None:
        super().__init__()

    def create_user(self, data):
        pass

    def get_all_users(self):
        cursor = self._connection.cursor()
        cursor.execute("select * from users;")

        print("Selecting rows from mobile table using cursor.fetchall")
        all_users = cursor.fetchall()

        return to_json_array(all_users, cursor)

    def get_user_by_id(self, id: int):
        cursor: psycopg2.cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users WHERE userid = %s", (id,))
        user = cursor.fetchone()

        if not user:
            return None

        return to_json_object(user, cursor)
