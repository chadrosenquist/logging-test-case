'''
MIT License

Copyright (c) 2016 Chad Rosenquist

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

Runs all the tests.

Created on Dec 24, 2016

@author: Chad Rosenquist
'''

import sys
import subprocess

from tests.manual import ManualTest
from pip.status_codes import SUCCESS

SUCCESS = 0
FAILURE = 1

def run_test(command):
    '''Runs a command'''
    new_command = 'python tests/' + command  # Ex: python tests/success01.py
    output = None
    try:
        output = subprocess.check_output(new_command,
                                         stderr=subprocess.STDOUT,
                                         universal_newlines=True)
    except subprocess.CalledProcessError as error:
        output = error.output
    
    return output


def success01():
    output = run_test("success01.py")
    
    if ("Ran 1 test" in output
        and "OK" in output
        and "SimpleLogging Critical" not in output
        and "SimpleLogging Error" not in output
        and "SimpleLogging Warning" not in output):
        return SUCCESS
    else:
        print("\nsuccess01 failed.  Output:\n%s\n" % output)
        return FAILURE


def failure02():
    output = run_test("failure02.py")
    
    if ("FAILED" in output
        and "CRITICAL:tests.simplelogging:SimpleLogging Critical" in output
        and "ERROR:tests.simplelogging:SimpleLogging Error" in output
        and "WARNING:tests.simplelogging:SimpleLogging Warning" in output
        and "INFO:tests.simplelogging:SimpleLogging Info" in output
        and "False is not true" in output):
        return SUCCESS
    else:
        print("\nfailure02 failed.  Output:\n%s\n" % output)
        return FAILURE


def error03():
    #output = run_test("error03.py")
    
    #print(output)  # TO DO!!!!
    pass


def main():
    '''
    Run each test case in class ManualTest.
    '''
    test_result = SUCCESS
    
    if success01() == FAILURE:
        test_result = FAILURE
    if failure02() == FAILURE:
        test_result = FAILURE
    if error03() == FAILURE:
        test_result = FAILURE
    
    return test_result

if __name__ == "__main__":
    sys.exit(main())


