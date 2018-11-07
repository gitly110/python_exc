import requests
import pytest

url='http://bdt.hrhbbx.com'
#url='http://api.test.hrhbbx.com'
def get_vercode(mobile, type):
    code_url=url + '/msconsumer/api/v1/sms/getVercode'
    body={'mobile':mobile,
          'type':type}
    res=requests.post(code_url,json=body)
    print(res.text)
'''* 注册--"type":"1"
* 忘记密码--"type":"2"
* 设置交易密码--"type":"3"
* 修改登录密码--"type":"4"
* 验证原手机号--"type":"5"
* 验证新手机号--"type":"6"
* 绑卡手机号验证--"type":"7"
* 修改交易密码4.1--"type":"8"
* 登录验证码4.3.2--"type":"9"
'''
get_vercode(13400000001,1)
def sms_login(mobile,vercode):
    sms_url=url +'/msconsumer/api/agent/login/smsLogin'
    body={'mobile':mobile,
          'type':type}
    res=requests.post(code_url,json=body)
    print(res.text)