# -*- coding:utf-8 -*-
# author: songyangyang
# time: 2018/11/1
from tools.sql_handler import get_conn


def get_user_id_by_phone(phone):
    with get_conn("dangdang") as cur:
        string_query = "select user_id from dd_user where user_phone = {}".format(phone)
        result = cur.t_select(string_query)
        return result[0][0]
