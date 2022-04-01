from models.user_model import UserModel


class UserController:
    def __init__(self) -> None:
        self.user_model = UserModel()

    def create_user(self, user_data: dict):
        return self.user_model.create_user(user_data)

    def get_users(self):
        # user_model = UserModel()
        return self.user_model.get_all_users()

    def get_user_info(self, id: int):
        # user_model = UserModel()
        return self.user_model.get_user_by_id(id)

    def filter_user_by_first_name(self, first_name: str):
        return self.user_model.filter_by_keyword({"first_name": first_name})

def get_user_info(id: int):
    user_model = UserModel()
    return user_model.get_user_by_id(id)
