from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://www.baidu.com/')

set_link = driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(set_link).perform()

driver.find_element_by_link_text('搜索设置').click()

e = driver.find_element_by_link_text(u'保存设置')
sleep(2)
e.click()
sleep(2)
message = driver.switch_to.alert.text
print(message)
driver.switch_to.alert.accept()
sleep(10)
driver.quit()


