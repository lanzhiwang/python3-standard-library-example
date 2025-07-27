import logging
from logging_tree import printout

logging.basicConfig(filename="example.log", encoding="utf-8", level=logging.DEBUG)
logging.debug("This message should go to the log file")
logging.info("So should this")
logging.warning("And this, too")
logging.error("And non-ASCII stuff, too, like Øresund and Malmö")

print()

printout()


"""
$ python 02_Logging_to_a_file.py

<--""
   Level DEBUG
   Handler File '/python3-standard-library-example/source/02_logging/06_Logging_HOWTO/example.log'
     Formatter fmt='%(levelname)s:%(name)s:%(message)s' datefmt=None
$
"""
