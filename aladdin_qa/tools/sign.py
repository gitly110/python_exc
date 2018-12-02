# -*- coding:utf-8 -*-
# author: songyangyang
# time: 2018/11/5
import hashlib
from urllib.request import unquote

def request_query_to_dict(query_string):
    tmp_array = query_string.split("&")
    result = {}
    for ele in tmp_array:
        k, v = ele.split("=", 2)
        result[k] = unquote(v)
    return result


def dict_to_request_query(query_dict):
    tmp = []
    for k in sorted(query_dict.keys()):
        tmp.append("{}={}".format(k, query_dict[k]))
    return "&".join(tmp)


def request_query_to_dict_remove_sign(query_string):
    tmp_dict = request_query_to_dict(query_string)
    if "sign" in tmp_dict:
        del tmp_dict["sign"]
    return tmp_dict


def get_md5(string):
    my_md5 = hashlib.md5()
    my_md5.update(string.encode("utf-8"))
    return my_md5.hexdigest()

def get_sign(param):
    if isinstance(param, str):
        t = request_query_to_dict_remove_sign(param)
        md5_sign = get_md5(dict_to_request_query(t))
        t.update({"sign": md5_sign})
        return t
    elif isinstance(param, dict):
        md5_sign = get_md5(dict_to_request_query(param))
        param.update({"sign": md5_sign})
        return param
    else:
        raise("the param to be signed is wrong")

if __name__ == "__main__":
    s = "platform=android&lookedUserId=1000014&channelId=a100001&sign=8b83d5218e662cfa2873086fccb580a7&cuid=fdb977b6ba7b503c&appVersion=1.3.63&userId=1375675&pageRows=10&ddtoken=5%2B9XQOpxoFZDDDrC%2FNyUrbAaS5BuhRJfrJnCkw%2B1SOctYGPG5A9nv34WYMJMX9qFsg47xcng7fWUrWaTDeNYiHJxeXboMdn3SLH1jYVZboU%3D&ydId=3H8wvbiQs5QEM7yHIpHeiYB6eb%2FeOJONk2%2FZObvJve1HLvIpZwEAAA%3D%3D&buildVersion=1.3.63&lastRowId=0"
    print(get_sign(s))