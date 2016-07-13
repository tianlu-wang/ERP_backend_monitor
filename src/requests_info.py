__author__ = 'TianluWang'
from config import time_node, requests
import re

def request_info(files):

    time_amount = [0.0] * len(requests)
    count = [0] * len(requests)
    status = {}
    for i in range(len(requests)):
        status[i] = {'200': 0}

    pre_time = str(time_node)[:-7].replace(" ", "T") + "+08:00"

    for file in files:
        with open(file) as f:
            for line in f.readlines():
                line_list = line.split(' ')
                if line_list[3][1:-1] < pre_time:
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
                    index = requests.index(url)
                    if line_list[7] == '200':
                        time_amount[index] += float(line_list[-3])
                        count[index] += 1
                        status[index]['200'] += 1
                    elif line_list[7] in status[index].keys():
                        status[index][line_list[7]] += 1
                    else:
                        status[index][line_list[7]] = 1
    avg_time = []
    for i in range(len(requests)):
        if count[i] > 0:
            avg_time.append(time_amount[i] * 1000 /count[i])
        else:
            avg_time.append(0.0)
    return requests, avg_time, count, status
