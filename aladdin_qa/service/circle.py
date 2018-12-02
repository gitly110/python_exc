# -*- coding:utf-8 -*-
# author: songyangyang
# time: 2018/10/16
from tools.sql_handler import MysqlConnectHandler
import requests
from common.get_user_profile import get_user_id_by_phone

class Circle:
    @staticmethod
    def join_circle_without_person_message(user_id, circle_id):
        url = "http://dev.im-dangdang.com/circle/v1/member/check/workLearn"
        data = {
            "sourceType": 0,
            "userId": user_id,
            "circleId": circle_id
        }
        resp = requests.post(url, data=data)
        return resp.json()

    @staticmethod
    def join_circle_with_person_message(user_id, circle_id):
        pass

if __name__ == "__main__":
    from common.get_user_profile import get_user_id_by_phone
    for p in range(18900000000, 18900000021):
        print(Circle.join_circle_without_person_message(get_user_id_by_phone(p), 1623375256))