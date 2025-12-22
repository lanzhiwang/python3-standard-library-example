#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Multiple concurrent access to a resource"""
# end_pymotw_header
import random
import multiprocessing
import time


class ActivePool:

    def __init__(self):
        super(ActivePool, self).__init__()
        self.mgr = multiprocessing.Manager()
        self.active = self.mgr.list()
        self.lock = multiprocessing.Lock()

    def makeActive(self, name):
        with self.lock:
            self.active.append(name)

    def makeInactive(self, name):
        with self.lock:
            self.active.remove(name)

    def __str__(self):
        with self.lock:
            return str(self.active)


def worker(s, pool):
    name = multiprocessing.current_process().name
    with s:
        pool.makeActive(name)
        print("Activating {} now running {}".format(name, pool))
        time.sleep(random.random())
        pool.makeInactive(name)


if __name__ == "__main__":
    pool = ActivePool()
    s = multiprocessing.Semaphore(3)
    jobs = [
        multiprocessing.Process(
            target=worker,
            name=str(i),
            args=(s, pool),
        )
        for i in range(10)
    ]

    for j in jobs:
        j.start()

    while True:
        alive = 0
        for j in jobs:
            if j.is_alive():
                alive += 1
                j.join(timeout=0.1)
                print("Now running {}".format(pool))
        if alive == 0:
            # all done
            break

"""
$ python 18_multiprocessing_semaphore.py
Activating 0 now running ['0']
Activating 3 now running ['0', '3']
Activating 1 now running ['0', '3', '1']
Now running ['0', '3', '1']
Activating 2 now running ['0', '1', '2']
Now running ['0', '1', '2']
Now running ['0', '1', '2']
Now running ['0', '1', '2']
Now running ['0', '1', '2']
Now running ['0', '1', '2']
Activating 4 now running ['0', '2', '4']
Now running ['0', '2', '4']
Activating 7 now running ['0', '4', '7']
Now running ['0', '4', '7']
Now running ['0', '4', '7']
Activating 8 now running ['4', '7', '8']
Now running ['4', '7', '8']
Now running ['4', '7', '8']
Activating 5 now running ['4', '7', '5']
Activating 6 now running ['4', '7', '6']
Now running ['4', '7', '6']
Activating 9 now running ['4', '7', '9']
Now running ['4', '7', '9']
Now running ['4', '7', '9']
Now running ['4', '7']
Now running ['7']
Now running ['7']
Now running ['7']
Now running []
$
"""
