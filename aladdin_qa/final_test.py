# -*- coding:utf-8 -*-
# author: songyangyang
# time: 2018/11/15
from tools.sql_handler import get_conn
from service.city_service import push_shop_notice, push_market_notice, create_shop
import random
from common.get_user_profile import get_user_id_by_phone


"""
阿拉丁05
"""
city_infos = {
    10001: (131, 131),  #北京
    10002: (132, 132),  #重庆
    10003: (7, 197),     #清远市
    10004: (7, 200),     #河源市
    10005: (30, 210),  #开封市
    10006: (30, 213),  #平顶山市
    10007: (26, 219),  #常德市
    10008: (26, 221),  #娄底市
    10009: (32, 239), #巴中市
    10010: (32, 241), #广安市
    10011: (23, 252), #黄山市
    10012: (23, 253),  #淮北市
    10013: (15, 270),   #宜昌市
    10014: (15, 271),   #黄冈市
    10015: (31, 278)  #宜春市
}
if __name__ == "__main__":
    # with get_conn("circle") as cur:
    #     q = "select first_cid, second_cid, third_cid,third_cname from dd_circle_shop_meta_categoty"  # where first_cid = 10015"
    #     result = cur.t_select(q)
    #
    # p = 18900000000
    # for r in result:
    #     while True:
    #         try:
    #             print(create_shop(get_user_id_by_phone(p), 1623375252, r[0], r[1], r[2], city_infos[r[0]][0], city_infos[r[0]][1], "{}-{}-{}-{}".format(p, r[0], r[1], r[2])))
    #             break
    #         except:
    #             continue
    #     p += 1
    # push_shop_notice(1991, "公告测试，哈哈哈！！哈哈哈，呵呵呵，呜呜呜哈哈哈！！！哈哈哈，呵呵呵，呜呜呜哈哈哈")
    import time
    for i in range(1, 50):
        push_market_notice(39, "{}公告测试，哈哈哈！！哈哈哈，呵呵呵，呜呜呜哈哈哈".format(i))
        time.sleep(1)

