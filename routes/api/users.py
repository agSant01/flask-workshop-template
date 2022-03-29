from flask import Blueprint
from utils.request import ApiResponse, ApiError
from controllers import users as UserController

bp = Blueprint("users", __name__, url_prefix="/users")


@bp.route("/", methods=["GET"])
def get_users():
    return ApiResponse(UserController.get_users())


@bp.route("/<int:id>", methods=["GET"])
def get_user(id: int):
    user_info = UserController.get_user_info(id)

    if user_info is None:
        return ApiError("User not found", 400)

    return ApiResponse(user_info)
