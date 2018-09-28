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

import loggingtestcase


class CaptureLogsExample(unittest.TestCase):
    """An example on how to capture logs."""
    @loggingtestcase.capturelogs('foo', level='INFO')
    def test_capture_logs(self, logs):
        """Verify logs using @capturelogs decorator."""
        logging.getLogger('foo').info('first message')
        logging.getLogger('foo.bar').error('second message')

        self.assertEqual(logs.output, ['INFO:foo:first message',
                                       'ERROR:foo.bar:second message'])
        self.assertEqual(logs.records[0].message, 'first message')
        self.assertEqual(logs.records[1].message, 'second message')

    def test_assert_logs(self):
        """Verify logs using built-in self.assertLogs()."""
        with self.assertLogs('foo', level='INFO') as logs:
            logging.getLogger('foo').info('first message')
            logging.getLogger('foo.bar').error('second message')
        self.assertEqual(logs.output, ['INFO:foo:first message',
                                       'ERROR:foo.bar:second message'])
        self.assertEqual(logs.records[0].message, 'first message')
        self.assertEqual(logs.records[1].message, 'second message')

    @loggingtestcase.capturelogs('foo', level='INFO',
                                 display_logs=loggingtestcase.DisplayLogs.ALWAYS)
    def test_always_display_logs(self, logs):
        """The logs are always written to the original handler(s)."""
        logging.getLogger('foo').info('first message')
        self.assertTrue(False)
        self.assertEqual(logs.output, ['INFO:foo:first message'])


if __name__ == '__main__':
    unittest.main()
