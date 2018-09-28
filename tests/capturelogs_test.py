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
from io import StringIO

import loggingtestcase


class CaptureLogsTestCase(unittest.TestCase):
    """Tests for capturing log files."""
    @loggingtestcase.capturelogs('foo', level='INFO')
    def test_capture_logs(self, logs):
        """Verify logs using @capturelogs decorator."""
        logging.getLogger('foo').info('first message')
        logging.getLogger('foo.bar').error('second message')
        self.assertEqual(logs.output, ['INFO:foo:first message',
                                       'ERROR:foo.bar:second message'])
        self.assertEqual(logs.records[0].message, 'first message')
        self.assertEqual(logs.records[1].message, 'second message')

    @loggingtestcase.capturelogs('foo', level='ERROR')
    def test_capture_logs_2(self, logs):
        """Verify logs using @capturelogs decorator, using a different level."""
        logging.getLogger('foo').info('first message')
        logging.getLogger('foo.bar').error('second message')

        self.assertEqual(logs.output, ['ERROR:foo.bar:second message'])

    @loggingtestcase.capturelogs('foo')
    def test_default_log_level(self, logs):
        """Verify defaults to INFO."""
        logging.getLogger('foo').info('first message')
        logging.getLogger('foo.bar').error('second message')
        logging.getLogger('foo').debug('third message')

        self.assertEqual(logs.output, ['INFO:foo:first message',
                                       'ERROR:foo.bar:second message'])

    @loggingtestcase.capturelogs(logging.getLogger('foo'), 'INFO')
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

    @loggingtestcase.capturelogs('foo', level='INFO')
    def _logging_test_function(self, logs):
        pass

    def test_log_level_restored_after_exception(self):
        """Verifies the log level is correct restored, even after an exception."""
        foo_logger = logging.getLogger('foo')
        foo_logger.setLevel(logging.DEBUG)
        with self.assertRaises(ValueError):
            self._logging_test_function_exception()
        self.assertEqual(foo_logger.level, logging.DEBUG)

    @loggingtestcase.capturelogs('foo', level='INFO')
    def _logging_test_function_exception(self, logs):
        raise ValueError('test')

    def test_arguments_and_return_value(self):
        """Verifies the arguments and return value are correctly preserved."""
        return_value = self._arguments_and_return('one', keyword_one='two')
        self.assertEqual(return_value, 'one | two')

    # noinspection PyUnusedLocal
    @loggingtestcase.capturelogs('foo', level='INFO')
    def _arguments_and_return(self, argument1, logs, keyword_one='hello'):
        return '{0} | {1}'.format(argument1, keyword_one)


class DisplayLogsTestCase(unittest.TestCase):
    """Tests for displaying the logs.

    The code is actually very simple, but there is a lot of test code
    so place this into another class.
    """
    @classmethod
    def _set_stream_handler(cls):
        foo_logger = logging.getLogger('foo')
        stream = StringIO()
        stream_handler = logging.StreamHandler(stream)
        stream_formatter = logging.Formatter("%(levelname)s:%(name)s:%(message)s")
        stream_handler.setFormatter(stream_formatter)
        foo_logger.addHandler(stream_handler)

        return stream

    def test_display_logs_if_failure(self):
        """If the test fails, the logs are displayed."""
        stream = self._set_stream_handler()

        # Run a test that writes to the logs and fails.
        with self.assertRaises(AssertionError):
            self._failed_test()

        # Verify the logs are captured.
        self.assertMultiLineEqual(stream.getvalue(),
                                  'INFO:foo:Failed to open file!'
                                  '\nDEBUG:foo:Check file permissions.\n')

    # noinspection PyUnusedLocal
    @loggingtestcase.capturelogs('foo', level='DEBUG')
    def _failed_test(self, logs):
        logging.getLogger('foo').info('Failed to open file!')
        logging.getLogger('foo').debug('Check file permissions.')
        self.assertTrue(False)

    def test_discard_logs_if_failure(self):
        """If the test fails, the logs are discarded."""
        stream = self._set_stream_handler()

        # Run a test that writes to the logs and fails.
        with self.assertRaises(AssertionError):
            self._failed_test_discard()

        # Verify the logs are not captured.
        self.assertEqual(stream.getvalue(), '')

    # noinspection PyUnusedLocal
    @loggingtestcase.capturelogs('foo', level='DEBUG',
                                 display_logs=loggingtestcase.DisplayLogs.NEVER)
    def _failed_test_discard(self, logs):
        logging.getLogger('foo').info('Failed to open file!')
        logging.getLogger('foo').debug('Check file permissions.')
        self.assertTrue(False)

    def test_discard_logs_if_success(self):
        """If the test passes, the logs are discarded."""
        stream = self._set_stream_handler()

        # Run a test that writes to the logs and fails.
        self._success_test_discard()

        # Verify the logs are not captured.
        self.assertEqual(stream.getvalue(), '')

    # noinspection PyUnusedLocal
    @loggingtestcase.capturelogs('foo', level='DEBUG')
    def _success_test_discard(self, logs):
        logging.getLogger('foo').info('Failed to open file!')
        logging.getLogger('foo').debug('Check file permissions.')

    def test_display_logs_if_success(self):
        """If the test passes, the logs are displayed."""
        stream = self._set_stream_handler()

        # Run a test that writes to the logs and fails.
        self._success_test_display()

        # Verify the logs are not captured.
        self.assertEqual(stream.getvalue(),
                         'INFO:foo:Failed to open file!\nDEBUG:foo:Check file permissions.\n')

    # noinspection PyUnusedLocal
    @loggingtestcase.capturelogs('foo', level='DEBUG',
                                 display_logs=loggingtestcase.DisplayLogs.ALWAYS)
    def _success_test_display(self, logs):
        logging.getLogger('foo').info('Failed to open file!')
        logging.getLogger('foo').debug('Check file permissions.')


if __name__ == '__main__':
    unittest.main()
