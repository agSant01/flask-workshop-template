from flask import Flask, g, render_template, request

from db import put_connection
from utils.request import ApiResponse, ApiError


class CustomFlask(Flask):
    """
    Overrides the make response method to add
    ApiResult and ApiException support
    """

    def make_response(self, rv):
        if isinstance(rv, ApiResponse):
            return rv.to_response()
        if isinstance(rv, ApiError):
            return rv.to_response()
        return Flask.make_response(self, rv)


app = CustomFlask(__name__, template_folder="views")


def register_error_handlers(app):
    """Register error handlers to flask application instance.

    Arguments:
        app {flask application} -- application instance
    """
    if app.config["ENV"] == "production":
        # if in production do not leak info
        @app.errorhandler(Exception)
        def handle_unexpected_error(error):
            if request.path.startswith("/api/"):
                print("[ERROR] Unexpected Error", error)
                return ApiError(
                    message="An unexpected error has occurred.",
                    status_code=500,
                )

    @app.errorhandler(400)
    @app.errorhandler(404)
    @app.errorhandler(405)
    def handle_api_error(error):
        print(error)
        if request.path.startswith("/api/"):
            if error.code == 400:
                return ApiError(message=str(error), status_code=400, type="Bad request")
            if error.code == 404:
                return ApiError(message=str(error), status_code=404, type="Not found")
            if error.code == 405:
                return ApiError(
                    message=str(error), status_code=405, type="Request method"
                )
        else:
            return error


# register all routes under controllers/
# register_api(app)
# register api error handlers
register_error_handlers(app)

# register app request cleanup
@app.teardown_request
def return_connection(_):
    # return connection
    if "db" in g:
        try:
            put_connection(g.db)
        except Exception as e:
            print("[DB-ERROR] putting connection...", e)


@app.route("/hello")
def hello_world():
    return render_template("hello-world.html")


from routes import pages_routes

app.register_blueprint(pages_routes)
