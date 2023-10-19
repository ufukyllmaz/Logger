import os
from pathlib import Path
import logging
from logging.handlers import TimedRotatingFileHandler

class Logger:
    def __init__(self, path=os.path.dirname(os.path.realpath('__file__'))) -> None:
       self.base_path = path
       
    def setup_customer_logger(self, project_folder = 'logs'):
        
        # create folder path and file path
        log_path = f"{self.base_path}/{project_folder}"
        file_path = os.path.join(log_path, 'project_log.log')
        
        # create folder if not exists
        Path(log_path).mkdir(parents=True, exist_ok=True)
        
        # create logger object
        logger = logging.getLogger(project_folder)
        logger.setLevel(logging.INFO)
        
        # create formatter
        formatter = logging.Formatter(fmt = "{asctime} {levelname:5} {filename}:{funcName}:{lineno} - {message}", style="{")
        
        # create rotating file handler
        rotating_file_handler = TimedRotatingFileHandler(filename=file_path, when='D', interval=30, backupCount=6)
        rotating_file_handler.setFormatter(formatter)
        
        # add rotating file handler to logger
        logger.addHandler(rotating_file_handler)
        
        return logger
    