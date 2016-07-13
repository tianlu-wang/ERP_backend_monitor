__author__ = 'TianluWang'
from config import time_node


def theme(files):
    time_amount = 0.0
    count = 0
    status = {'200':0}

    pre_time = str(time_node)[:-7].replace(" ", "T") + "+08:00"

    for file in files:
        with open(file) as f:
            for line in f.readlines():
                line_list = line.split(' ')
                if line_list[3][1:-1] < pre_time:
                    continue
                url = line_list[5]
                if 'theme' in url:
                    if line_list[7] == '200':
                        time_amount += float(line_list[-3])
                        count += 1
                        status['200'] += 1
                    elif line_list[7] in status.keys():
                        status[line_list[7]] += 1
                    else:
                        status[line_list[7]] = 1
    if count > 0:
        avg_time = time_amount * 1000 /count
    else:
        avg_time = 0.0
    return avg_time, count, status
