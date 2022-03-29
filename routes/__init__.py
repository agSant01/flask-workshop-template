from flask import Blueprint
from werkzeug.utils import find_modules, import_string


pages_routes = Blueprint("pages", import_name=__name__)

for name in find_modules("routes", include_packages=True):
    print("name:", name)
    mod = import_string(name)
    if hasattr(mod, "bp"):
        pages_routes.register_blueprint(mod.bp)
