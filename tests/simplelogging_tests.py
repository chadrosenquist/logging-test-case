'''
Created on Dec 21, 2016

@author: Chad Rosenquist
'''
import unittest
import logging
import sys
from .simplelogging import SimpleLogging
from loggingunittest.unittesthandler import UnitTestHandler

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        #ok = 'yo'
        #print("TEARDOWN: %s" % ok)
        pass

    def run(self, result=None):
        '''
        Extremely tightly coupled with how unittest.TestCase and unittest.TestResult are implemented!!!
        If these classes change, this class could break!
        '''
        
        if result is None:
            super(Test, self).run(result)
        else:
            before_failures = len(result.failures)
            before_errors = len(result.errors)
            
            # Run the test case.
            with self.assertLogs(logger=None, level=None) as capture_logs:
                super(Test, self).run(result)
            
            after_failures = len(result.failures)
            after_errors = len(result.errors)           
        
            if after_failures > before_failures:
                #print("CHAD: failure", file=sys.stderr)   # TO DO: Need to be able to write to TestResult's buffer if result.buffer is True.
                #test, failure_string = result.failures[-1]
                #print("CHAD: failure_string = %s" % failure_string)
                #print("CHAD: failure_string = %s" % result.failures[-1][1])
                #sys.stderr.flush()
                #result.failures.append(("yo test", "CHAD: failure append"))
                #result.failures[-1] = (result.failures[-1][0], result.failures[-1][1] + "\nCHAD: failure")
                result.failures[-1] = (result.failures[-1][0], result.failures[-1][1] + "\n" + str(capture_logs.output))
                
            elif after_errors > before_errors:
                #print("CHAD: error", file=sys.stderr)
                #sys.stderr.flush()
                #result.errors.append(('yo test', "CHAD: errors append"))
                #result.errors[-1] = (result.errors[-1][0], result.errors[-1][1] + "\nCHAD: error")
                result.errors[-1] = (result.errors[-1][0], result.errors[-1][1] + "\n" + str(capture_logs.output))
                
                
        #print("CHAD: failures = %s errors = %s" % (len(result.failures), len(result.errors)))

    def testOne(self):
        #handler = UnitTestHandler()
        
        #logging.basicConfig(level=logging.INFO)
        
        test = SimpleLogging()
        #logger = test.logger
        #logger.addHandler(handler)
        
        test.error()
        test.warning()
        test.info()
        test.debug()
        
        #logger.removeHandler(handler)
        
        #print("CHAD:\n%s" % str(handler))
        
        '''
        TO DO:
        1. Option to block console output.
        2. assert regex functions.
        
        https://docs.python.org/3.4/library/unittest.html#unittest.TestCase.assertLogs
        assertLogs(logger=None, level=None)
        '''
        #self.assertTrue(False)
        #raise Exception("test exception")
        
        #logger = test.logger
        #for handler in logger.hasHandlers():
        #    print(handler)
    
    def XtestError(self):
        raise Exception("test exception")
        pass
    
    def XtestFailure(self):
        self.assertTrue(False)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()