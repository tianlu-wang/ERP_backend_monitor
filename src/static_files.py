__author__ = 'TianluWang'
from config import time_node
from json_body_makeup import json_body_makeup
from datetime import datetime, timedelta
from user import ip_location


def static_files(files):
    json_bodys = []

    pre_time = str(time_node)[:-7].replace(" ", "T")

    for file in files:
        with open(file) as f:
            for line in f.readlines():
                line_list = line.split(' ')
                if line_list[3][1:-7] < pre_time:
                    continue
                tmp = line_list[5].split('/')[-1]
                if 'vendor' in tmp or 'app' in tmp:
                    measurement = 'static_files'
                    CST_time_s = line_list[3][1:-7].replace("T", " ")
                    CST_time = datetime.strptime(CST_time_s, '%Y-%m-%d %H:%M:%S')
                    UTC_time = CST_time - timedelta(hours=8)
                    time = str(UTC_time).replace(" ", "T")
                    value = {}
                    value['ip'] = line_list[0]
                    value['country'] = ip_location(value['ip'])
                    value['status'] = line_list[7]
                    value['time_cost_new'] = int(line_list[-3])
                    value['Android'] = 'Android' in line
                    value['iPhone'] = 'iPhone' in line
                    if 'Android' in line:
                        value['ios_or_an'] = 0
                    else:
                        value['ios_or_an'] = 1
                    value['url'] = line_list[5]
                    json_body = json_body_makeup(measurement, time, value)
                    json_bodys.append(json_body)

    return json_bodys
