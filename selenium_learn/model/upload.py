from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://www.baidu.com/')
driver.find_element_by_class_name('soutu-btn').click()
driver.find_element_by_class_name('upload-pic').send_keys(r'C:\Users\ll\Desktop\timg.jpg')

cookie = driver.get_cookies()

print(cookie)


