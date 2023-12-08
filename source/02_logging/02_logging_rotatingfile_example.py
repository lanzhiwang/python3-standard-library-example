#!/usr/bin/env python3
"""Log to a file, creating a new file every 20 bytes

See http://blog.doughellmann.com/2007/05/pymotw-logging.html

"""

#end_pymotw_header
import glob
import logging
import logging.handlers
from logging_tree import printout

LOG_FILENAME = 'logging_rotatingfile_example.out'

# Set up a specific logger with our desired output level
my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)

# Add the log message handler to the logger
handler = logging.handlers.RotatingFileHandler(
    LOG_FILENAME,
    maxBytes=20,
    backupCount=5,
)
my_logger.addHandler(handler)

# Log some messages
for i in range(20):
    my_logger.debug('i = %d' % i)

# See what files are created
logfiles = glob.glob('%s*' % LOG_FILENAME)
for filename in sorted(logfiles):
    print(filename)

print()

printout()

"""
$ python 02_logging_rotatingfile_example.py
logging_rotatingfile_example.out
logging_rotatingfile_example.out.1
logging_rotatingfile_example.out.2
logging_rotatingfile_example.out.3
logging_rotatingfile_example.out.4
logging_rotatingfile_example.out.5

<--""
   Level WARNING
   |
   o<--"MyLogger"
       Level DEBUG
       Handler RotatingFile '/python3-standard-library-example/source/02_logging/logging_rotatingfile_example.out' maxBytes=20 backupCount=5
$
"""
