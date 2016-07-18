__author__ = 'TianluWang'
from requests_info import request_info
from static_files import static_files
from write_db import write_db
from user import app_open
from config import files

json_bodys1 = request_info(files)
json_bodys2 = app_open(files)
json_bodys3 = static_files(files)

write_db(json_bodys1 + json_bodys2 + json_bodys3)






