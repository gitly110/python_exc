# -*- coding:utf-8 -*-
# author: songyangyang
# time: 2018/10/30
import requests
from faker import Faker
import time
from tools.image_handler import get_random_image_url_from_oss
import time

fker = Faker(locale="zh_CN")

class Console:
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.header = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
        }
        self.init_header_with_token()

    def init_header_with_token(self):
        url = "http://devgzq.im-dangdang.com/cp/login?account={}&password={}&rememberPwd=1".format(self.user, self.password)
        resp = requests.get(url)
        self.ctoken = resp.json()["data"]["ctoken"]
        self.header.update({"Cookie": "account={};ctoken={}".format(self.user, self.ctoken)})

    def create_material(self):
        """
        在素材库中创建一个素材
        :return: 
        """
        image_url = get_random_image_url_from_oss("山水风景")
        # image_url = "http://s1.im-dangdang.com/dev/20181030/DzKw6XQeFS.JPG"
        url = "http://devgzq.im-dangdang.com/cp/material/news"
        data = {
            "title": fker.words(),
            "source": fker.name(),
            "detail": "<p>{}</p>".format(fker.text()),
            "closeComment": 0,
            "formatNewsTime": time.strftime("%Y-%m-%d", time.localtime(time.time())),
            "coverImage": '{{"picture":"{}","width":"640","height":"640"}}'.format(image_url),
            "cover": image_url
        }
        resp = requests.post(url, headers=self.header, data=data, verify=False)
        return resp.json()["data"]["materialId"]

    def publish_article(self, material_id, item_id):
        """
        发布素材库中的一片文章
        :return: 
        """
        url = "http://devgzq.im-dangdang.com/cp/article"
        data = {
            "materialIds": "[{}]".format(material_id),
            "showAccess": 1,
            "itemId": item_id,
            "location": "",
            "latitude": "",
            "longitude": ""
        }
        resp = requests.post(url, headers=self.header, data=data, verify=False)
        return resp.text


    def create_album(self, album_name):
        url = "http://devgzq.im-dangdang.com/cp/album"
        data = {
            "albumName": album_name,
            "albumDesc": fker.sentence(),
            "pictures": '[{{"width":"1200","height":"800","picture":"{}"}}]'.format(get_random_image_url_from_oss("山水风景")),
            "coverImage": '{{"width":"1200","height":"800","picture":"{}"}}'.format(get_random_image_url_from_oss("山水风景")),
            "location": "",
            "longitude": "",
            "latitude": "",
            "showAccess": 1,
            "switchFcs": 1
        }
        resp = requests.post(url, headers=self.header, data=data, verify=False)
        return resp.json()

    def add_relatite_circle(self, relate_circle_id):
        url = "http://devgzq.im-dangdang.com/cp/binding/add"
        data = {
            "accountNums": '["{}"]'.format(relate_circle_id)
        }
        resp = requests.post(url, headers=self.header, data=data)
        return resp.json()

    def create_scene(self):
        pass

