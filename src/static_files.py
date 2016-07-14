__author__ = 'TianluWang'
from config import time_node
from json_body_makeup import json_body_makeup
from write_db import write_db
from user import ip_location


def static_files(files):

    pre_time = str(time_node)[:-7].replace(" ", "T")

    for file in files:
        with open(file) as f:
            for line in f.readlines():
                line_list = line.split(' ')
                if line_list[3][1:-7] < pre_time:
                    continue
                tmp = line_list[5].split('/')[-1]
                if 'vendor' in tmp or 'app' in tmp:
                    measurement = 'static files'
                    time = line_list[3][1:-7]
                    value = {}
                    value['ip'] = line_list[0]
                    value['country'] = ip_location(value['ip'])
                    value['status'] = line_list[7]
                    value['time'] = line_list[-3]
                    value['Android'] = 'Android' in line
                    value['iPhone'] = 'iPhone' in line
                    value['url'] = line_list[5]
                    json_body = json_body_makeup(measurement, time, value)
                    write_db(json_body)
    return
