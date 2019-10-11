import logging
logging.basicConfig(format='%(asctime)s %(message)s')
logging.warning('is when this event was logged.')

"""
2010-12-12 11:41:42,612 is when this event was logged.
"""

import logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.warning('is when this event was logged.')

"""
12/12/2010 11:46:36 AM is when this event was logged.
"""