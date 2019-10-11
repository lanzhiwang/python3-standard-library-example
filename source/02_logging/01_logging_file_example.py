#!/usr/bin/env python3
"""Example use of Python's logging module writing to a file.
"""

#end_pymotw_header
import logging

LOG_FILENAME = 'logging_example.out'
logging.basicConfig(
    filename=LOG_FILENAME,
    level=logging.DEBUG,
)

logging.debug('This message should go to the log file')

with open(LOG_FILENAME, 'rt') as f:
    body = f.read()

print('FILE:')
print(body)

"""
[root@huzhi-code logging]# python3 01_logging_file_example.py
FILE:
DEBUG:root:This message should go to the log file

[root@huzhi-code logging]# cat logging_example.out
DEBUG:root:This message should go to the log file
[root@huzhi-code logging]#
"""