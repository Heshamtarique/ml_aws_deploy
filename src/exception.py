# https://docs.python.org/3/library/exceptions.html

# we can write our own custom exceptions

# import sys -- https://docs.python.org/3/library/sys.html

import sys
import os
from src.logger import logging

def error_msg_details(error, error_detail:sys):
    # return type of sys 
    _,_, exc_tb = error_detail.exc_info()    # excution info -- 3 info gicve.
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))
    # above code is given in the DOC: https://docs.python.org/3/library/sys.html
    
    return error_message


class CustomException(Exception):
    
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)  # overrifing the init
        self.error_message = error_msg_details(
            error_message, error_detail=error_detail)
        
    
    def __str__(self):
        return self.error_message
        
        
        
if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        logging.info("logging---")
        raise CustomException(e, sys)
    
    
    