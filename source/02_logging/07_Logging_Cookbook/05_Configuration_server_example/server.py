import logging
import logging.config
import time
import os
from logging_tree import printout

# read initial config file
logging.config.fileConfig('logging.conf')

# create and start listener on port 9999
t = logging.config.listen(9999)
t.start()

logger = logging.getLogger('simpleExample')

print()

printout()

print()

try:
    # loop through logging calls to see the difference
    # new configurations make, until Ctrl+C is pressed
    while True:
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warn message')
        logger.error('error message')
        logger.critical('critical message')
        time.sleep(20)
except KeyboardInterrupt:
    # cleanup
    logging.config.stopListening()
    t.join()

"""
$ python server.py

<--""
   Level DEBUG
   Handler Stream <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>
     Level DEBUG
     Formatter fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s' datefmt=''
   |
   o   "simpleExample"
       Level DEBUG
       Propagate OFF
       Handler Stream <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>
         Level DEBUG
         Formatter fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s' datefmt=''

2023-12-08 08:33:07,870 - simpleExample - DEBUG - debug message
2023-12-08 08:33:07,871 - simpleExample - INFO - info message
2023-12-08 08:33:07,871 - simpleExample - WARNING - warn message
2023-12-08 08:33:07,871 - simpleExample - ERROR - error message
2023-12-08 08:33:07,871 - simpleExample - CRITICAL - critical message
2023-12-08 08:33:27,895 - simpleExample - DEBUG - debug message
2023-12-08 08:33:27,896 - simpleExample - INFO - info message
2023-12-08 08:33:27,896 - simpleExample - WARNING - warn message
2023-12-08 08:33:27,896 - simpleExample - ERROR - error message
2023-12-08 08:33:27,896 - simpleExample - CRITICAL - critical message
2023-12-08 08:33:47,897 - simpleExample - DEBUG - debug message
2023-12-08 08:33:47,898 - simpleExample - INFO - info message
2023-12-08 08:33:47,898 - simpleExample - WARNING - warn message
2023-12-08 08:33:47,898 - simpleExample - ERROR - error message
2023-12-08 08:33:47,898 - simpleExample - CRITICAL - critical message
2023-12-08 08:34:07,877 - simpleExample - DEBUG - debug message
2023-12-08 08:34:07,877 - simpleExample - INFO - info message
2023-12-08 08:34:07,877 - simpleExample - WARNING - warn message
2023-12-08 08:34:07,877 - simpleExample - ERROR - error message
2023-12-08 08:34:07,877 - simpleExample - CRITICAL - critical message
2023-12-08 08:34:27,897 - simpleExample - DEBUG - debug message
2023-12-08 08:34:27,898 - simpleExample - INFO - info message
2023-12-08 08:34:27,898 - simpleExample - WARNING - warn message
2023-12-08 08:34:27,898 - simpleExample - ERROR - error message
2023-12-08 08:34:27,898 - simpleExample - CRITICAL - critical message
2023-12-08 08:34:47,898 - simpleExample - DEBUG - debug message
2023-12-08 08:34:47,898 - simpleExample - INFO - info message
2023-12-08 08:34:47,898 - simpleExample - WARNING - warn message
2023-12-08 08:34:47,898 - simpleExample - ERROR - error message
2023-12-08 08:34:47,898 - simpleExample - CRITICAL - critical message
2023-12-08 08:35:07,899 - simpleExample - DEBUG - debug message
2023-12-08 08:35:07,899 - simpleExample - INFO - info message
2023-12-08 08:35:07,900 - simpleExample - WARNING - warn message
2023-12-08 08:35:07,900 - simpleExample - ERROR - error message
2023-12-08 08:35:07,900 - simpleExample - CRITICAL - critical message
2023-12-08 08:35:27,921 - simpleExample - DEBUG - debug message
2023-12-08 08:35:27,921 - simpleExample - INFO - info message
2023-12-08 08:35:27,921 - simpleExample - WARNING - warn message
2023-12-08 08:35:27,922 - simpleExample - ERROR - error message
2023-12-08 08:35:27,922 - simpleExample - CRITICAL - critical message
2023-12-08 08:35:47,920 - simpleExample - DEBUG - debug message
2023-12-08 08:35:47,920 - simpleExample - INFO - info message
2023-12-08 08:35:47,920 - simpleExample - WARNING - warn message
2023-12-08 08:35:47,920 - simpleExample - ERROR - error message
2023-12-08 08:35:47,920 - simpleExample - CRITICAL - critical message
2023-12-08 08:36:07,916 - simpleExample - DEBUG - debug message
2023-12-08 08:36:07,917 - simpleExample - INFO - info message
2023-12-08 08:36:07,917 - simpleExample - WARNING - warn message
2023-12-08 08:36:07,917 - simpleExample - ERROR - error message
2023-12-08 08:36:07,917 - simpleExample - CRITICAL - critical message
2023-12-08 08:36:27,938 - simpleExample - DEBUG - debug message
2023-12-08 08:36:27,939 - simpleExample - INFO - info message
2023-12-08 08:36:27,939 - simpleExample - WARNING - warn message
2023-12-08 08:36:27,939 - simpleExample - ERROR - error message
2023-12-08 08:36:27,939 - simpleExample - CRITICAL - critical message
2023-12-08 08:36:47,938 - simpleExample - DEBUG - debug message
2023-12-08 08:36:47,938 - simpleExample - INFO - info message
2023-12-08 08:36:47,938 - simpleExample - WARNING - warn message
2023-12-08 08:36:47,938 - simpleExample - ERROR - error message
2023-12-08 08:36:47,938 - simpleExample - CRITICAL - critical message
2023-12-08 08:37:07,942 - simpleExample - DEBUG - debug message
2023-12-08 08:37:07,942 - simpleExample - INFO - info message
2023-12-08 08:37:07,942 - simpleExample - WARNING - warn message
2023-12-08 08:37:07,942 - simpleExample - ERROR - error message
2023-12-08 08:37:07,943 - simpleExample - CRITICAL - critical message
^C

"""
