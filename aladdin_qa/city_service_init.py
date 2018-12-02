# -*- coding:utf-8 -*-
# author: songyangyang
# time: 2018/11/14
from service.circle import Circle
from service.city_service import set_user_as_shop_operator, create_shop
from common.get_user_profile import get_user_id_by_phone
from service.city_service import create_shop, push_shop_notice
from tools.sql_handler import get_conn


if __name__ == "__main__":
    # for p in range(18900000000, 18900000021):
    #     print(Circle.join_circle_without_person_message(get_user_id_by_phone(p), 1623375257))
    #     print(set_user_as_shop_operator(1623375256, 1016064, get_user_id_by_phone(p)))

    with get_conn("circle") as cur:
        q = "select first_cid, second_cid, third_cid,third_cname from dd_circle_shop_meta_categoty" # where first_cid = 10015"
        result = cur.t_select(q)

    p = 18900000089
    for r in result:
        print(r)
        while True:
            try:
                print(create_shop(get_user_id_by_phone(p), 1623375255, r[0], r[1], r[2], 132, 132, "{}-{}-{}-{}".format(p, r[0], r[1], r[2])))
                break
            except:
                continue
        p += 1
with get_conn("circle") as cur:
    result = cur.t_select("select shop_id from dd_circle_shop where circle_id = 1623375252")
    n = 0.002
    l = 39.909420
    for i in result:
        cur.t_update("update dd_circle_shop set latitude={} where shop_id={}".format(l + n, i[0]))
        n += 0.002
