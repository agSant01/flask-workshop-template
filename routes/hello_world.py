from datetime import datetime
from flask import Blueprint, render_template


bp = Blueprint("pages", import_name=__name__, url_prefix="/hello-world")


@bp.route("/", methods=["GET"])
@bp.route("/<string:name>", methods=["GET"])
def index(name=None):
    data = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        + " or "
        + datetime.now().strftime("%l:%M%p %Z on %b %d, %Y"),
        "name": name,
    }
    return render_template("hello-world.html", **data)
