# -*- coding:utf-8 -*-
# author: songyangyang
# time: 2018/10/19
import requests
import time
import random
from common.get_user_profile import get_user_id_by_phone
from tools.sql_handler import get_conn

def create_scene(name, latitude, longitude=0):
    """
    :param name: 
    :param latitude: 
    :param longitude: 
    :return: 
    """
    data = {
        "circleId": 1623375237,
        "cityName": "北京",
        "desc": "自动化测试现场{}".format(time.strftime("%Y-%m-%d %H%M%S", time.localtime(time.time()))),
        "duration": 1800,
        "isAdmin": 1,
        "latitude": 39.909421 + latitude,
        "longitude": 116.482198 + longitude,
        "name": name,
        "signinDistance": 10000,
        "userId": 1015964,
        "location": '{{"locationName": "北京市·华贸写字楼3座","locationAddress": "建国路xxx号"}}',
    }
    url = "http://dev.im-dangdang.com/circle/v1/scene"
    r = requests.get(url, params=data)
    return r.json()

def set_signin_expire(scene_id, user_id):
    with get_conn("circle") as cur:
        t = int(time.time()) + 5
        query_string = "update dd_circle_scene_member set signout_time={} where scene_id={} and user_id={} and is_delete=0".format(t, scene_id, user_id)
        cur.t_update(query_string)

def set_circle_to_default(circle_id):
    with get_conn("circle") as cur:
        query_string = "update dd_circle_special set is_delete=1 where circle_id={}".format(circle_id)
        cur.t_update(query_string)

def set_circle_to_train(circle_id):
    set_circle_to_default(circle_id)
    t = int(time.time())
    with get_conn("circle") as cur:
        query_string = "insert into dd_circle_special(circle_id, special_type, city_id, is_delete, create_time, update_time) values ({},10,0,0,{},{})".format(circle_id, t, t)
        cur.t_insert(query_string)

def set_circle_to_fly(circle_id):
    set_circle_to_default(circle_id)
    t = int(time.time())
    with get_conn("circle") as cur:
        query_string = "insert into dd_circle_special(circle_id, special_type, city_id, is_delete, create_time, update_time) values ({},2,0,0,{},{})".format(circle_id, t, t)
        cur.t_insert(query_string)

def scene_sign(scene_id, user_id, latitude=39.909166, longitude=116.482022):
    url = "http://dev.im-dangdang.com/circle/v1/scene/signin"
    data ={
        "latitude": latitude,
        "longitude": longitude,
        "sceneId": scene_id,
        "userId": user_id
    }
    resp = requests.post(url, data=data)
    return resp.json()
