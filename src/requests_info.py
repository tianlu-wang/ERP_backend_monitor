__author__ = 'TianluWang'
from config import time_node, requests
from json_body_makeup import json_body_makeup
from write_db import write_db
from user import ip_location
import re


def request_info(files):
    json_bodys = []
    pre_time = str(time_node)[:-7].replace(" ", "T")

    for file in files:
        with open(file) as f:
            for line in f.readlines():
                line_list = line.split(' ')
                if line_list[3][1:-7] < pre_time:
                    continue
                url = line_list[5]
                if '/bc/' not in url:
                    continue
                match = re.match(r'(.*)\d', url)
                if match is not None:
                    url_reverse = url[::-1]
                    pos = url_reverse.index('/')
                    url = url[:-(pos+1)]
                if url in requests:
                    url_split = url.split('/')
                    measurement = url_split[-2]+'_'+url_split[-1]
                    time = line_list[3][1:-7]
                    value = {}
                    value['ip'] = line_list[0]
                    value['country'] = ip_location(value['ip'])

                    value['status'] = line_list[7]
                    value['time_cost'] = line_list[-3]
                    value['Android'] = 'Android' in line
                    value['iPhone'] = 'iPhone' in line
                    value['url'] = line_list[5]
                    json_body = json_body_makeup(measurement, time, value)
                    json_bodys.append(json_body)

    return json_bodys
