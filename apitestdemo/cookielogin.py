import requests


url = 'http://test.hrhbbx.com/login'
# get方法其它加个ser-Agent就可以了
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
           }
s = requests.session()
r = s.get(url, headers=headers, verify=False)
print(s.cookies)

c = requests.cookies.RequestsCookieJar()
c.set('session_user', '"v27vkRGypKcgcq0GBeyJvkliUP0d83gicrHam23+0yczEpmzbBuzWw=="')
s.cookies.update(c)

r1 = s.get('http://test.hrhbbx.com/admin/home')
assert '保代通CMS' in r.text, '失败'


