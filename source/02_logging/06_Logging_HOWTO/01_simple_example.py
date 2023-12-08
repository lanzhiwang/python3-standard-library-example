import logging
from logging_tree import printout

logging.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')  # will not print anything

print()

printout()

"""
$ python 01_simple_example.py
WARNING:root:Watch out!

<--""
   Level WARNING
   Handler Stream <_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>
     Formatter fmt='%(levelname)s:%(name)s:%(message)s' datefmt=None
$

"""
