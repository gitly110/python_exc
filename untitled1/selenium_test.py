from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://www.baidu.com/")
sleep(3)
# driver.find_element_by_id('kw').send_keys('bbb')
# driver.find_element_by_id('su').click()
driver.find_element_by_xpath('//*[@id="form"]/span[1]/span').click()
sleep(8)
driver.quit()


