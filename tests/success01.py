'''
Created on Dec 26, 2016

@author: Chad Rosenquist
'''
import unittest

from loggingtestcase import LoggingTestCase
from tests.simplelogging import SimpleLogging

class Success01(LoggingTestCase):


    def setUp(self):
        self.simple_logging = SimpleLogging()
    
    def test_success(self):
        '''
        No logs should be written to the console.
        The test passed, so the logs are discarded.
        '''
        self.simple_logging.all()
        self.assertTrue(True)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()