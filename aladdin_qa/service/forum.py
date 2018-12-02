# -*- coding:utf-8 -*-
# author: songyangyang
# time: 2018/10/25
import requests
import time


def create_a_topic(circle_id, user_id, title=None):
    url = "http://dev.im-dangdang.com/circle/v1/forum/topic/publish"
    data = {
        "circleId": circle_id,
        "content": "<p>这是一条自动化脚本发送的论坛内容<p></p></p>",
        "detailImages": [],
        "title": title if title else time.strftime("%Y-%m-%d %H:%S:%M", time.localtime(time.time())),
        "userId": user_id
    }
    resp = requests.post(url, data=data)
    return resp.status_code

def delete_a_topic(circle_id, user_id, topic_id):
    url = "http://dev.im-dangdang.com/circle/v1/forum/topic/delete"
    data = {
        "circleId": circle_id,
        "isAdmin": 1,
        "status": 1,
        "topicId": topic_id,
        "userId": user_id
    }
    resp = requests.post(url, data=data)
    return resp.status_code