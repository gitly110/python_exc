# coding:utf-8

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "8DF6R17124000857"
caps["app"] = "C:\\Users\\ll\\Desktop\\bdt_V4.3.1_beta5.apk"
caps["noReset"] = False
caps["autoLaunch"] = False
caps["automationName"] = "Uiautomator2"
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

time.sleep(5)
driver.launch_app()
time.sleep(3)
driver.swipe(1000, 1500, 500, 1700, 300)
time.sleep(1)
driver.swipe(1000, 1500, 500, 1700, 300)
time.sleep(1)
el0 = driver.find_element_by_id("com.hrhb.bdt:id/tiyan_btn")
el0.click()
time.sleep(3)


def always_allow(driver, number=5):
    for i in range(number):
        loc = ("xpath", "//*[@text='始终允许']")
        try:
            e = WebDriverWait(driver, 1, 0.5).until(EC.presence_of_element_located(loc))
            e.click()
        except:
            pass
#------------toast-------------------
def is_toast_exist(driver,text,timeout=30,poll_frequency=0.5):
    '''is toast exist, return True or False
    :Agrs:
     - driver - 传driver
     - text   - 页面上看到的文本内容
     - timeout - 最大超时时间，默认30s
     - poll_frequency  - 间隔查询时间，默认0.5s查询一次
    :Usage:
     is_toast_exist(driver, "看到的内容")
    '''
    try:
        toast_loc = ("xpath", ".//*[contains(@text,'%s')]"%text)
        WebDriverWait(driver, timeout, poll_frequency).until(EC.presence_of_element_located(toast_loc))
        return True
    except:
        return False


if __name__ == "__main__":
    # 调用始终允许函数
    always_allow(driver)

time.sleep(3)
el0 = driver.find_element_by_id("com.hrhb.bdt:id/close_update_iv")
el0.click()
el1=driver.find_element_by_id('com.hrhb.bdt:id/img_red_close')
el1.click()
el2 = driver.find_element_by_id("com.hrhb.bdt:id/btn_mine")
el2.click()
el3 = driver.find_element_by_id("com.hrhb.bdt:id/v_user")
el3.click()
el4 = driver.find_element_by_id("com.hrhb.bdt:id/registe_tv")
el4.click()
el5 = driver.find_element_by_id("com.hrhb.bdt:id/edit_input_phone")
mobile=str(random.randint(13000000002,19999999999))
print("mobile:",mobile)
el5.send_keys(mobile)
el6 = driver.find_element_by_id("com.hrhb.bdt:id/tv_get_code")
el6.click()
el7 = driver.find_element_by_id("com.hrhb.bdt:id/edit_mms_code")
el7.send_keys("123456")
el8 = driver.find_element_by_id("com.hrhb.bdt:id/edit_input_pass_word")
el8.send_keys("qwe123")
el9 = driver.find_element_by_id("com.hrhb.bdt:id/btn_register")
el9.click()

