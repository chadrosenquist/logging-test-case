'''
Created on Dec 22, 2016

@author: Chad Rosenquist
'''
import unittest


'''
TO DO

Properties:
    testlogger - Set the logger.  The default is the root logger.
    testlevel - Set the log level.  logging.CRITICAL, logging.ERROR, ...
            The default is logging.INFO.
    
    Note: testlogger and testlevel are not named logger and level to ensure
          the names do not conflict with any super class variables.
'''
class LoggingTestCase(unittest.TestCase):
    
    def __init__(self, methodName='runTest', testlogger=None, testlevel=None):
        super().__init__(methodName)
        self.testlogger = testlogger
        self.testlevel = testlevel

    def run(self, result=None):
        '''
        Runs the test case, capturing logs.  If the test fails or errors, the logs are displayed.
        '''        
        # Extremely tightly coupled with how unittest.TestCase and unittest.TestResult are implemented!!!
        # If these classes change, this class could break!
        
        if result is None:
            super(LoggingTestCase, self).run(result)
        else:
            before_failures = len(result.failures)
            before_errors = len(result.errors)
            
            # Run the test case, capturing logs.
            with self.assertLogs(logger=self.testlogger, level=self.testlevel) as capture_logs:
                super(LoggingTestCase, self).run(result)
            
            after_failures = len(result.failures)
            after_errors = len(result.errors)           
        
            # If the number of failures or errors increased, add the logs to the output
            # for that test case.
            if after_failures > before_failures:
                result.failures[-1] = (result.failures[-1][0], result.failures[-1][1] + "\n" + self._capture_logs_to_string(capture_logs))
                
            elif after_errors > before_errors:
                result.errors[-1] = (result.errors[-1][0], result.errors[-1][1] + "\n" + self._capture_logs_to_string(capture_logs))
    
    
    def _capture_logs_to_string(self, capture_logs):
        return str(capture_logs.output)
