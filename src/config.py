__author__ = 'TianluWang'
#location: 47.88.87.104:/var/log/nginx
from datetime import datetime, timedelta

host = '47.88.85.15'
port = 8086
user = 'grafana'
password = '123456'
dbname = 'request_status'

time_node = current_time = datetime.now() - timedelta(minutes=5)
requests = ['/bc/shop/checkout/create_order', '/bc/shop/itemsCount',
            '/bc/shop/payment', '/bc/shop/cart/view', '/bc/shop/checkout/customer_info']
files = ['/var/log/nginx/access.log', '/var/log/nginx/access.log.1']  # TODO
# files = ['./data/access.log']