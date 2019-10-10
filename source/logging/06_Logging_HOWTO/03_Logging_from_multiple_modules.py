# myapp.py
import logging
import mylib

def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logging.info('Started')
    mylib.do_something()
    logging.info('Finished')

if __name__ == '__main__':
    main()

"""
# mylib.py
import logging

def do_something():
    logging.info('Doing something')
    

If you run myapp.py, you should see this in myapp.log:

INFO:root:Started
INFO:root:Doing something
INFO:root:Finished
"""
