# https://www.i2tutorials.com/python-super-with-__init__-methods/#:~:text=The%20%E2%80%9C__init__%E2%80%9D%20is,the%20attributes%20of%20the%20class.&text=The%20super()%20function%20allows,the%20base%20class%20name%20explicitly.

from flask import Response, json
from datetime import datetime, timezone


class ApiError:
    def __init__(self, message, status_code, headers={}, type=None) -> None:
        self.error_message = message
        self.status_code = status_code
        self.headers = headers
        self.type = type

    def to_response(self):
        return Response(
            json.dumps(
                {
                    "message": self.error_message,
                    "error": True,
                    "type": self.type,
                    "status": self.status_code,
                    "timestamp": datetime.now(tz=timezone.utc).isoformat(
                        timespec="seconds"
                    ),
                }
            ),
            headers=self.headers,
            status=self.status_code,
            mimetype="application/json",
        )
