import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logging.debug('This message should appear on the console')
logging.info('So should this')
logging.warning('And this, too')

"""
DEBUG:This message should appear on the console
INFO:So should this
WARNING:And this, too
"""