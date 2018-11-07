import unittest
import HTMLTestRunner

testcase_path = ".\\testcase"
report_path = ".\\report\\"

def creat_suit():
    unit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(testcase_path, pattern="test_*.py")
