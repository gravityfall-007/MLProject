import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler and set the logging level
log_file = 'logs/errors.log'
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.ERROR)

# create a formatter for the log messages
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# add the file handler to the logger
logger.addHandler(file_handler)

class CustomException(Exception):
    def __init__(self, error_message, error_details=None):
        self.error_message = error_message_details(error_message, error_details=error_details)
        logger.error(self.error_message)

def error_message_details(error_message, error_details=None):
    filename = sys.argv[0]
    line_number = sys.exc_info()[-1].tb_lineno
    return "Error occurred in Python script name [{0}] line number [{1}] with error message [{2}]".format(filename, line_number, error_message)

if __name__ == "__main__":
    try:
        a = 1 / 1
    except Exception as e:
        raise CustomException(str(e), sys.exc_info()) from e
