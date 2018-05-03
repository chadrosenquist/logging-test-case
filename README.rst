logging-test-case
=================

Production systems rely heavily upon logging. Unit tests should verify
logs are correct. ``unittest.assertLogs()`` allows developers to verify
logs are correct. Including this context manager in every test case
becomes tiresome. Also, if the test fails, the logs are not displayed.

This project provides the function decorator ``@capturelogs``.
``@capturelogs`` is similar to ``unittest.assertLogs()``, but it is a
function decorator, reducing the clutter inside the test function.

This project provides the class ``LoggingTestCase``, which inherits from
``unittest.TestCase``. For every test run, logs are automatically
captured to ``self.captured_logs``. If the test fails, the contents of
``self.captured_logs`` are written to the test output for easy
debugging.

-  Use ``@capturelogs`` if only a few tests involve log files.
-  Use ``LoggingTestCase`` if most of the tests involve logs. This
   avoids putting a function decorator for each function.

Installation
============

This package is at pypi at:

https://pypi.python.org/pypi/logging-test-case

To install using pip:

``pip install logging-test-case``

Requirements
============

-  Python 3.4 or higher.

@capturelogs
============

``capturelogs(logger=None, level=None, display_logs=DisplayLogs.FAILURE)``

* logger: Name of logger, or an actual logger. Defaults to root logger.
* level: Log level as a text string. Defaults to 'INFO'.
* display_logs: Determines when to display logs
    - DisplayLogs.NEVER: Never display the logs. The logs will always be discarded.
        + This is the current behavior of ``unittest.assertLogs()``.
    - DisplayLogs.FAILURE: Display the logs only if the test case fails. (default)
        + This can be useful for debugging test failures because the logs are still written out.
    - DisplayLogs.ALWAYS: Always displays the logs - pass or fail.
        + This can be useful when manually running the tests and the developer wants to visually inspect the logging output.

Examples are located at: ``examples/capturelogs_example.py``

unittest.assertLogs example
---------------------------

::

    class CaptureLogsExample(unittest.TestCase):
        def test_assert_logs(self):
            """Verify logs using built-in self.assertLogs()."""
            with self.assertLogs('foo', level='INFO') as logs:
                logging.getLogger('foo').info('first message')
                logging.getLogger('foo.bar').error('second message')
            self.assertEqual(logs.output, ['INFO:foo:first message',
                                           'ERROR:foo.bar:second message'])

@capturelogs example
--------------------

::

    import unittest
    import logging
    from loggingtestcase import capturelogs


    class CaptureLogsExample(unittest.TestCase):
        @capturelogs('foo', level='INFO')
        def test_capture_logs(self, logs):
            """Verify logs using @capturelogs decorator."""
            logging.getLogger('foo').info('first message')
            logging.getLogger('foo.bar').error('second message')

            self.assertEqual(logs.output, ['INFO:foo:first message',
                                           'ERROR:foo.bar:second message'])

In the above example, there is less clutter and indenting inside of the
test function. For this simple example, it doesn't matter. But if the
test involves multiple patches and ``self.assertRaises`` and many other
context managers, the function becomes crowded very quickly. The
``@capturelogs`` function decorator allows the developer to reduce the
contents and indent level inside of the function.

@capturelogs display example
----------------------------

::

    import unittest
    import logging
    from loggingtestcase import capturelogs, DisplayLogs


    class CaptureLogsExample(unittest.TestCase):
        @capturelogs('foo', level='INFO', display_logs=DisplayLogs.ALWAYS)
        def test_always_display_logs(self, logs):
            """The logs are always written to the original handler(s)."""
            logging.getLogger('foo').info('first message')
            self.assertTrue(False)
            self.assertEqual(logs.output, ['INFO:foo:first message'])

In the above example, the test fails, the logs are be displayed.

LoggingTestCase Examples
========================

Example1
--------

``examples/example1.py``

::

    import unittest
    import logging
    from loggingtestcase import LoggingTestCase


    class Example1(LoggingTestCase):

        def __init__(self, methodName='runTest', testlogger=None, testlevel=None):
            """
            To change the logger or log level, override __init__.
            By default, the root logger is used and the log level is logging.INFO.
            """
            # testlevel = logging.ERROR
            super().__init__(methodName, testlogger, testlevel)

        def setUp(self):
            self.logger = logging.getLogger(__name__)
            pass

        def test_pass(self):
            """
            Run a test that logs an info message and
            verify the info is correctly logged.

            Notice that the info message is not logged to the console.
            When all your tests pass, your console output is nice and clean.
            """
            self.logger.info("Starting request...")
            self.logger.info("Done with request.")
            self.assertEqual(self.captured_logs.output,
                             ['INFO:examples.example1:Starting request...',
                              'INFO:examples.example1:Done with request.'])

        def test_fail(self):
            """
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
            """
            self.logger.error("Failed to open file.")
            raise FileNotFoundError("Failed to open file.")

In the above example, notice how ``test_pass()`` and ``test_fail()`` do
not have any function decorators or context managers. The captured logs
are automatically available in ``self.captured_logs.output``.

Changelog
=========

release-1.3
-----------
* Support for Python 3.4, 3.5, and 3.6.
    -  Previously only Python 3.6 worked.
* Support for pytest.
    - Previously only unittest worked.  Now both unittest and pytest work.

Thanks to jayvdb on GitHub for providing both fixes!

release-1.2
-----------
Fixed the following error on Python < 3.6:

::

    /usr/local/lib/python3.5/dist-packages/loggingtestcase/capturelogs.py:31: in <module>
        from enum import Enum, auto
    E   ImportError: cannot import name 'auto'

This is because ``enum.auto()`` is new in Python 3.6.  To preserve backward compatibility,
``auto()`` is no longer used.

release-1.1.2
-------------

Added ``README.rst`` so this readme shows up on PyPI.

release-1.1
-----------

Added ``@capturelogs``.

release-1.0
-----------

Added ``LoggingTestCase``.

Tests
=====

Manual Tests
------------

``tests/manual.py``
~~~~~~~~~~~~~~~~~~~

Run this file manually. All the tests are commented out. Uncomment and
run each test one at a time. Verify the console output.

This module is not named ``manual_test.py`` because these tests are not
meant to be run automatically.

Automated Tests
---------------

To run all the tests from the command line, simply use pytest:

::

    pytest

tests/loggingtestcase\_test.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module tests class ``LoggingTestCase``. It uses
``subprocess.check_output`` to run each test case one at a time,
capturing the output. The output is examined to verify it is correct.
``loggingtestcase_test.py`` run tests in module
``simpleloggingtests.py``.

Even though automated tests are included, it is still a good idea to run
the manual tests and visually look at the output of each test case.

tests/capturelogs\_test.py
~~~~~~~~~~~~~~~~~~~~~~~~~~

This module tests ``@capturelogs``, defined in
``loggingtestcase/capturelogs.py``.
