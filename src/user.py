__author__ = 'TianluWang'
from config import time_node
from geoip import geolite2
from json_body_makeup import json_body_makeup
from datetime import datetime, timedelta
import logging


# find out user is android or ios
def app_open(files):
    json_bodys = []
    pre_time = str(time_node)[:-7].replace(" ", "T")

    for file in files:
        with open(file) as f:
            for line in f.readlines():
                line_list = line.split(' ')
                if line_list[3][1:-7] < pre_time:
                    continue
                url = line_list[5]
                if '/club_factory/init' in url:
                    measurement = 'app_location'
                    CST_time_s = line_list[3][1:-7].replace("T", " ")
                    CST_time = datetime.strftime(CST_time_s, '%Y-%m-%d %H:%M:%S')
                    UTC_time = CST_time - timedelta(hours=8)
                    time = str(UTC_time).replace(" ", "T")
                    value = {}
                    value['ip'] = line_list[0]
                    value['country'] = ip_location(value['ip'])
                    value['status'] = line_list[7]
                    value['time_cost'] = line_list[-3]
                    value['Android'] = 'Android' in line
                    value['iPhone'] = 'Club_Factory_UIWebView' in line
                    value['url'] = line_list[5]
                    json_body = json_body_makeup(measurement, time, value)
                    json_bodys.append(json_body)

    return json_bodys


# find out the location of customer
def ip_location(ip):
    match = geolite2.lookup(ip)
    try:
        country = match.country
        return country
    except Exception,e:
        logging.info(ip)
        return None