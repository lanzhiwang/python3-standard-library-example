#!/usr/bin/env python3
"""Example use of Python's logging module writing to a file."""

# end_pymotw_header
import logging
from logging_tree import printout

LOG_FILENAME = "logging_example.out"
logging.basicConfig(
    filename=LOG_FILENAME,
    level=logging.DEBUG,
)

logging.debug("This message should go to the log file")

with open(LOG_FILENAME, "rt") as f:
    body = f.read()

print("FILE:")
print(body)

printout()

"""
$ python 01_logging_file_example.py
FILE:
DEBUG:root:This message should go to the log file

<--""
   Level DEBUG
   Handler File '/python3-standard-library-example/source/02_logging/logging_example.out'
     Formatter fmt='%(levelname)s:%(name)s:%(message)s' datefmt=None

$ ls -al
total 40
drwxr-xr-x  11 root root   352 Dec  8 06:54 .
drwxr-xr-x 120 root root  3840 Aug  8  2020 ..
-rw-r--r--   1 root root  1253 Dec  8 06:54 01_logging_file_example.py
-rw-r--r--   1 root root  1324 Feb 21  2020 02_logging_rotatingfile_example.py
-rw-r--r--   1 root root  1195 Feb 21  2020 03_logging_level_example.py
-rw-r--r--   1 root root   629 Feb 21  2020 04_logging_modules_example.py
-rw-r--r--   1 root root   711 Feb 21  2020 05_logging_capture_warnings.py
drwxr-xr-x  11 root root   352 Feb 21  2020 06_Logging_HOWTO
drwxr-xr-x  11 root root   352 Feb 21  2020 07_Logging_Cookbook
-rw-r--r--   1 root root 14946 Dec  8 06:47 README.md
-rw-r--r--   1 root root    50 Dec  8 06:54 logging_example.out
$
"""
