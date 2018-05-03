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

Created on Dec 22, 2016

@author: Chad Rosenquist
"""

import unittest


class LoggingTestCase(unittest.TestCase):
    """This class captures the logfile output.

    If the test passes, the output is thrown away.
    If the test fails, the output is displayed.

    Attributes:
        captured_logs - The captured logs files generated by the assertLogs() context manager.
        testlogger    - Set the logger.  The default is the root logger.
        testlevel     - Set the log level.  logging.CRITICAL, logging.ERROR, ...
                        The default is logging.INFO.

    Note: testlogger and testlevel are not named logger and level to ensure
          the names do not conflict with any super class variables.

    Example:
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

            ERROR:examples.example1:Failed to open file.
            ----------------------------------------------------------------------
            '''
            self.logger.error("Failed to open file.")
            raise FileNotFoundError("Failed to open file.")
    """

    def __init__(self, methodName='runTest', testlogger=None, testlevel=None):
        """Constructor

        Args:
            methodName: Name of the method
            testlogger: test logger.  Set to override the default.
            testlevel: The log level.  Set to override the default of Debug.

        Returns:
            LoggingTestCase object
        """
        super().__init__(methodName)
        self.testlogger = testlogger
        self.testlevel = testlevel
        self.captured_logs = None

    def run(self, result=None):
        """Runs the test case, capturing logs.

        If the test fails or errors, the logs are displayed.

        Args:
            result: Location to store the result.  If None, have the super class run the test case.
        """
        # Extremely tightly coupled with how unittest.TestCase and unittest.TestResult
        # are implemented!!!  If these classes change, this class could break!
        if result is None:
            super(LoggingTestCase, self).run(result)
        else:
            before_failures = len(result.failures)
            before_errors = len(result.errors)

            # Run the test case, capturing logs.
            # assertLogs throws an AssertionError if no logging is written.  Because there could be
            # test cases that do not log anything, this code captures that exception and ignores it.
            try:
                with self.assertLogs(logger=self.testlogger,
                                     level=self.testlevel) as self.captured_logs:
                    super(LoggingTestCase, self).run(result)
            except AssertionError as assertion_error:
                if not self.captured_logs.records and "no logs of level" in str(assertion_error):
                    pass
                else:
                    raise

            after_failures = len(result.failures)
            after_errors = len(result.errors)

            # If the number of failures or errors increased, add the logs to the output
            # for that test case.
            if self.captured_logs.records:
                if after_failures > before_failures:
                    result.failures[-1] = (result.failures[-1][0], result.failures[-1][1] + "\n"
                                           + self._capture_logs_to_string(self.captured_logs))

                elif after_errors > before_errors:
                    result.errors[-1] = (result.errors[-1][0], result.errors[-1][1] + "\n"
                                         + self._capture_logs_to_string(self.captured_logs))

    @staticmethod
    def _capture_logs_to_string(capture_logs):
        return "\n".join(capture_logs.output)
