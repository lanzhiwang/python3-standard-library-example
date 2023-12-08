#!/usr/bin/env python3
"""Simulate logging from different modules

See http://blog.doughellmann.com/2007/05/pymotw-logging.html
"""

#end_pymotw_header
import logging
from logging_tree import printout

logging.basicConfig(level=logging.WARNING)

logger1 = logging.getLogger('package1.module1')
logger2 = logging.getLogger('package2.module2')

logger1.warning('This message comes from one module')
logger2.warning('This comes from another module')
print()

printout()

"""
$ python3 04_logging_modules_example.py
WARNING:package1.module1:This message comes from one module
WARNING:package2.module2:This comes from another module

<--""
   Level WARNING
   Handler Stream <_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>
     Formatter fmt='%(levelname)s:%(name)s:%(message)s' datefmt=None
   |
   o<--[package1]
   |   |
   |   o<--"package1.module1"
   |       Level NOTSET so inherits level WARNING
   |
   o<--[package2]
       |
       o<--"package2.module2"
           Level NOTSET so inherits level WARNING
$
"""
