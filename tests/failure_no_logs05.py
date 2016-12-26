'''
Created on Dec 26, 2016

@author: Chad Rosenquist
'''
import unittest

from loggingtestcase import LoggingTestCase
from tests.simplelogging import SimpleLogging

class FailureNoLogs05(LoggingTestCase):


    def setUp(self):
        self.simple_logging = SimpleLogging()

    def test_failure_no_logs(self):
        '''
        This test fails with no logs.
        '''
        self.assertTrue(False)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()