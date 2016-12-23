'''
Created on Dec 23, 2016

@author: Chad Rosenquist
'''
import unittest
import logging
from loggingtestcase import LoggingTestCase

class Example1(LoggingTestCase):

    def __init__(self, methodName='runTest', testlogger=None, testlevel=None):
        '''
        To change the logger or log level, override __init__.
        By default, the root logger is used and the log level is logging.INFO.
        '''
        #testlevel = logging.ERROR
        super().__init__(methodName, testlogger, testlevel)

    def setUp(self):
        self.logger = logging.getLogger(__name__)
        pass

    def test_pass(self):
        '''
        Run a test that logs an info message and
        verify the info is correctly logged.
        
        Notice that the info message is not logged to the console.
        When all your tests pass, your console output is nice and clean.
        '''
        self.logger.info("Starting request...")
        self.logger.info("Done with request.")
        self.assertEquals(self.captured_logs.output,
                          ['INFO:examples.example1:Starting request...',
                           'INFO:examples.example1:Done with request.'])
    
    def test_fail(self):
        '''
        Run a test that fails.
        
        Notice that the error message is logged to the console.
        This allows for easier debugging.
        
        Here is the output:
        ======================================================================
        ERROR: test_fail (examples.example1.Example1)
        ----------------------------------------------------------------------
        Traceback (most recent call last):
          File "D:\Git\logging-test-case\examples\example1.py", line 42, in test_fail
            raise FileNotFoundError("Failed to open file.")
        FileNotFoundError: Failed to open file.
        
        ['ERROR:examples.example1:Failed to open file.']
        ----------------------------------------------------------------------        
        '''
        self.logger.error("Failed to open file.")
        raise FileNotFoundError("Failed to open file.")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()