'''
Created on Dec 26, 2016

@author: Chad Rosenquist
'''
import unittest
import logging

from loggingtestcase import LoggingTestCase
from tests.simplelogging import SimpleLogging

class FailureErrAndCrit08(LoggingTestCase):
    def __init__(self, methodName='runTest', testlogger=None, testlevel=None):
        testlevel = logging.ERROR
        super().__init__(methodName, testlogger, testlevel)

    def setUp(self):
        self.simple_logging = SimpleLogging()

    def test_failure_error_and_critical(self):
        '''
        This test fails.  Logs should be written to the console.
        Only the critical and error message should be written out.
        '''
        self.simple_logging.all()
        self.assertTrue(False)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()