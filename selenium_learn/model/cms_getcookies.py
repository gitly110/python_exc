from selenium import webdriver
from time import sleep
import json
driver = webdriver.Chrome()
driver.get('http://test.hrhbbx.com/')

print()

driver.find_element_by_name('username').send_keys('admin')
driver.find_element_by_name('password').send_keys('&XCp^Dzu2%ftOoSV')
sleep(10)
driver.find_element_by_class_name('ui-button').click()

cookie = driver.get_cookies()
print(type(cookie))

f1 = open('cookie.txt', 'w')
f1.write(json.dumps(cookie))
f1.close()


'''

[{'domain': 'test.hrhbbx.com', 'httpOnly': True, 'name': 'JSESSIONID', 'path': '/', 'secure': False, 'value': 'B10BFAA3C8259D7FB0A3359E6B09E6C9'},
 {'domain': 'test.hrhbbx.com', 'expiry': 1538015657.061925, 'httpOnly': False, 'name': 'session_user', 'path': '/', 'secure': False, 'value': '"v27vkRGypKcgcq0GBeyJvkliUP0d83gicrHam23+0yczEpmzbBuzWw=="'}]
'''