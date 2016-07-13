__author__ = 'TianluWang'

import re

requests = {}
with open('/Users/koala/PycharmProjects/ERP_backend_monitor/data/access.log') as f:
    for line in f.readlines():
        line_list = line.split(' ')
        url = line_list[5]
        if '/bc/' not in url:
            continue
        match = re.match(r'(.*)\d', url)
        if match is not None:
            url_reverse = url[::-1]
            pos = url_reverse.index('/')
            url = url[:-(pos+1)]
        if url in requests.keys():
            requests[url] += 1
        else:
            requests[url] = 1

for item in requests:
    print item
    print requests[item]
    print '**********'