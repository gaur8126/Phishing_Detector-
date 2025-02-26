import os 
import sys 
# from src.logger.logger import logging


class PhishingException(Exception) :

    def __init__(self,error_message,error_details:sys):
        self.error_message = error_message
        self.error_details = error_details
        _,_,exc_tb = error_details.exc_info()

        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error occures in python script name [{0}] line number [{1}] error message [{2}]".format(
            self.file_name,self.lineno,str(self.error_message)
            )


if __name__ == "__main__":
    try:
        # logging.info("exception has started")
        1/0
    except Exception as e:
        print(PhishingException(e,sys))
        # logging.info("Exception raised" , PhishingException(e,sys))


    