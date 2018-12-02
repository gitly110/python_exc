# -*- coding:utf-8 -*-
# author: songyangyang
# time: 2018/10/30
from tools.sql_handler import get_conn
import time
from tools.fker import fker
from tools.image_handler import get_picture_array_string
import requests

class Square:
    @staticmethod
    def add_square_search_suggest(suggestion, sort_num=1):
        t = int(time.time())
        with get_conn("dangdang") as cur:
            query_string = "insert into dd_square_search_suggestion(suggestion,sort_num,create_time,update_time) values('{suggestion}',{sort_num},{create_time},{update_time})".format(suggestion=suggestion, sort_num=sort_num, create_time=t, update_time=t)
            cur.t_insert(query_string)


    @staticmethod
    def add_square_share(user_id):
        url = "http://dev.im-dangdang.com/moments/v1/moments/add"
        data = {
            "longitude": fker.longitude(),
            "userId": user_id,
            "showAccess": 4,
            "content": fker.sentence(),
            "pictures": get_picture_array_string(2),
            "location": '{"address":"北京市朝阳区大望路华贸写字楼3座","name":"华贸中心"}',
            "latitude": fker.latitude()
        }
        resp = requests.post(url, data=data, verify=False)
        return resp

