# -*- coding:utf-8 -*-
# author: songyangyang
# time: 2018/11/13
from tools.sql_handler import get_conn
import time
import requests
from common.get_user_profile import get_user_id_by_phone
from tools.fker import fker
from tools.image_handler import get_random_image_url_from_oss_with_width_and_height, get_random_image_url_from_oss


def _generate_shop_bg_or_logo(keyword):
    image_url, width, height = get_random_image_url_from_oss_with_width_and_height(keyword)
    return '{{"height":"{}","width":"{}","picture":"{}", "pictureUrl": "{}"}}'.format(height, width, image_url, image_url)


def _generate_shop_pv_list():
    img1 = get_random_image_url_from_oss("人文地理")
    img2 = get_random_image_url_from_oss("山水风景")
    tmp = '[{{"pictureUrl":"{}","id":0,"image":{{"pictureUrl":"{}","picture":"{}","id":0,"width":"0","height":"0"}},"width":0,"height":0,"duration":0}},{{"pictureUrl":"{}","id":0,"image":{{"pictureUrl":"{}","picture":"{}","id":0,"width":"0","height":"0"}},"width":0,"height":0,"duration":0}}]'
    return tmp.format(img1, img1, img1, img2, img2, img2)


def create_shop(user_id, circle_id, cid1, cid2, cid3, p_id, c_id, shop_name):
    """
    创建商家，前提是当前用户必须有商家运营的权限
    :return: 
    """
    url = "http://dev.im-dangdang.com/circle2/v1/shop/add"
    data = {
        "pvList": _generate_shop_pv_list(),
        "cityId": c_id,
        "userId": user_id,
        "categoryId1": cid1,
        "circleId": circle_id,
        "provinceId": p_id,
        "categoryId2": cid2,
        "categoryId3": cid3,
        "specialType": 0,
        "shopDesc": fker.text(),
        "shopName": shop_name,
        "shopBg": _generate_shop_bg_or_logo("萌宠"),
        "logo": _generate_shop_bg_or_logo("城市风景"),
        'location': '{"address":"华贸写字楼3座建国路77号","longitude":116.4822,"city":"北京市","name":"华贸写字楼3座","latitude":39.90942,"ext":{"provienceName":"北京市","cityName":"北京市","businessArea":"大望路","countyName":"朝阳区"}}'
    }
    resp = requests.post(url, data=data)
    return resp.json()

def set_user_as_shop_operator(circle_id, admin_id, user_id):
    url = "http://dev.im-dangdang.com/circle2/v1/shop/operation/add"
    data = {
        "circleId": circle_id,
        "isAdmin": 1,
        "operaUserId": user_id,
        "userId": admin_id
    }
    resp = requests.post(url, data=data)
    return resp.json()


def push_shop_notice(shop_id, title):
    with get_conn("circle") as cur:
        t = int(time.time())
        query_string = "insert into dd_circle_shop_notice(shop_id,title,content,create_time,update_time) values ({}, '{}', '{}', {}, {})".format(shop_id, title, "哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈", t, t)
        cur.t_insert(query_string)


def push_market_notice(market_id, title):
    with get_conn("circle") as cur:
        t = int(time.time())
        query_string = "insert into dd_circle_shop_notice(title,content,create_time,update_time,market_id) values ('{}', '{}', {}, {}, {})".format(title, "哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈", t, t, market_id)
        cur.t_insert(query_string)

