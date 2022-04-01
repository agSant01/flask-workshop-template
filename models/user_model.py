from typing import Dict, List
from .base_model import BaseModel
from db import to_json_array, to_json_object, Cursor


class UserModel(BaseModel):
    def __init__(self) -> None:
        super().__init__()

    def create_user(self, data):
        # do insert query
        # cursor = self._connection.cursor()
        # cursor.execute("insert into users () values(?,?,?);")
        return {"name": "Dummy user", "last_name": "Not in db. Pending implementation"}

    def get_all_users(self):
        cursor = self._connection.cursor()
        cursor.execute("select * from users;")

        print("Selecting rows from mobile table using cursor.fetchall")
        all_users = cursor.fetchall()

        return to_json_array(all_users, cursor)

    def get_user_by_id(self, id: int):
        cursor: Cursor = self._connection.cursor()
        #  Prepared Statement => Google it :)
        cursor.execute("SELECT * FROM users WHERE userid = %s", (id,))
        user = cursor.fetchone()

        if not user:
            return None

        return to_json_object(user, cursor)

    def filter_by_keyword(self, keywords: Dict[str, str]) -> List:
        print("model", keywords)

        if len(keywords) == 0:
            return []

        where_clause = []
        params = []

        #  building parametrized quiery to avoid SQL Injection
        for key, value in keywords.items():
            where_clause.append(f"{key} ilike %s")  # ILIKE => insensitive case LIKE
            params.append(
                f"%{value}%"
            )  # when using like, put the %'s inside the query param

        where_clause = " AND ".join(where_clause)
        print("[DEBUG] UserModel: filter: message: where clause =>", where_clause)

        cursor: Cursor = self._connection.cursor()
        cursor.execute(f"SELECT * FROM users WHERE {where_clause};", tuple(params))
        filtered_users = cursor.fetchall()

        data = to_json_array(filtered_users, cursor)

        # cleanup
        cursor.close()

        return data
