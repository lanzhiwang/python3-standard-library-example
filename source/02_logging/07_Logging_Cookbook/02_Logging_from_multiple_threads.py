import logging
import threading
import time

def worker(arg):
    while not arg['stop']:
        logging.debug('Hi from myfunc')
        time.sleep(0.5)

def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(relativeCreated)6d %(threadName)s %(message)s'
    )
    info = {'stop': False}
    thread = threading.Thread(target=worker, args=(info,))
    thread.start()
    while True:
        try:
            logging.debug('Hello from main')
            time.sleep(0.75)
        except KeyboardInterrupt:
            info['stop'] = True
            break
    thread.join()

if __name__ == '__main__':
    main()

"""
$ python 02_Logging_from_multiple_threads.py
     1 Thread-1 (worker) Hi from myfunc
     1 MainThread Hello from main
   504 Thread-1 (worker) Hi from myfunc
   754 MainThread Hello from main
  1006 Thread-1 (worker) Hi from myfunc
  1506 MainThread Hello from main
  1507 Thread-1 (worker) Hi from myfunc
  2011 Thread-1 (worker) Hi from myfunc
  2258 MainThread Hello from main
  2512 Thread-1 (worker) Hi from myfunc
  3011 MainThread Hello from main
  3013 Thread-1 (worker) Hi from myfunc
  3516 Thread-1 (worker) Hi from myfunc
  3763 MainThread Hello from main
  4022 Thread-1 (worker) Hi from myfunc
  4516 MainThread Hello from main
  4524 Thread-1 (worker) Hi from myfunc
  5003 Thread-1 (worker) Hi from myfunc
^C$
$
"""
