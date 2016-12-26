'''
Created on Dec 26, 2016

@author: Chad Rosenquist
'''
import unittest

from loggingtestcase import LoggingTestCase
from tests.simplelogging import SimpleLogging

class ErrorNoLogs06(LoggingTestCase):


    def setUp(self):
        self.simple_logging = SimpleLogging()

    def test_error_no_logs(self):
        '''
        This test errors with no logs.
        '''
        raise Exception("test exception")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()