#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016 Doug Hellmann.  All rights reserved.
# Written for https://pymotw.com
#
"""Running tasks in a managed group of threads.
"""

#end_pymotw_header
from concurrent import futures
import threading
import time


def task(n):
    print('{}: sleeping {}'.format(threading.current_thread().name, n))
    time.sleep(n / 10)
    print('{}: done with {}'.format(threading.current_thread().name, n))
    return n / 10


ex = futures.ThreadPoolExecutor(max_workers=2)
print('main: starting')
results = ex.map(task, range(5, 0, -1))
print('main: unprocessed results {}'.format(results))
print('main: waiting for real results')
real_results = list(results)
print('main: results: {}'.format(real_results))

"""
main: starting
ThreadPoolExecutor-0_0: sleeping 5
ThreadPoolExecutor-0_1: sleeping 4
main: unprocessed results <generator object Executor.map.<locals>.result_iterator at 0x107ec07c8>
main: waiting for real results
ThreadPoolExecutor-0_1: done with 4
ThreadPoolExecutor-0_1: sleeping 3
ThreadPoolExecutor-0_0: done with 5
ThreadPoolExecutor-0_0: sleeping 2
ThreadPoolExecutor-0_1: done with 3
ThreadPoolExecutor-0_1: sleeping 1
ThreadPoolExecutor-0_0: done with 2
ThreadPoolExecutor-0_1: done with 1
main: results: [0.5, 0.4, 0.3, 0.2, 0.1]


main: starting
ThreadPoolExecutor-0_0: sleeping 5
ThreadPoolExecutor-0_0: done with 5

ThreadPoolExecutor-0_1: sleeping 4
ThreadPoolExecutor-0_1: done with 4

ThreadPoolExecutor-0_1: sleeping 3
ThreadPoolExecutor-0_1: done with 3

ThreadPoolExecutor-0_0: sleeping 2
ThreadPoolExecutor-0_0: done with 2

ThreadPoolExecutor-0_1: sleeping 1
ThreadPoolExecutor-0_1: done with 1

main: unprocessed results <generator object Executor.map.<locals>.result_iterator at 0x107ec07c8>
main: waiting for real results
main: results: [0.5, 0.4, 0.3, 0.2, 0.1]

"""