#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Passing arguments to threads when they are created"""

# end_pymotw_header
import multiprocessing
import logging
import time

logging.basicConfig(
    level=logging.DEBUG,
    format="(%(processName)-10s) %(message)s",
)


def worker(num, d):
    """thread worker function"""
    print("Worker:", num)
    d["a"] = "b"
    logging.debug(d)


d = {}
d["a"] = "a"
d["b"] = "b"
logging.debug(d)

if __name__ == "__main__":
    jobs = []
    for i in range(2):
        p = multiprocessing.Process(target=worker, args=(i, d))
        jobs.append(p)
        p.start()

time.sleep(3)
logging.debug(d)

"""
Worker: 0
Worker: 1
Worker: 2
Worker: 3
Worker: 4
"""
