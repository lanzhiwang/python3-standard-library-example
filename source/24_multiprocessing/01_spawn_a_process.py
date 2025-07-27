#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Spawn a Process – Chapter 3: Process Based Parallelism"""
# end_pymotw_header
import multiprocessing


def function(i):
    print("called function in process: %s" % i)
    return


if __name__ == "__main__":
    Process_jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=function, args=(i,))
        Process_jobs.append(p)
        p.start()
        p.join()

"""
called function in process: 0
called function in process: 1
called function in process: 2
called function in process: 3
called function in process: 4
"""
