# -*- coding:utf-8 -*-
# author: songyangyang
# time: 2018/10/17
from tools.sql_handler import get_conn

conn = get_conn("dangdang")

def create_diray():
    pass


def delete_diary_with_id(diary_id):
    with conn as cur:
        if isinstance(diary_id, (list, tuple)):
            for d_id in diary_id:
                query_string = "update dd_diary set is_delete=1 where diary_id={}".format(d_id)
                cur.t_update(query_string)
        else:
            query_string = "update dd_diary set is_delete=1 where diary_id={}".format(diary_id)
            cur.t_update(query_string)




def get_all_diary_id_without_delete_and_sync_to_space_of_user(user_id):
    with conn as cur:
        query_string = "select diary_id from dd_diary where user_id = {} and is_delete = 0 and is_sync_space = 1".format(user_id)
        result = conn.t_select(query_string)
        format_result = []
        for r in result:
            format_result.append(r[0])
        return format_result

if __name__ == "__main__":
    print(delete_diary_with_id(420))