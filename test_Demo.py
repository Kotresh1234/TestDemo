
import time
from unittest.suite import TestSuite
import unittest
import HtmlTestRunner

class TestCase(unittest.TestCase):

 def setUp(self):
     unittest.TestCase.setUp(self)

 def tearDown(self):
     unittest.TestCase.tearDown(self)

 def test_Demo_Windows(self):
     # value = input("Please Enter The Value :\n ")
     # print(f'Your Entered Value {value}')
     a=1
     b=2
     c=a+b
     print(f'Your Entered Value {c}')
     assert c==3
     True
     print("Assertion Pass")
     
     
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/Learning/AutomationQA'))