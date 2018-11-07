#coding=utf-8
from appium import webdriver
import time
import unittest

#测试类继承自unittest.TestCase
class AppMarket(unittest.TestCase):
    def setUp(self):
        print("setUp now")
    def test1(self):
        print("test1 start")
        self.assertEqual(1,1,"test1 error")
    def test2(self):
        print("test2 start")
        self.assertEqual(1,2,"test2 error")
    def tearDown(self):
        print("tearDown")

if __name__=='__name__':
    testSuit=unittest.TestSuite()
    testLoader=unittest.defaultTestLoader
    test1=testLoader.loadTestsFromName("demo02.APPCenter.test1")
    test2=testLoader.loadTestsFromName("demo02.APPCenter.test2")
    test3 = testLoader.loadTestsFromName("demo02")
    testSuit.addTests([test1,test2,test3])
    unittest.TextTestRunner(verbosity=2).run(testSuit)

