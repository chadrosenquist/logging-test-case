'''
Created on Dec 26, 2016

@author: Chad Rosenquist
'''
import unittest

from loggingtestcase import LoggingTestCase
from tests.simplelogging import SimpleLogging

class Error03(LoggingTestCase):


    def setUp(self):
        self.simple_logging = SimpleLogging()


    def test_error(self):
        '''
        This test errors.  Logs should be written to the console.
        You should see all logs but debug because debug is not
        enabled by default.
        '''
        self.simple_logging.all()
        raise Exception("test exception")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()