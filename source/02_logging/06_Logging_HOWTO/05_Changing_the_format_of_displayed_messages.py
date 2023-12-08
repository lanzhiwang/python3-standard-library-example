import logging
from logging_tree import printout

logging.basicConfig(
    format='%(levelname)s:%(message)s',
    level=logging.DEBUG
)

logging.debug('This message should appear on the console')
logging.info('So should this')
logging.warning('And this, too')

print()

printout()

"""
$ python 05_Changing_the_format_of_displayed_messages.py
DEBUG:This message should appear on the console
INFO:So should this
WARNING:And this, too

<--""
   Level DEBUG
   Handler Stream <_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>
     Formatter fmt='%(levelname)s:%(message)s' datefmt=None
$

"""
