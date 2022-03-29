from datetime import datetime, timezone
from werkzeug.utils import find_modules, import_string
from flask import Blueprint, jsonify

from utils.request import ApiError

api_routes = bp = Blueprint("api_controller", __name__, url_prefix="/api")


@api_routes.route("/")
def base():
    return jsonify(
        {
            "status": 200,
            "message": "FLASK WORKSHOP API.",
            "timestamp": datetime.now(tz=timezone.utc).isoformat(timespec="seconds"),
        }
    )


@api_routes.route("/example-error")
def error():
    return ApiError("Test error", 400)


@api_routes.route("/health")
def health():
    return jsonify(
        {
            "status": 200,
            "message": "Healthy",
            "timestamp": datetime.now(tz=timezone.utc).isoformat(timespec="seconds"),
        }
    )


for name in find_modules("routes.api", include_packages=True):
    print("api: name:", name)
    mod = import_string(name)
    if hasattr(mod, "bp"):
        api_routes.register_blueprint(mod.bp)
