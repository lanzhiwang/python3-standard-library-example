import logging
import auxiliary_module

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

"""
2019-10-10 10:29:40,605 - spam_application - INFO - creating an instance of auxiliary_module.Auxiliary
2019-10-10 10:29:40,605 - spam_application.auxiliary.Auxiliary - INFO - creating an instance of Auxiliary
2019-10-10 10:29:40,605 - spam_application - INFO - created an instance of auxiliary_module.Auxiliary
2019-10-10 10:29:40,606 - spam_application - INFO - calling auxiliary_module.Auxiliary.do_something
2019-10-10 10:29:40,606 - spam_application.auxiliary.Auxiliary - INFO - doing something
2019-10-10 10:29:40,606 - spam_application.auxiliary.Auxiliary - INFO - done doing something
2019-10-10 10:29:40,606 - spam_application - INFO - finished auxiliary_module.Auxiliary.do_something
2019-10-10 10:29:40,606 - spam_application - INFO - calling auxiliary_module.some_function()
2019-10-10 10:29:40,606 - spam_application.auxiliary - INFO - received a call to "some_function"
2019-10-10 10:29:40,606 - spam_application - INFO - done with auxiliary_module.some_function()
"""