import logging
import auxiliary_module
from logging_tree import printout

# create logger with 'spam_application'
logger = logging.getLogger('spam_application')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

logger.info('creating an instance of auxiliary_module.Auxiliary')
a = auxiliary_module.Auxiliary()
logger.info('created an instance of auxiliary_module.Auxiliary')
logger.info('calling auxiliary_module.Auxiliary.do_something')
a.do_something()
logger.info('finished auxiliary_module.Auxiliary.do_something')
logger.info('calling auxiliary_module.some_function()')
auxiliary_module.some_function()
logger.info('done with auxiliary_module.some_function()')

print()

printout()

"""
$ python main_module.py

<--""
   Level WARNING
   |
   o<--"spam_application"
       Level DEBUG
       Handler File '/python3-standard-library-example/source/02_logging/07_Logging_Cookbook/01_Using_logging_in_multiple_modules/spam.log'
         Level DEBUG
         Formatter fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s' datefmt=None
       Handler Stream <_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>
         Level ERROR
         Formatter fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s' datefmt=None
       |
       o<--"spam_application.auxiliary"
           Level NOTSET so inherits level DEBUG
           |
           o<--"spam_application.auxiliary.Auxiliary"
               Level NOTSET so inherits level DEBUG
$
"""
