# -*- coding:utf-8 -*-
# author: songyangyang
# time: 2018/10/16
# -*- coding:utf-8 -*-
# author: songyangyang
# time: 2018/10/14
from tools.sql_handler import get_conn

def update_regist(email):
    query_string = "update dd_circle set status=1,regist_step=0,circle_type=1 where email='{}'".format(email)
    with get_conn("circle") as cur:
        cur.t_update(query_string)

if __name__ == "__main__":
    print(update_regist("test4@songyangyang.com"))