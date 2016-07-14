__author__ = 'TianluWang'
#location: 47.88.87.104:/var/log/nginx
from datetime import datetime, timedelta

host = '47.88.85.15'
port = 8086
user = 'grafana'
password = '123456'
dbname = 'erp_backend'

time_node = current_time = datetime.now() - timedelta(minutes=10)  # TODO
requests = ['/bc/shop/checkout/create_order',
            '/bc/shop/itemsCount',
            '/bc/shop/payment',
            '/bc/shop/cart/view',
            '/bc/shop/checkout/customer_info',
            '/bc/user_center/orders',
            '/bc/payment/stripe/ipn',
            '/bc/shop/items',
            '/bc/shop/payment/transaction',
            '/bc/user_center/contact_info_update',
            '/bc/auth/reset_password',
            '/bc/user_center/center'
            '/bc/shop/product/content',
            '/bc/shop/product/favorites/delete',
            '/bc/shop/payment/new_validate',
            '/bc/shop/cart/update_json',
            '/bc/shop/category',
            '/bc/auth/logout',
            '/bc/user_center/get_tracking_info',
            '/bc/shop/tracking_last_order/',
            '/bc/shop/product/items',
            '/bc/shop/product/favorites/add',
            '/bc/shop/cart/delete',
            '/bc/shop/product/favorites/view',
            '/bc/shop/payment/tx',
            '/bc/shop/payment/order',
            '/bc/auth/login',
            '/bc/auth/facebook/login',
            '/bc/auth/signup']
files = ['/var/log/nginx/access.log', '/var/log/nginx/access.log.1']  # TODO
# files = ['./data/access.log']