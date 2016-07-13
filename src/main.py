__author__ = 'TianluWang'
from requests_info import request_info
from static_files import static_files
from user import ip_category, login, signup
from json_body_makeup import json_body_makeup
from write_db import write_db
from config import files

json_bodys = []
measurements = []
values = []

# for every request
requests, avg_time, count, status = request_info(files)
for request in requests:
    request_split = request.split('/')
    measurements.append(request_split[-2]+'_'+request_split[-1])

for i in range(len(requests)):
    value = {}
    value['avg_time'] = avg_time[i]
    value['count'] = count[i]
    for key in status[i].keys():
        value[key] = status[i][key]
    values.append(value)

# static files
v_c, v_j, a_c, a_j = static_files(files)
value = {'vendor_css_avgtime': v_c[0], 'vendor_css_200': v_c[1],
         'vendor_css_304': v_c[2], 'vendor_js_avgtime': v_j[0],
         'vendor_js_200': v_j[1], 'vendor_js_304': v_j[2],
         'app_css_avgtime': a_c[0], 'app_css_200': a_c[1],
         'app_css_304': a_c[2], 'app_js_avgtime': a_j[0],
         'app_js_200': a_j[1], 'app_js_304': a_j[2]}

measurements.append('static_files')
values.append(value)

# user info
android_num, ios_v1_num, ios_v2_num, locations = ip_category(files)
measurements.append('user_info')
value = {'android_num': android_num,
         'ios_v1_num': ios_v1_num,
         'ios_v2_num': ios_v2_num,
         'US': locations.get('US', 0),
         'CA': locations.get('CA', 0),
         'AE': locations.get('AE', 0),
         'KW': locations.get('KW', 0),
         'AU': locations.get('AU', 0),
         'other': locations.get('other', 0)}
values.append(value)

locations, facebook, android, ios, time_avg = login(files)
measurements.append('login_info')
value = {'all': ios + android,
         'facebook': facebook,
         'ios': ios,
         'android': android,
         'time_avg': time_avg,
         'US': locations.get('US', 0),
         'CA': locations.get('CA', 0),
         'AE': locations.get('AE', 0),
         'KW': locations.get('KW', 0),
         'AU': locations.get('AU', 0),
         'other': locations.get('other', 0)}
values.append(value)

locations, android, ios, time_avg = signup(files)
measurements.append('sign_info')
value = {'all': ios + android,
         'ios': ios,
         'android': android,
         'time_avg': time_avg,
         'US': locations.get('US', 0),
         'CA': locations.get('CA', 0),
         'AE': locations.get('AE', 0),
         'KW': locations.get('KW', 0),
         'AU': locations.get('AU', 0),
         'other': locations.get('other', 0)}
values.append(value)

for i in range(len(measurements)):
    json_bodys.append(json_body_makeup(measurements[i], values[i]))

# for item in json_bodys:
#     print item
#     print '*****************'
write_db(json_bodys)




