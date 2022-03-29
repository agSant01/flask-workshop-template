from models.user_model import UserModel


def get_users():
    user_model = UserModel()
    return user_model.get_all_users()


def get_user_info(id: int):
    user_model = UserModel()
    return user_model.get_user_by_id(id)
