'''
Created on Dec 26, 2016

@author: Chad Rosenquist
'''
import unittest

from loggingtestcase import LoggingTestCase
from tests.simplelogging import SimpleLogging

class SuccessNoLogs04(LoggingTestCase):


    def setUp(self):
        self.simple_logging = SimpleLogging()

    def test_success_no_logs(self):
        '''
        Tests success with no logs written out.
        
        By default, assertLogs() throws an exception if no logs are written.
        So this test case verifies that exception is correctly handled.
        '''
        self.assertTrue(True)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()