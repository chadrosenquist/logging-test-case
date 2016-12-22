'''
Created on Dec 21, 2016

@author: Chad Rosenquist

http://bugs.python.org/file4410/logging.py
'''

from logging import Handler

class UnitTestHandlerRecord(object):
    '''
    Holds one logging record.
    '''
    def __init__(self, message, levelno, levelname):
        self.message = message
        self.levelno = levelno
        self.levelname = levelname
    
    def __str__(self):
        return '{0} {1} {2}'.format(self.levelname, self.levelno, self.message, self.levelno)


class UnitTestHandler(Handler):
    '''
    TO DO: Describe what this class does and how to use it.
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super().__init__()
        self.__messages = []
    
    def flush(self):
        '''
        Flush
        '''
        pass
    
    def emit(self, record):
        '''
        Adds the record to the list of messages.
        
        If a formatter is specified, it is used to format the record.
        If exception information is present, it is formatted using
        traceback.print_exception and appended to the stream.
        '''
        print("CHAD: record = %s" % str(record))
        try:
            message = self.format(record)
            self.messages.append(UnitTestHandlerRecord(message, record.levelno, record.levelname))
            self.flush()
        except:
            self.handleError()
    
    def __str__(self):
        '''
        Returns the contents as a string.
        
        Example:
        ERROR 40 SimpleLogging Error
        WARNING 30 SimpleLogging Warning
        INFO 20 SimpleLogging Info
        '''
        string = ''
        for message in self.messages:
            string = string + str(message) + "\n"
        return string
    
    @property
    def messages(self):
        return self.__messages

    