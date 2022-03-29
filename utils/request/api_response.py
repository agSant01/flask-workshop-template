from flask import Response, json
from datetime import datetime, timezone


class ApiResponse:
    def __init__(self, data, status_code=200, headers={}) -> None:
        self.data = data
        self.status_code = status_code
        self.headers = headers

    def to_response(self):
        return Response(
            json.dumps(
                {
                    "data": self.data,
                    "error": False,
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
