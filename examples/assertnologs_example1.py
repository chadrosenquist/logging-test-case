"""
MIT License

Copyright (c) 2018 Chad Rosenquist

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

Created on Nov 22, 2018

@author: Chad Rosenquist
"""
import unittest
import logging

import loggingtestcase


class AssertNoLogsExample(loggingtestcase.LoggingTestCase):
    """Example on how to use LoggingTestCase and no logging."""

    def __init__(self, methodName='runTest', testlogger=None, testlevel=None):
        """
        To change the logger or log level, override __init__.
        By default, the root logger is used and the log level is logging.INFO.
        """
        # testlevel = logging.ERROR
        super().__init__(methodName, testlogger, testlevel)

    def setUp(self):
        self.logger = logging.getLogger(__name__)

    def test_assert_no_logs_fail(self):
        """The test fails because logs are emitted.

        Here is the output:
        E               AssertionError: The follow messages were unexpectedly logged:
        E                   ERROR:examples.assertnologs_example1:first message
        E                   ERROR:examples.assertnologs_example1:second message

        """
        with self.assertNoLogs():
            self.logger.error('first message')
            self.logger.error('second message')

    def test_assert_no_logs_pass(self):
        """The test passes because no logs are emitted inside the context manager."""
        self.logger.error('first message')
        with self.assertNoLogs():
            pass
        self.logger.error('second message')


if __name__ == "__main__":
    unittest.main()
