'''
Created on Dec 21, 2016

@author: Chad Rosenquist
'''

import logging

class SimpleLogging(object):
    '''
    classdocs
    '''
    CRITICAL_MESSAGE = 'SimpleLogging Critical'
    ERROR_MESSAGE = 'SimpleLogging Error'
    WARNING_MESSAGE = 'SimpleLogging Warning'
    INFO_MESSAGE = 'SimpleLogging Info'
    DEBUG_MESSAGE = 'SimpleLogging Debug'
    

    def __init__(self):
        '''
        Constructor
        '''
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
