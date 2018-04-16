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

Tests LoggingTestCase.

Created on Dec 24, 2016

@author: Chad Rosenquist
"""

import subprocess
import unittest


def run_test(command):
    """Runs a test case and returns the output."""
    new_command = 'python -m unittest ' + command
    new_command = new_command.split()
    try:
        output = subprocess.check_output(new_command,
                                         stderr=subprocess.STDOUT,
                                         universal_newlines=True)
    except subprocess.CalledProcessError as error:
        output = error.output
    
    return output


class LoggingTestCaseTest(unittest.TestCase):

    def test_success(self):
        """
        No logs should be written to the console.
        The test passed, so the logs are discarded.
        """
        output = run_test("tests.simpleloggingtests.SimpleLoggingTests.test_success")
        self.assertIn("OK", output)
        self.assertNotIn("SimpleLogging Critical", output)
        self.assertNotIn("SimpleLogging Error", output)
        self.assertNotIn("SimpleLogging Warning", output)
    
    def test_failure(self):
        """
        This test fails.  Logs should be written to the console.
        You should see all logs but debug because debug is not
        enabled by default.
        """
        output = run_test("tests.simpleloggingtests.SimpleLoggingTests.test_failure")
        self.assertIn("FAILED", output)
        self.assertIn("CRITICAL:tests.simplelogging:SimpleLogging Critical", output)
        self.assertIn("ERROR:tests.simplelogging:SimpleLogging Error", output)
        self.assertIn("WARNING:tests.simplelogging:SimpleLogging Warning", output)
        self.assertIn("INFO:tests.simplelogging:SimpleLogging Info", output)
        self.assertIn("False is not true", output)

    def test_error(self):
        """
        This test errors.  Logs should be written to the console.
        You should see all logs but debug because debug is not
        enabled by default.
        """
        output = run_test("tests.simpleloggingtests.SimpleLoggingTests.test_error")
        self.assertIn("FAILED", output)
        self.assertIn("CRITICAL:tests.simplelogging:SimpleLogging Critical", output)
        self.assertIn("ERROR:tests.simplelogging:SimpleLogging Error", output)
        self.assertIn("WARNING:tests.simplelogging:SimpleLogging Warning", output)
        self.assertIn("INFO:tests.simplelogging:SimpleLogging Info", output)
        self.assertNotIn("DEBUG:tests.simplelogging:SimpleLogging Debug", output)
        self.assertIn("test exception", output)

    def test_success_no_logs(self):
        """
        Tests success with no logs written out.
        
        By default, assertLogs() throws an exception if no logs are written.
        So this test case verifies that exception is correctly handled.
        """
        output = run_test("tests.simpleloggingtests.SimpleLoggingTests.test_success_no_logs")
        self.assertIn("OK", output)
        self.assertNotIn("AssertionError", output)

    def test_failure_no_logs(self):
        """
        This test fails with no logs.
        """
        output = run_test("tests.simpleloggingtests.SimpleLoggingTests.test_failure_no_logs")
        self.assertIn("FAIL", output)
        self.assertIn("AssertionError", output)

    def test_error_no_logs(self):
        """
        This test errors with no logs.
        """
        output = run_test("tests.simpleloggingtests.SimpleLoggingTests.test_error_no_logs")
        self.assertIn("ERROR", output)
        self.assertIn("test exception", output)

    def test_captured_logs(self):
        """
        Tests accessing the captured log files.
        """
        output = run_test("tests.simpleloggingtests.SimpleLoggingTests.test_captured_logs")
        self.assertIn("OK", output)
        self.assertNotIn("FAILED", output)

    def test_failure_error_and_critical(self):
        """
        This test fails.  Logs should be written to the console.
        Only the critical and error message should be written out.
        """
        output = run_test("tests.simpleloggingtests.SimpleLoggingTestsErrAndCrit.test_failure_error_and_critical")
        self.assertIn("CRITICAL:tests.simplelogging:SimpleLogging Critical", output)
        self.assertIn("ERROR:tests.simplelogging:SimpleLogging Error", output)
        self.assertNotIn("WARNING:tests.simplelogging:SimpleLogging Warning", output)        


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
