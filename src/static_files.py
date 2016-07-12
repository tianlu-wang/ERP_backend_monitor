__author__ = 'TianluWang'
from config import time_node


def static_files(files):

    vendor_css = [0.00, 0, 0]  # avg_time, res_200, res_304
    vendor_js = [0.00, 0, 0]
    app_css = [0.00, 0, 0]
    app_js = [0.00, 0, 0]

    pre_time = str(time_node)[:-7].replace(" ", "T") + "+08:00"

    for file in files:
        with open(file) as f:
            for line in f.readlines():
                line_list = line.split(' ')
                if line_list[3][1:-1] < pre_time:
                    continue
                tmp = line_list[5].split('/')[-1]
                if 'vendor' in tmp and 'css' in tmp:
                    if line_list[7] == '200':
                        vendor_css[0] += float(line_list[-3])
                        vendor_css[1] += 1
                    elif line_list[7] == '304':
                        vendor_css[2] += 1
                elif 'vendor' in tmp and 'js' in tmp:
                    if line_list[7] == '200':
                        vendor_js[0] += float(line_list[-3])
                        vendor_js[1] += 1
                    elif line_list[7] == '304':
                        vendor_js[2] += 1
                elif 'app' in tmp and 'css' in tmp:
                    if line_list[7] == '200':
                        app_css[0] += float(line_list[-3])
                        app_css[1] += 1
                    elif line_list[7] == '304':
                        app_css[2] += 1
                elif 'app' in tmp and 'js' in tmp:
                    if line_list[7] == '200':
                        app_js[0] += float(line_list[-3])
                        app_js[1] += 1
                    elif line_list[7] == '304':
                        app_js[2] += 1
    if vendor_css[1] > 0:
        vendor_css[0] = vendor_css[0] * 1000 / vendor_css[1]
    else:
        vendor_css[0] = 0.0
    if vendor_js[1] > 0:
        vendor_js[0] = vendor_js[0] * 1000 / vendor_js[1]
    else:
        vendor_js[0] = 0.0
    if app_css[1] > 0:
        app_css[0] = app_css[0] * 1000 / app_css[1]
    else:
        app_css[0] = 0.0
    if app_js[1] > 0:
        app_js[0] = app_js[0] * 1000 / app_js[1]
    else:
        app_js[0] = 0.0
    return vendor_css, vendor_js, app_css, app_js