# -*- coding:utf-8 -*-
# author: songyangyang
# time: 2018/10/15
import oss2
import time
import os
import hashlib
import requests


def upload_img_to_oss(img_path):
    file_base_url = "http://s1.im-dangdang.com/"
    now = time.localtime(time.time())
    year, month, day = now.tm_year, now.tm_mon, now.tm_mday
    auth = oss2.Auth("UtqbxRCdYazB7oGW", "WXvBPebVPGlXAWfGdQrXFyDZCorSmG")
    bucket = oss2.Bucket(auth, "http://oss-cn-beijing.aliyuncs.com", "dangdangshejiao")
    name = "dev/{year}{month}{day}/{md5}.{itype}".format(year=year, month=month, day=day, md5=_get_md5_of_file(img_path), itype=img_path.split(".")[1])
    if _check_file_exist_on_oss(name):
        return file_base_url + name
    else:
        result = bucket.put_object_from_file(name, img_path)
        return file_base_url + name


def _get_md5_of_file(file_path):
    if os.path.exists(file_path) and os.path.isfile(file_path):
            m = hashlib.md5()
            a_file = open(file_path, 'rb')  # 需要使用二进制格式读取文件内容
            m.update(a_file.read())
            a_file.close()
            return m.hexdigest()


def _check_file_exist_on_oss(file_key):
    url = "http://s1.im-dangdang.com/" + file_key
    resp_code = requests.head(url, verify=False).status_code
    if resp_code == 200:
        return True
    else:
        return False