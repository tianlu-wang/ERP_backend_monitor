__author__ = 'TianluWang'
import socket


def json_body_makeup(measurement, time, value):
    json_body = [
        {
            "measurement": measurement,
            "tags": {
                "host": socket.gethostname()
            },
            "time": time,
            "fields": value
        }
    ]
    return json_body
