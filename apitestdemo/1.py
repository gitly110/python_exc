# coding:utf-8
import requests

# url = "http://gg.test.hrhbbx.com/login"
# headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
#            }  # get方法其它加个ser-Agent就可以了
# s = requests.session()
# r = s.get(url, headers=headers, verify=False)
# print(s.cookies)

c = requests.cookies.RequestsCookieJar()
c.set('JSESSIONID', 'b020f498-470c-4661-a334-bddf91deb6d3')
# s.cookies.update(c)
url='http://gg.test.hrhbbx.com/index'
# print(s.cookies)
r1 = requests.get(url, cookies=c)
assert '李翠花' in r1.text, '失败'

