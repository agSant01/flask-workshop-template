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


@bp.route("/", methods=["POST"])
def create_user():

    user_data: dict = request.get_json()
    print(user_data)

    # verify user data:
    if user_data.get("password", None) is None:
        return ApiError("Missing password", 400, type="Invalid user object")

    """
    first name
    last name
    age
    email
    password
    """

    user_controller = UserController()
    user_info = user_controller.create_user(user_data)

    return ApiResponse({"message": "User created", "user": user_info}, status_code=201)


VALID_SEARCH_KEYS = ["firstname", "lastname"]


@bp.route("/search", methods=["GET"])
def search():
    query_params = request.args
    print("query params", query_params)

    allowed_ = dict(filter(lambda qp: qp[0].lower() in VALID_SEARCH_KEYS, query_params.items()))
    user_controller = UserController()

    user_list = user_controller.filter_users(allowed_)

    return ApiResponse(user_list)
