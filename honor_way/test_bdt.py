#coding=utf-8
from appium import webdriver
import time
import unittest
#测试类继承unittest.TestCase
class APPMarket(unittest.TestCase):
    def setUp(self):
        desired_caps={
            'platformName':'Android',
            'platVersion':'8.1',
            'deviceName':'8DF6R17124000857',
            'appPackage':'com.hrhb.bdt',
            'appActivity':'.activity.FlashActivity',
            'noReset':True,
            #'autoLaunch':True
        }
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(3)
        try:
            self.driver.find_element_by_id("com.hrhb.bdt:id/tv_ad_skip").click()
            self.driver.find_element_by_id("com.hrhb.bdt:id/close_update_iv").click()
            self.driver.find_element_by_id('com.hrhb.bdt:id/img_red_close').click()
        except:
            print("no ad,update or red")

    def test_product(self):
        self.driver.find_element_by_id('com.hrhb.bdt:id/product').click()
        self.driver.get_screenshot_as_file('d:\\screenshot\\t01.png')
        result=[u'【臻心医疗】',u'【臻爱医疗特需版】',u'【臻爱医疗2018】']
        e4 =self.driver.find_elements_by_xpath("//android.widget.LinearLayout\
        /android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView[@index=0]")
        for i in range(3):
            print(e4[i].text)
            self.assertIn(e4[i].text,result)
        time.sleep(2)
    #def tearDown(self):
        #self.driver.quit()

if __name__ =='__main__':
    unittest.main()








