#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Passing arguments to threads when they are created"""

# end_pymotw_header
import multiprocessing


def worker(num):
    """thread worker function"""
    print("Worker:", num)


if __name__ == "__main__":
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()

"""
$ python 02_multiprocessing_simpleargs.py
Worker: 0
Worker: 1
Worker: 2
Worker: 3
Worker: 4
$
"""
