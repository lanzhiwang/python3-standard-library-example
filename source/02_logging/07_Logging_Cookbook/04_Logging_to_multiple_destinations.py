import logging
from logging_tree import printout

# set up logging to file - see previous section for more details
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='myapp.log',
                    filemode='w')
# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger('').addHandler(console)

# Now, we can log to the root logger, or any other logger. First the root...
logging.info('Jackdaws love my big sphinx of quartz.')

# Now, define a couple of other loggers which might represent areas in your
# application:

logger1 = logging.getLogger('myapp.area1')
logger2 = logging.getLogger('myapp.area2')

logger1.debug('Quick zephyrs blow, vexing daft Jim.')
logger1.info('How quickly daft jumping zebras vex.')
logger2.warning('Jail zesty vixen who grabbed pay from quack.')
logger2.error('The five boxing wizards jump quickly.')

print()

printout()

"""
$ python 04_Logging_to_multiple_destinations.py
root        : INFO     Jackdaws love my big sphinx of quartz.
myapp.area1 : INFO     How quickly daft jumping zebras vex.
myapp.area2 : WARNING  Jail zesty vixen who grabbed pay from quack.
myapp.area2 : ERROR    The five boxing wizards jump quickly.

<--""
   Level DEBUG
   Handler File '/python3-standard-library-example/source/02_logging/07_Logging_Cookbook/myapp.log'
     Formatter fmt='%(asctime)s %(name)-12s %(levelname)-8s %(message)s' datefmt='%m-%d %H:%M'
   Handler Stream <_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>
     Level INFO
     Formatter fmt='%(name)-12s: %(levelname)-8s %(message)s' datefmt=None
   |
   o<--[myapp]
       |
       o<--"myapp.area1"
       |   Level NOTSET so inherits level DEBUG
       |
       o<--"myapp.area2"
           Level NOTSET so inherits level DEBUG
$
"""