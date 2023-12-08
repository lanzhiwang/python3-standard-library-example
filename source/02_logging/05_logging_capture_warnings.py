#!/usr/bin/env python3
"""Simple logging to stderr using different levels.
"""

#end_pymotw_header
import logging
import warnings
from logging_tree import printout

logging.basicConfig(
    level=logging.INFO,
)

warnings.warn('This warning is not sent to the logs')

logging.captureWarnings(True)

warnings.warn('This warning is sent to the logs')

print()

printout()

"""
$ python 05_logging_capture_warnings.py
/python3-standard-library-example/source/02_logging/05_logging_capture_warnings.py:14: UserWarning: This warning is not sent to the logs
  warnings.warn('This warning is not sent to the logs')
WARNING:py.warnings:/python3-standard-library-example/source/02_logging/05_logging_capture_warnings.py:18: UserWarning: This warning is sent to the logs
  warnings.warn('This warning is sent to the logs')


<--""
   Level INFO
   Handler Stream <_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>
     Formatter fmt='%(levelname)s:%(name)s:%(message)s' datefmt=None
   |
   o<--[py]
       |
       o<--"py.warnings"
           Level NOTSET so inherits level INFO
           Handler <NullHandler (NOTSET)>
$
"""

