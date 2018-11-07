#coding=utf-8
from appium import webdriver
import time
#import unittest
#测试类继承unittest.TestCase

#class APPMarket(unittest.TestCase):
    #def setUp(self):
desired_caps={
    'platformName':'Android',
    'platVersion':'6.0',
    'deviceName':'8DF6R17124000857',
    'appPackage':'com.huawei.appmarket',
    'appActivity':'.MainActivity',
    'noReset':True,
    'autoLaunch':True
}
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(3)
print('111')