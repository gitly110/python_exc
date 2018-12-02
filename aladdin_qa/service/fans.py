# -*- coding:utf-8 -*-
# author: songyangyang
# time: 2018/10/22
from tools.sql_handler import get_conn
import time
import requests


def update_fans_activity_deadline(deadline, activity_id):
    with get_conn("circle") as cur:
        query_string = "update dd_circle_fans_activity set deadline = {} where activity_id = {}".format(deadline, activity_id)
        cur.t_update(query_string)


def update_fans_activity_member_list(create_time, activity_id, member_id):
    with get_conn("circle") as cur:
        query_string = "update dd_circle_fans_activity_member set create_time = {} where activity_id = {} and user_id = {}".format(create_time, activity_id, member_id)
        cur.t_update(query_string)



"""
场景1:  活动已经结束
场景2:  活动结束时间为当天的23:59:59
场景3:  活动结束时间为第二天凌晨的：00:00:00
场景4:  活动结束时间为第二天凌晨的：12:00:00
场景5:  活动结束时间为2018年12月31日  23:59:59
场景6:  活动结束时间为2019年1月1日  00:00:00
场景7:  活动结束时间为2017年12月31日 23:59:59
"""
    # activity_id = 36
    # times = [int(time.time() - 1), 1540223999, 1540224000, 1540267200, 1546271999, 1546272000]
    # # time1 = 1540224072
    # for time1 in times:
    #     update_fans_activity_deadline(time1, activity_id)
    #     url = "http://dev.im-dangdang.com/circle4/v1/fans/activity/list"
    #     resp = requests.get(url)
    #     print(resp.json()["data"]["activityList"][1]["fmtDeadline"])
    #     time.sleep(1)
"""
场景1:  用户参加活动的时间离当前时间小于1分钟
场景2:  用户参加活动的时间离当前时间等于1分钟
场景3:  用户参加活动的时间离当前时间为1分1秒钟
场景4:  用户参加活动的时间离当前时间为60分钟整
场景5:  用户参加活动的时间离当前时间1.5小时
场景6:  用户参加活动的时间离当前时间3小时
场景7:  用户参加活动的时间离当前时间昨天的凌晨00:00
场景8: 用户参加活动的时间离当前时间昨天的23:59:59秒
场景9: 用户参加活动的时间离当前时间前天的凌晨00:00
场景10:  用户参加活动的时间离当前时间前天的23:59:59
场景11:  用户参加活动的时间离当前时间5天前的12:00:00
场景12:  用户参加活动的时间为2017年10月1日 00:00:00
"""
if __name__ == "__main__":
    times = [int(time.time() - 59), int(time.time() - 60), int(time.time() - 61), int(time.time() - 60*60), int(time.time() - 1.5*60*60), int(time.time() - 3*60*60), 1540051200, 1540137599, 1539964800, 1540051199, 1539791999, 1506873599]
    for t in times:
        update_fans_activity_member_list(t, 36, 1016017)
        url = "http://dev.im-dangdang.com/circle4/v1/fans/activity/member/list?activityId=36&pageRows=10"
        resp = requests.get(url).json()
        print(resp["data"]["memberList"][0]["fmtCreateTime"])
        time.sleep(1)