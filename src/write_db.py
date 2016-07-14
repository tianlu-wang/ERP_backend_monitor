__author__ = 'TianluWang'
from influxdb import InfluxDBClient
from config import host, port, user, password, dbname
import logging
import traceback


def write_db(json_body):
    try:
        client = InfluxDBClient(host, port, user, password, dbname)
    except Exception, e:
        logging.error(traceback.format_exc())
        return
    try:
        client.write_points(json_body)
    except Exception, e:
        logging.error(traceback.format_exc())
        return