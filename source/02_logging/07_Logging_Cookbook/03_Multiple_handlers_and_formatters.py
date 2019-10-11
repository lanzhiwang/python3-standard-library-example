import logging

logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# add the handlers to logger
logger.addHandler(ch)
logger.addHandler(fh)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')

"""
[root@huzhi-code 07_Logging_Cookbook]# python3 03_Multiple_handlers_and_formatters.py
2019-10-10 10:42:23,303 - simple_example - ERROR - error message
2019-10-10 10:42:23,303 - simple_example - CRITICAL - critical message
[root@huzhi-code 07_Logging_Cookbook]# 
[root@huzhi-code 07_Logging_Cookbook]# cat spam.log
2019-10-10 10:42:23,302 - simple_example - DEBUG - debug message
2019-10-10 10:42:23,302 - simple_example - INFO - info message
2019-10-10 10:42:23,303 - simple_example - WARNING - warn message
2019-10-10 10:42:23,303 - simple_example - ERROR - error message
2019-10-10 10:42:23,303 - simple_example - CRITICAL - critical message
[root@huzhi-code 07_Logging_Cookbook]#
"""