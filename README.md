# logging-test-case
Production systems rely heavily upon logging.  Unit tests should verify logs are correct.
`unittest.assertLogs()` allows developers to verify logs are correct.
Including this context manager in every test case becomes tiresome.  Also, if the test fails, the logs are not displayed.

This project provides the class `LoggingTestCase`, which inherits from `unittest.assertLogs()`.
For every test run, logs are automatically captured to `self.captured_logs`.
If the test fails, the contents of `self.captured_logs` are written to the test output for easy debugging.

# Installation
This package is at pypi at:

https://pypi.python.org/pypi/logging-test-case

To install using pip:

`pip install logging-test-case`

# Requirements
* Python 3.6 or higher.

# Examples
## Example1
`examples/example1.py`

```
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
```

# Tests
## Manual Tests
### `tests/manual.py`

Run this file manually.  All the tests are commented out.  Uncomment and run each test one at a time.  Verify the console output.

This module is not named `manual_test.py` because these tests are not meant to be run automatically.

## Automated Tests
To run all the tests from the command line, simply use pytest:
```
pytest
```
### tests/loggingtestcase_test.py

This module tests class `LoggingTestCase`.  It uses `subprocess.check_output` to run each test case one at a time, capturing the output.
The output is examined to verify it is correct.  `loggingtestcase_test.py` run tests in module `simpleloggingtests.py`.

Even though automated tests are included, it is still a good idea to run the manual tests and visually look at the output of each test case.
