'''
Created on Dec 22, 2016

@author: Conan
'''
import unittest
from loggingtestcase import LoggingTestCase
from tests.simplelogging import SimpleLogging

#class LoggingTestCaseTests(LoggingTestCase):
class LoggingTestCaseTests(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testOne(self):
        test = SimpleLogging()
        test.warning()
        self.assertTrue(False)
        pass
    
    def testTwo(self):
        test = SimpleLogging()
        test.error()
        #self.assertTrue(False)
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main(buffer=True)