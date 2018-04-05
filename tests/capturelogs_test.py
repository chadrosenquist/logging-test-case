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

Tests CaptureLogs.

Created on April 4, 2018

@author: Chad Rosenquist
"""

import unittest
import logging

from loggingtestcase import capturelogs


class CaptureLogsTestCase(unittest.TestCase):
    @capturelogs('foo', level='INFO')
    def test_capture_logs(self, logs):
        """Verify logs using @capturelogs decorator."""
        logging.getLogger('foo').info('first message')
        logging.getLogger('foo.bar').error('second message')

        self.assertEqual(logs.output, ['INFO:foo:first message',
                                       'ERROR:foo.bar:second message'])
        self.assertEqual(logs.records[0].message, 'first message')
        self.assertEqual(logs.records[1].message, 'second message')

    @capturelogs('foo', level='ERROR')
    def test_capture_logs_2(self, logs):
        """Verify logs using @capturelogs decorator, using a different level."""
        logging.getLogger('foo').info('first message')
        logging.getLogger('foo.bar').error('second message')

        self.assertEqual(logs.output, ['ERROR:foo.bar:second message'])

    @capturelogs('foo')
    def test_default_log_level(self, logs):
        """Verify defaults to INFO."""
        logging.getLogger('foo').info('first message')
        logging.getLogger('foo.bar').error('second message')
        logging.getLogger('foo').debug('third message')

        self.assertEqual(logs.output, ['INFO:foo:first message',
                                       'ERROR:foo.bar:second message'])

    @capturelogs(logging.getLogger('foo'), 'INFO')
    def test_logger_passed_in(self, logs):
        """Tests with a logger passed in, instead of a log name."""
        logging.getLogger('foo').info('first message')
        self.assertEqual(logs.output, ['INFO:foo:first message'])

    def test_log_level_restored(self):
        """Verifies the log level is correct restored."""
        foo_logger = logging.getLogger('foo')
        foo_logger.setLevel(logging.DEBUG)
        self._logging_test_function()
        self.assertEqual(foo_logger.level, logging.DEBUG)

    @capturelogs('foo', level='INFO')
    def _logging_test_function(self, logs):
        pass

    def test_log_level_restored_after_exception(self):
        """Verifies the log level is correct restored, even after an exception."""
        foo_logger = logging.getLogger('foo')
        foo_logger.setLevel(logging.DEBUG)
        with self.assertRaises(ValueError):
            self._logging_test_function_exception()
        self.assertEqual(foo_logger.level, logging.DEBUG)

    @capturelogs('foo', level='INFO')
    def _logging_test_function_exception(self, logs):
        raise ValueError('test')

    def test_arguments_and_return_value(self):
        """Verifies the arguments and return value are correctly preserved."""
        return_value = self._arguments_and_return('one', keyword_one='two')
        self.assertEqual(return_value, 'one | two')

    @capturelogs('foo', level='INFO')
    def _arguments_and_return(self, argument1, logs, keyword_one='hello'):
        _ = logs  # get rid of warning
        return '{0} | {1}'.format(argument1, keyword_one)

    # CHAD: Add optional parameter to fail or not fail if no logs are generated.


if __name__ == '__main__':
    unittest.main()
