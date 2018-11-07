from selenium import webdriver
from selenium.webdriver import ActionChains

from time import sleep

first_url = 'http://www.baidu.com'
second_url = 'http://tieba.baidu.com'

driver = webdriver.Edge()
driver.get(first_url)
driver.maximize_window()
sleep(2)

driver.get(second_url)
sleep(2)

# driver.back()
# sleep(2)

# driver.forward()
#
# for i in range(3):
#     driver.refresh()
#     print('这是第 %d 刷新' % (i+1))
# sleep(3)

driver.find_element_by_id('wd1').clear()
driver.find_element_by_id('wd1').send_keys('hello')
driver.find_element_by_id('wd1').submit()
sleep(3)

size = driver.find_element_by_id('wd1').size
print(size)
text = driver.find_element_by_id('footer').text
print(text)
sleep(3)

above = driver.find_element_by_css_selector('.u_member_wrap')
ActionChains(driver).move_to_element(above).perform()
sleep(3)
text1 = driver.find_element_by_xpath('//*[@id="com_userbar"]/ul/li[7]/div[2]/div/div[1]/ul/li[3]').text
print(text1)

driver.quit()

