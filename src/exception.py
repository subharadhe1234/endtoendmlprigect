import sys
import logging
'''The sys library in Python is a built-in module that provides information about the current Python 
interpreter and allows you to manipulate different parts of the Python runtime environment.'''
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    '''exc_tb hold whitch file error occer or witch line error occer '''
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occerar in a file [{0}] the line no [{1}] the error is [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message



class CastomException(Exception):
    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail)
    def __str__(self):
        return self.error_message
    
if __name__=="__main__":

    try:
        a=1/0 
    except Exception as e:
        logging.info("radhe radhe")
        raise CastomException(e,sys)