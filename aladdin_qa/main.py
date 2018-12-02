# -*- coding:utf-8 -*-
# author: songyangyang
# time: 2018/10/30
from tools.sql_handler import get_conn
import time
import requests

"""
scene_id=91679 and user_id=1016064
circle=1623375249
"""


def set_signin_expire(scene_id, user_id):
    with get_conn("circle") as cur:
        t = int(time.time()) + 5
        query_string = "update dd_circle_scene_member set signout_time={} where scene_id={} and user_id={} and is_delete=0".format(
            t, scene_id, user_id)
        cur.t_update(query_string)


def set_circle_to_default(circle_id):
    with get_conn("circle") as cur:
        query_string = "update dd_circle_special set is_delete=1 where circle_id={}".format(circle_id)
        cur.t_update(query_string)


def set_circle_to_train(circle_id):
    set_circle_to_default(circle_id)
    t = int(time.time())
    with get_conn("circle") as cur:
        query_string = "insert into dd_circle_special(circle_id, special_type, city_id, is_delete, create_time, update_time) values ({},10,0,0,{},{})".format(
            circle_id, t, t)
        cur.t_insert(query_string)


def set_circle_to_fly(circle_id):
    set_circle_to_default(circle_id)
    t = int(time.time())
    with get_conn("circle") as cur:
        query_string = "insert into dd_circle_special(circle_id, special_type, city_id, is_delete, create_time, update_time) values ({},2,0,0,{},{})".format(
            circle_id, t, t)
        cur.t_insert(query_string)


def scene_sign(scene_id, user_id, latitude=39.909166, longitude=116.482022):
    url = "http://dev.im-dangdang.com/circle/v1/scene/signin"
    data = {
        "latitude": latitude,
        "longitude": longitude,
        "sceneId": scene_id,
        "userId": user_id
    }
    resp = requests.post(url, data=data)
    return resp.json()


if __name__ == "__main__":
    # set_circle_to_fly(1623375249)
    # set_circle_to_train(1623375249)
    set_circle_to_default(1623375249)
    # set_signin_expire(91679, 1016064)
    # set_signin_expire(91679, 1016065)
    # for
