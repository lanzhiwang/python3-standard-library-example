import logging
from logging_tree import printout

# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')

print()

printout()

"""
$ python 07_Configuring_Logging.py
2023-12-08 07:42:31,632 - simple_example - DEBUG - debug message
2023-12-08 07:42:31,632 - simple_example - INFO - info message
2023-12-08 07:42:31,632 - simple_example - WARNING - warn message
2023-12-08 07:42:31,632 - simple_example - ERROR - error message
2023-12-08 07:42:31,632 - simple_example - CRITICAL - critical message

<--""
   Level WARNING
   |
   o<--"simple_example"
       Level DEBUG
       Handler Stream <_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>
         Level DEBUG
         Formatter fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s' datefmt=None
$
"""
