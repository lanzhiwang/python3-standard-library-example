import logging
from random import choice
from logging_tree import printout

class ContextFilter(logging.Filter):
    """
    This is a filter which injects contextual information into the log.

    Rather than use actual contextual information, we just use random
    data in this demo.
    """

    USERS = ['jim', 'fred', 'sheila']
    IPS = ['123.231.231.123', '127.0.0.1', '192.168.0.1']

    def filter(self, record):

        record.ip = choice(ContextFilter.IPS)
        record.user = choice(ContextFilter.USERS)
        return True

if __name__ == '__main__':
    levels = (logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL)
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)-15s %(name)-5s %(levelname)-8s IP: %(ip)-15s User: %(user)-8s %(message)s')
    a1 = logging.getLogger('a.b.c')
    a2 = logging.getLogger('d.e.f')

    f = ContextFilter()
    a1.addFilter(f)
    a2.addFilter(f)
    a1.debug('A debug message')
    a1.info('An info message with %s', 'some parameters')
    for x in range(10):
        lvl = choice(levels)
        lvlname = logging.getLevelName(lvl)
        a2.log(lvl, 'A message at %s level with %d %s', lvlname, 2, 'parameters')

    print()
    printout()

"""
$ python 09_Using_Filters_to_impart_contextual_information.py
2023-12-08 08:44:20,837 a.b.c DEBUG    IP: 123.231.231.123 User: sheila   A debug message
2023-12-08 08:44:20,837 a.b.c INFO     IP: 192.168.0.1     User: jim      An info message with some parameters
2023-12-08 08:44:20,837 d.e.f WARNING  IP: 192.168.0.1     User: sheila   A message at WARNING level with 2 parameters
2023-12-08 08:44:20,837 d.e.f WARNING  IP: 123.231.231.123 User: fred     A message at WARNING level with 2 parameters
2023-12-08 08:44:20,838 d.e.f CRITICAL IP: 127.0.0.1       User: fred     A message at CRITICAL level with 2 parameters
2023-12-08 08:44:20,838 d.e.f DEBUG    IP: 127.0.0.1       User: fred     A message at DEBUG level with 2 parameters
2023-12-08 08:44:20,838 d.e.f DEBUG    IP: 123.231.231.123 User: jim      A message at DEBUG level with 2 parameters
2023-12-08 08:44:20,838 d.e.f CRITICAL IP: 123.231.231.123 User: sheila   A message at CRITICAL level with 2 parameters
2023-12-08 08:44:20,838 d.e.f ERROR    IP: 192.168.0.1     User: sheila   A message at ERROR level with 2 parameters
2023-12-08 08:44:20,838 d.e.f WARNING  IP: 192.168.0.1     User: sheila   A message at WARNING level with 2 parameters
2023-12-08 08:44:20,838 d.e.f ERROR    IP: 127.0.0.1       User: sheila   A message at ERROR level with 2 parameters
2023-12-08 08:44:20,838 d.e.f CRITICAL IP: 192.168.0.1     User: fred     A message at CRITICAL level with 2 parameters

<--""
   Level DEBUG
   Handler Stream <_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>
     Formatter fmt='%(asctime)-15s %(name)-5s %(levelname)-8s IP: %(ip)-15s User: %(user)-8s %(message)s' datefmt=None
   |
   o<--[a]
   |   |
   |   o<--[a.b]
   |       |
   |       o<--"a.b.c"
   |           Level NOTSET so inherits level DEBUG
   |           Filter <__main__.ContextFilter object at 0x7f49b9746920>
   |
   o<--[d]
       |
       o<--[d.e]
           |
           o<--"d.e.f"
               Level NOTSET so inherits level DEBUG
               Filter <__main__.ContextFilter object at 0x7f49b9746920>
$

"""
