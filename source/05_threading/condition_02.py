import threading
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

condition = threading.Condition()
def f():
    condition.acquire()
    logging.debug("Waiting for the condition")
    condition.wait()
    logging.debug("Done waiting")
    condition.release()

thread1 = threading.Thread(target=f)
thread2 = threading.Thread(target=f)
thread1.start()
thread2.start()

condition.acquire()
condition.notify()
condition.release()

condition.acquire()
condition.notify()
condition.release()

"""
(venv) huzhi@huzhideMacBook-Pro 05_threading % python condition_02.py
(Thread-1  ) Waiting for the condition
(Thread-2  ) Waiting for the condition
(Thread-1  ) Done waiting
(Thread-2  ) Done waiting
(venv) huzhi@huzhideMacBook-Pro 05_threading % python condition_02.py
(Thread-1  ) Waiting for the condition
(Thread-2  ) Waiting for the condition
(Thread-1  ) Done waiting
(Thread-2  ) Done waiting
(venv) huzhi@huzhideMacBook-Pro 05_threading % python condition_02.py
(Thread-1  ) Waiting for the condition
(Thread-2  ) Waiting for the condition
(Thread-1  ) Done waiting
(Thread-2  ) Done waiting
(venv) huzhi@huzhideMacBook-Pro 05_threading %
"""
