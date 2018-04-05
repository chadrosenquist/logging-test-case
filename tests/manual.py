"""
MIT License

Copyright (c) 2016 Chad Rosenquist

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

This module is for manually testing class LoggingTestCase.

Created on Dec 23, 2016

@author: Chad Rosenquist
"""
import unittest

from loggingtestcase import LoggingTestCase
from tests.simplelogging import SimpleLogging


class ManualTest(LoggingTestCase):
    """
    This class is for manually testing LoggingTestCase.
    By default, all the tests are disabled.
    Enable them, one by one.
    """
    def __init__(self, methodName='runTest', testlogger=None, testlevel=None):
        """
        To change log level, override __init__.
        TO DO: There has go to be a better way!!!!!!!!!!
        """
        # import logging; testlevel = logging.ERROR
        super().__init__(methodName, testlogger, testlevel)

    def setUp(self):
        self.simple_logging = SimpleLogging()

    def tearDown(self):
        pass

    @unittest.skip("manual test")
    def test_success(self):
        """
        No logs should be written to the console.
        The test passed, so the logs are discarded.
        """
        self.simple_logging.all()
        self.assertTrue(True)
    
    @unittest.skip("manual test")
    def test_failure(self):
        """
        This test fails.  Logs should be written to the console.
        You should see all logs but debug because debug is not
        enabled by default.
        """
        self.simple_logging.all()
        self.assertTrue(False)
    
    @unittest.skip("manual test")
    def test_error(self):
        """
        This test errors.  Logs should be written to the console.
        You should see all logs but debug because debug is not
        enabled by default.
        """
        self.simple_logging.all()
        raise Exception("test exception")
    
    @unittest.skip("manual test")
    def test_success_no_logs(self):
        """
        Tests success with no logs written out.
        
        By default, assertLogs() throws an exception if no logs are written.
        So this test case verifies that exception is correctly handled.
        """
        self.assertTrue(True)

    @unittest.skip("manual test")
    def test_failure_no_logs(self):
        """
        This test fails with no logs.
        """
        self.assertTrue(False)

    @unittest.skip("manual test")
    def test_error_no_logs(self):
        """
        This test errors with no logs.
        """
        raise Exception("test exception")
    
    @unittest.skip("manual test")
    def test_captured_logs(self):
        """
        Tests accessing the captured log files.
        """
        self.simple_logging.warning()
        self.assertEqual(self.captured_logs.output, ['WARNING:tests.simplelogging:SimpleLogging Warning'])
    
    @unittest.skip("manual test")
    def test_failure_error_and_critical(self):
        """
        This test fails.  Logs should be written to the console.
        
        Only the critical and error message should be written out.
        In __init__(), uncomment out the line:
            import logging; testlevel = logging.ERROR
        """
        self.simple_logging.all()
        self.assertTrue(False)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
