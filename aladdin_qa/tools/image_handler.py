# -*- coding:utf-8 -*-
# author: songyangyang
# time: 2018/10/24
import requests
import random
import os
from tools.upload_handler import upload_img_to_oss
import time
from PIL import Image

def download_image(url, fpath=None):
    if not fpath:
        image_tmp_dir = os.path.dirname(os.path.dirname(__file__)) + "/tmp"
        with open(image_tmp_dir + "/tmp.jpg", "wb") as f:
            content = requests.get(url).content
            f.write(content)
    else:
        with open(fpath + "/{}.jpg".format(int(time.time())), "wb") as f:
            content = requests.get(url).content
            f.write(content)

def get_random_image_url_from_oss(keyword="人物头像"):
    download_image(get_random_image_url_from_baidu_with_keyword(keyword))
    return upload_img_to_oss(os.path.dirname(os.path.dirname(__file__)) + "/tmp/tmp.jpg")

def get_random_image_url_from_baidu_with_keyword(keyword):
    pn = random.randint(1, 1000)
    url = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&fp=result&queryWord={}&cl=2&lm=-1&word={}&cg=head&pn={}&rn=30".format(keyword,keyword, pn)
    resp = requests.get(url, verify=False).json()
    for i in range(10):
        try:
            result = resp["data"][random.randint(0, 30)]["thumbURL"]
            break
        except KeyError:
            continue
    return result


def get_random_image_url_from_oss_with_width_and_height(keyword="人物头像"):
    download_image(get_random_image_url_from_baidu_with_keyword(keyword))
    image_path = os.path.dirname(os.path.dirname(__file__)) + "/tmp/tmp.jpg"
    width, height = get_width_and_height_of_picture(image_path)
    image_url = upload_img_to_oss(image_path)
    return image_url, width, height


def get_width_and_height_of_picture(image_path):
    image = Image.open(image_path)
    return image.size

def get_picture_array_string(num):
    result = []
    for i in range(num):
        tmp = '{{"height":"{},"width":"{}","picture":"{}"}}'.format(*get_random_image_url_from_oss_with_width_and_height())
        result.append(tmp)
    t = ",".join(result)
    return "[" + t + "]"


if __name__ == "__main__":
    print(get_random_image_url_from_oss_with_width_and_height("明星头像"))
