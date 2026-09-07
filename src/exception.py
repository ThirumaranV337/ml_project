import sys##it is a built in modeule available on the python it tells the information about the error that we handling by exception
import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)

    )
    return error_message
class CustomException(Exception):##inherit the original Exception object as a parent 
    def __init__(self,error_message,error_detail:sys):
        super().__init__(self,error_message)##registring this custom exception as the original Exception and giving the input the raw error message because the third party only consider there is no error message if it empty 
        self.error_message=error_message_detail(error_message,error_detail=error_detail)#now passing to the function and getting the custom beatifull string error message 
    def __str__(self):##it is the function overriding when the user try to print the string object it display the object address but this override help to convert this object to string representation 
        return self.error_message
if __name__=="__main__":
    try:
        a=2/0
    except Exception as e:
        logging.info("Divide by zero")
        raise CustomException(e,sys)