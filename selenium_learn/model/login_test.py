from time import sleep
from model.cms_cookie_login import CookieLogin

# 登录
cl = CookieLogin()
cl.cookie_login()
sleep(5)
#cl.quite()
#
