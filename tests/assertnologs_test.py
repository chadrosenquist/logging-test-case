"""Tests LoggingTestCase.assertNoLogs."""
import unittest
import logging

import loggingtestcase


def divide_by(numerator, denominator):
    """Performs division and provides error logging.

    :param numerator: numerator
    :param denominator: denominator
    :returns: numerator / denominator
    :raises ZeroDivisionError: Also logs error messages.
    """
    try:
        return numerator / denominator
    except ZeroDivisionError:
        logging.getLogger().error('Divide by zero!')
        logging.getLogger().error('It is really not a good idea.')
        raise


class AssertNoLogsTestCase(loggingtestcase.LoggingTestCase):
    """Tests LoggingTestCase.assertNoLogs."""
    def test_divide_by_zero(self):
        """Test function correctly logs an error to the logger."""
        with self.assertRaises(ZeroDivisionError):
            with self.assertLogs() as assert_logs:
                divide_by(10, 0)
        self.assertEqual(assert_logs.output[0], 'ERROR:root:Divide by zero!')
        self.assertEqual(assert_logs.output[1], 'ERROR:root:It is really not a good idea.')

    def test_divide_success(self):
        """Successful division.  No errors should be logged!"""
        with self.assertNoLogs():
            divide_by(10, 2)

    def test_failed_because_errors(self):
        """Error message was logged when it shouldn't have been, so the test "fails"."""
        with self.assertRaisesRegex(AssertionError,
                                    'The follow messages were unexpectedly logged:\n'
                                    '    ERROR:root:Divide by zero!\n'
                                    '    ERROR:root:It is really not a good idea.'):
            with self.assertRaises(ZeroDivisionError):
                logging.getLogger().error(
                    'Should not be in AssertError before it was logged '
                    'with "with self.assertNoLogs()"')
                with self.assertNoLogs():
                    divide_by(10, 0)


if __name__ == '__main__':
    unittest.main()
