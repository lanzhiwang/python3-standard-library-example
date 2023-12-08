import logging
import logging.config
from logging_tree import printout

logging.config.fileConfig('logging.conf')

# create logger
logger = logging.getLogger('simpleExample')

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')

print()

printout()

"""
$ python 08_Configuring_Logging.py
2023-12-08 07:45:10,771 - simpleExample - DEBUG - debug message
2023-12-08 07:45:10,771 - simpleExample - INFO - info message
2023-12-08 07:45:10,772 - simpleExample - WARNING - warn message
2023-12-08 07:45:10,772 - simpleExample - ERROR - error message
2023-12-08 07:45:10,772 - simpleExample - CRITICAL - critical message

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
$

"""
