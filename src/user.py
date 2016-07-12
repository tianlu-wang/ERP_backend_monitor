__author__ = 'TianluWang'
from config import time_node
from geoip import geolite2
import logging

# find out user is android or ios
def ip_category(files):
    pre_time = str(time_node)[:-7].replace(" ", "T") + "+08:00"

    android_num = 0
    android_ips = []
    ios_v1_num = 0
    ios_v1_ips = []
    ios_v2_num = 0
    ios_v2_ips = []
    for file in files:
        with open(file) as f:
            for line in f.readlines():
                line_list = line.split(' ')
                if line_list[3][1:-1] < pre_time:
                    continue
                if '/club_factory/init' in line:
                    if line_list[7] != '200':
                        continue
                    if 'Android' in line:
                        if line_list[0] in android_ips:
                            continue
                        android_num += 1
                        android_ips.append(line_list[0])
                    elif 'Club_Factory_UIWebView' in line:
                        if 'version=1.3.0' in line:
                            if line_list[0] in ios_v1_ips:
                                continue
                            ios_v1_num += 1
                            ios_v1_ips.append(line_list[0])
                        elif 'version=1.3.1' in line:
                            if line_list[0] in ios_v2_ips:
                                continue
                            ios_v2_num += 1
                            ios_v2_ips.append(line_list[0])
    locations = ip_location(android_ips+ios_v1_ips+ios_v2_ips)
    return android_num, ios_v1_num, ios_v2_num, locations


# find out the location of customer
def ip_location(ips):
    locations = {}
    for ip in ips:
        match = geolite2.lookup(ip)
        try:
            country = match.country
            if country in locations.keys():
                locations[country] += 1
            else:
                locations[country] = 1
        except Exception,e:
            logging.info(ip)

    other = 0
    for key in locations.keys():
        if key not in ['AU', 'CA', 'AE', 'KW', 'US']:
            other += locations[key]
    locations['other'] = other
    return locations


def login(files):
    pre_time = str(time_node)[:-7].replace(" ", "T") + "+08:00"

    ips = []
    is_facebook = 0
    is_ios = 0
    is_android = 0
    time_avg = 0.0
    for file in files:
        with open(file) as f:
            for line in f.readlines():
                line_list = line.split(' ')
                if line_list[3][1:-1] < pre_time:
                    continue
                if '/bc/auth/login' in line or '/bc/auth/facebook/login' in line:
                    if line_list[7] != '200':
                        continue
                    if line_list[0] in ips:
                        continue
                    ips.append(line_list[0])
                    if 'facebook' in line:
                        is_facebook +=1
                    if 'Android' in line:
                        is_android += 1
                    if 'iPhone' in line:
                        is_ios += 1

                    time_avg += float(line_list[-3])
    if len(ips) == 0:
        time_avg = 0
    else:
        time_avg = time_avg * 1000/len(ips)
    locations = ip_location(ips)
    return locations, is_facebook, is_android, is_ios, time_avg


def signup(files):
    pre_time = str(time_node)[:-7].replace(" ", "T") + "+08:00"

    ips = []
    is_ios = 0
    is_android = 0
    time_avg = 0.0
    for file in files:
        with open(file) as f:
            for line in f.readlines():
                line_list = line.split(' ')
                if line_list[3][1:-1] < pre_time:
                    continue
                if '/bc/auth/signup' in line:
                    if line_list[7] != '200':
                        continue
                    if line_list[0] in ips:
                        continue
                    ips.append(line_list[0])
                    if 'Android' in line:
                        is_android += 1
                    if 'iPhone' in line:
                        is_ios += 1

                    time_avg += float(line_list[-3])
    if len(ips) == 0:
        time_avg = 0
    else:
        time_avg = time_avg * 1000/len(ips)
    locations = ip_location(ips)
    return locations, is_android, is_ios, time_avg