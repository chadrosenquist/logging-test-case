'''
Created on Dec 22, 2016

@author: Conan
'''
import unittest
from tests.loggingtestcase_tests import LoggingTestCaseTests 
from tests.simplelogging import SimpleLogging
from loggingtestcase import LoggingTestCase

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testName(self):
        simple = SimpleLogging()
        #tests = LoggingTestCaseTests()
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()