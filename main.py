from logger import Logger

if __name__ == '__main__':
    logger = Logger().setup_customer_logger()
    logger.info('This is an example of logging')