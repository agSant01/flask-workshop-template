from flask import Blueprint, request
from utils.request import ApiResponse, ApiError
from controllers.users import UserController

bp = Blueprint("users", __name__, url_prefix="/users")


@bp.route("/", methods=["GET"])
def get_users():
    user_controller = UserController()
    user_list = user_controller.get_users()
    return ApiResponse(user_list)


@bp.route("/<int:id>", methods=["GET"])
def get_user(id: int):
    user_controller = UserController()

    user_info = user_controller.get_user_info(id)

    if user_info is None:
        return ApiError("User not found", 400)

    return ApiResponse(user_info)
