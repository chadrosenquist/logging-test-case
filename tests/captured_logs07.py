'''
Created on Dec 26, 2016

@author: Chad Rosenquist
'''
import unittest

from loggingtestcase import LoggingTestCase
from tests.simplelogging import SimpleLogging

class CapturedLogs07(LoggingTestCase):


    def setUp(self):
        self.simple_logging = SimpleLogging()
    
    def test_captured_logs(self):
        '''
        Tests accessing the captured log files.
        '''
        self.simple_logging.warning()
        self.assertEqual(self.captured_logs.output, ['WARNING:tests.simplelogging:SimpleLogging Warning'])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()