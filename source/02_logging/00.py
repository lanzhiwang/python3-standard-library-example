#!/usr/bin/env python3

import logging
from logging_tree import printout

logging.critical("This is a critical error message")  # 50
logging.error("This is an error message")  # 40
logging.warning("This is a warning message")  # 30
logging.info("This is an info message")  # 20
logging.debug("This is a debug message")  # 10

print()

printout()

"""
$ python 00.py
CRITICAL:root:This is a critical error message
ERROR:root:This is an error message
WARNING:root:This is a warning message

<--""
   Level WARNING
   Handler Stream <_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>
     Formatter fmt='%(levelname)s:%(name)s:%(message)s' datefmt=None
$
"""
