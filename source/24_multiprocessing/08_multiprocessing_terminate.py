#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
""" """

# end_pymotw_header
import multiprocessing
import time


def slow_worker():
    print("Starting worker")
    time.sleep(0.1)
    print("Finished worker")


if __name__ == "__main__":
    p = multiprocessing.Process(target=slow_worker)
    print("BEFORE:", p, p.is_alive())

    p.start()
    print("DURING:", p, p.is_alive())

    p.terminate()
    print("TERMINATED:", p, p.is_alive())

    p.join()
    print("JOINED:", p, p.is_alive())

"""
$ python 08_multiprocessing_terminate.py
BEFORE: <Process name='Process-1' parent=51 initial> False
DURING: <Process name='Process-1' pid=52 parent=51 started> True
TERMINATED: <Process name='Process-1' pid=52 parent=51 started> True
JOINED: <Process name='Process-1' pid=52 parent=51 stopped exitcode=-SIGTERM> False
$
"""
