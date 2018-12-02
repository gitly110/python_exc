# -*- coding:utf-8 -*-
# author: songyangyang
# time: 2018/10/14
from tools.sql_handler import get_conn

def get_regist_code(phone_number):
    query_string = "select val_code from dd_code where phone = {}".format(phone_number)
    with get_conn("dangdang") as cur:
        result = cur.t_select(query_string)
        return result[0][0]
