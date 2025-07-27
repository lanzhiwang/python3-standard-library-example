import time
import threading
from threading import Condition, RLock

t = Condition()
a = 1


def test_th(n):
    print("thread start ", n)
    with t:
        print("thread start wait ", n)
        if t.wait(5):
            print("thread ", n)
        else:
            print("************************* ", n)
            print("sleep ", n)
            time.sleep(n)
            print("sleep over ", n)

        if n == 2:
            t.notify()


threads = [threading.Thread(target=test_th, args=(i,)) for i in range(1, 10)]
[t.start() for t in threads]

with t:
    print("start notify ")
    t.notify(2)
