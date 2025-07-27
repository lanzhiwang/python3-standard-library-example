import logging
from logging_tree import printout

logging.basicConfig(format="%(asctime)s %(message)s")
logging.warning("is when this event was logged.")
print()

printout()
print()

import logging

logging.basicConfig(format="%(asctime)s %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
logging.warning("is when this event was logged.")
print()

printout()

"""
$ python 06_Displaying_the_date_time_in_messages.py
2023-12-08 07:40:17,082 is when this event was logged.

<--""
   Level WARNING
   Handler Stream <_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>
     Formatter fmt='%(asctime)s %(message)s' datefmt=None

2023-12-08 07:40:17,082 is when this event was logged.

<--""
   Level WARNING
   Handler Stream <_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>
     Formatter fmt='%(asctime)s %(message)s' datefmt=None
$

"""
