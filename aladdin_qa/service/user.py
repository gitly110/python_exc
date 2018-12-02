# -*- coding:utf-8 -*-
# author: songyangyang
# time: 2018/10/14
import random
import requests
from faker import Faker

from common.get_regist_code import get_regist_code
from common.update_gzq_regist import update_regist

basic_form_data = {
    "appVersion": "1.3.60",
    "buildVersion": "1.3.60",
    "platform": "anroid",
    "channelId": "yingyongbao"

}


def user_regist(phone, user_image, user_name=None):
    """
    在测试环境注册铛铛用户
    :param phone: 
    :return: true or false
    """
    fker = Faker(locale='zh_CN')
    identify_url = "http://dev.im-dangdang.com/user/v1/regist/identify"
    identify_form_data = {
        "checkPhone": "1",
        "phone": phone
    }
    identify_form_data.update(basic_form_data)
    resp_code = requests.post(identify_url, data=identify_form_data).json()["status"]
    if resp_code == "10102":
        raise RecursionError("用户已经注册")
    elif resp_code == "1":
        sex = random.choice([1, 2])
        if sex == 1:
            name = fker.name_male()
        else:
            name = fker.name_female()
        val_code = get_regist_code(phone)
        regist_url = "https://dev.im-dangdang.com/user/v1.1/regist"
        regist_data = {
            "nickName": user_name if user_name else name,
            "sex": sex,
            "cityId": 268,
            "userName": user_name if user_name else name,
            "provinceId": 30,
            "password": "123456",
            "userImage": '{{"width": "200", "picture": "{}", "height": "200"}}'.format(user_image),
            "phone": phone,
            "identifyCode": val_code
        }
        regist_data.update(basic_form_data)
        resp = requests.post(regist_url, data=regist_data, verify=False).json()
        return resp

def gzq_regist(email, password=12345678):
    gzq_regist_url = "http://devgzq.im-dangdang.com/cp/regist/base"
    gzq_regist_data = {
        "email": email,
        "password": password
    }
    requests.post(gzq_regist_url, data=gzq_regist_data)
    update_regist(email)

if __name__ == "__main__":
    from common.get_user_profile import get_user_id_by_phone
    from tools.image_handler import get_random_image_url_from_oss
    for p in range(13660000023, 13660000051):
        user_regist(p, get_random_image_url_from_oss("明星头像"))

    # print(user_regist(13660000000, get_random_image_url_from_oss("篮球明星")))
