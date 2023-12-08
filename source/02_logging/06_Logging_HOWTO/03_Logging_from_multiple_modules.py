import logging
import mylib1
import mylib2

from logging_tree import printout

def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logging.info('Started')
    mylib1.do_something()
    mylib2.do_something()
    logging.info('Finished')

    print()
    printout()


if __name__ == '__main__':
    main()

"""
$ python 03_Logging_from_multiple_modules.py

<--""
   Level INFO
   Handler File '/python3-standard-library-example/source/02_logging/06_Logging_HOWTO/myapp.log'
     Formatter fmt='%(levelname)s:%(name)s:%(message)s' datefmt=None
   |
   o<--[06_Logging_HOWTO]
       |
       o<--"06_Logging_HOWTO.mylib2"
           Level NOTSET so inherits level INFO
$

INFO:root:Started
INFO:root:Doing something in mylib1
INFO:06_Logging_HOWTO.mylib2:Doing something in mylib2
INFO:root:Finished

"""
