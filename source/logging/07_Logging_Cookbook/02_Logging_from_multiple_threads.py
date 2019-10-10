import logging
import threading
import time


def worker(arg):
    while not arg['stop']:
        logging.debug('Hi from myfunc')
        time.sleep(0.5)


def main():
    logging.basicConfig(level=logging.DEBUG, format='%(relativeCreated)6d %(threadName)s %(message)s')
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
     0 Thread-1 Hi from myfunc
     1 MainThread Hello from main
   501 Thread-1 Hi from myfunc
   752 MainThread Hello from main
  1002 Thread-1 Hi from myfunc
  1503 MainThread Hello from main
  1503 Thread-1 Hi from myfunc
  2004 Thread-1 Hi from myfunc
  2254 MainThread Hello from main
  2505 Thread-1 Hi from myfunc
  3005 MainThread Hello from main
  3005 Thread-1 Hi from myfunc
  3506 Thread-1 Hi from myfunc
  3756 MainThread Hello from main
  4007 Thread-1 Hi from myfunc
  4507 MainThread Hello from main
  4508 Thread-1 Hi from myfunc
  5009 Thread-1 Hi from myfunc
  5258 MainThread Hello from main
  5509 Thread-1 Hi from myfunc
  6009 MainThread Hello from main
  6010 Thread-1 Hi from myfunc
  6511 Thread-1 Hi from myfunc
  6760 MainThread Hello from main
  7012 Thread-1 Hi from myfunc
  7512 MainThread Hello from main
  7513 Thread-1 Hi from myfunc
  8013 Thread-1 Hi from myfunc
  8263 MainThread Hello from main
  8514 Thread-1 Hi from myfunc
  9014 MainThread Hello from main
  9015 Thread-1 Hi from myfunc
  9516 Thread-1 Hi from myfunc
"""