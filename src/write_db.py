__author__ = 'TianluWang'
from influxdb import InfluxDBClient
from config import host, port, user, password, dbname
import logging
import traceback


def write_db(json_bodys):
    try:
        client = InfluxDBClient(host, port, user, password, dbname)
    except Exception, e:
        logging.error(traceback.format_exc())
        return

    for json_body in json_bodys:
        try:
            client.write_points(json_body)
        except Exception, e:
            logging.error(traceback.format_exc())
            return

    return