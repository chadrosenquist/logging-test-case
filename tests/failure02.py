'''
Created on Dec 26, 2016

@author: Chad Rosenquist
'''
import unittest

from loggingtestcase import LoggingTestCase
from tests.simplelogging import SimpleLogging

class Failure02(LoggingTestCase):


    def setUp(self):
        self.simple_logging = SimpleLogging()


    def test_failure(self):
        '''
        This test fails.  Logs should be written to the console.
        You should see all logs but debug because debug is not
        enabled by default.
        '''
        self.simple_logging.all()
        self.assertTrue(False)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()