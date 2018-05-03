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

Created on April 4, 2018

@author: Chad Rosenquist
"""

import logging
from functools import wraps
from enum import Enum


class DisplayLogs(Enum):
    """Determines when to display logs.

    :Values:
        * NEVER: Never display the logs.  The logs will always be discarded.
        * FAILURE: Display the logs only if the test case fails.
        * ALWAYS: Always displays the logs - pass or fail.
    """
    NEVER = 1
    FAILURE = 2
    ALWAYS = 3


def capturelogs(logger=None, level=None, display_logs=DisplayLogs.FAILURE):
    """Very similar to self.assertLogs() except can be used a function decorator,
        reducing clutter in test functions.

    :param logger: Name of logger, or an actual logger.  Defaults to root logger.
    :param level: Log level as a text string.  Defaults to 'INFO'.
    :param DisplayLogs display_logs:  Determines when to display logs.
        * DisplayLogs.NEVER: Never display the logs.  The logs will always be discarded.
        * DisplayLogs.FAILURE: Display the logs only if the test case fails.
        * DisplayLogs.ALWAYS: Always displays the logs - pass or fail.

    Example::

        import logging
        from loggingtestcase import capturelogs

        @capturelogs('foo', level='INFO')
        def test_capture_logs(self, logs):
            logging.getLogger('foo').info('first message')
            logging.getLogger('foo.bar').error('second message')

            self.assertEqual(logs.output, ['INFO:foo:first message',
                                           'ERROR:foo.bar:second message'])
            self.assertEqual(logs.records[0].message, 'first message')
            self.assertEqual(logs.records[1].message, 'second message')


    Always display logs example::

        import logging
        from loggingtestcase import capturelogs, DisplayLogs

        @capturelogs('foo', level='INFO', display_logs=DisplayLogs.ALWAYS)
        def test_always_display_logs(self, logs):
            logging.getLogger('foo').info('first message')
            self.assertTrue(False)
            self.assertEqual(logs.output, ['INFO:foo:first message'])

    """
    def decorate(func):
        """Sets the logger and log level."""
        log = _set_the_logger(logger)
        log_level = _set_the_level(level)

        @wraps(func)
        def wrapper(*args, **kwargs):
            """Captures the logs."""
            assertion_error_raised = False

            # Capture the logs.
            formatter = logging.Formatter("%(levelname)s:%(name)s:%(message)s")
            handler = _CaptureLogsHandler()
            handler.setFormatter(formatter)
            old_handlers = log.handlers[:]
            old_level = log.level
            old_propagate = log.propagate
            log.handlers = [handler]
            log.setLevel(log_level)
            log.propagate = False

            try:
                # Call the function, adding the captured_logs as an argument.
                args = list(args) + [handler.captured_logs]
                return_value = func(*args, **kwargs)
                return return_value

            except Exception:
                assertion_error_raised = True
                raise

            finally:
                # Restore the logs.
                log.handlers = old_handlers
                log.level = old_level
                log.propagate = old_propagate

                # Print logs to the original handler.
                if display_logs is DisplayLogs.ALWAYS \
                        or (display_logs is DisplayLogs.FAILURE and assertion_error_raised):
                    for record in handler.captured_logs.records:
                        log.log(record.levelno, record.msg)
        return wrapper
    return decorate


def _set_the_logger(logger):
    if isinstance(logger, logging.Logger):
        return logger
    else:
        return logging.getLogger(logger)


def _set_the_level(level):
    if level:
        # noinspection PyProtectedMember
        # pylint: disable=protected-access
        return logging._nameToLevel.get(level, level)
    else:
        return logging.INFO


class _TheCapturedLogs(object):
    """Stores the captured logs."""
    def __init__(self):
        self.records = []
        self.output = []

    def __repr__(self):
        return 'records = {0} output = {1}'.format(self.records, self.output)


class _CaptureLogsHandler(logging.Handler):
    """Captures the logs and stores them so they can be inspected later."""
    def __init__(self):
        logging.Handler.__init__(self)
        self.captured_logs = _TheCapturedLogs()

    def flush(self):
        pass

    def emit(self, record):
        self.captured_logs.records.append(record)
        message = self.format(record)
        self.captured_logs.output.append(message)
