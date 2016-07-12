__author__ = 'TianluWang'
import socket


def json_body_makeup(measurement, value):
    json_body = [
        {
            "measurement": measurement,
            "tags": {
                "host": socket.gethostname()
            },
            "fields": value
        }
    ]
    return json_body
