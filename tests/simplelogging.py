"""
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

Created on Dec 21, 2016

@author: Chad Rosenquist
"""

import logging


class SimpleLogging(object):
    """
    Simple object used to test LoggingTestCase.
    """
    CRITICAL_MESSAGE = 'SimpleLogging Critical'
    ERROR_MESSAGE = 'SimpleLogging Error'
    WARNING_MESSAGE = 'SimpleLogging Warning'
    INFO_MESSAGE = 'SimpleLogging Info'
    DEBUG_MESSAGE = 'SimpleLogging Debug'

    def __init__(self):
        """
        Constructor
        """
        self.__logger = logging.getLogger(__name__)

    @property
    def logger(self):
        return self.__logger
    
    def critical(self):
        self.logger.critical(self.CRITICAL_MESSAGE)
    
    def error(self):
        self.logger.error(self.ERROR_MESSAGE)
    
    def warning(self):
        self.logger.warning(self.WARNING_MESSAGE)
    
    def info(self):
        self.logger.info(self.INFO_MESSAGE)
    
    def debug(self):
        self.logger.debug(self.DEBUG_MESSAGE)

    def all(self):
        self.critical()
        self.error()
        self.warning()
        self.info()
        self.debug()
