#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016 Doug Hellmann.  All rights reserved.
# Written for https://pymotw.com
#
"""Running tasks in a managed group of threads."""

# end_pymotw_header
from concurrent import futures
import threading
import time


def task(n):
    print("{}: sleeping {}".format(threading.current_thread().name, n))
    time.sleep(n / 10)
    print("{}: done with {}".format(threading.current_thread().name, n))
    return n / 10


ex = futures.ThreadPoolExecutor(max_workers=2)
print("main: starting")
f = ex.submit(task, 5)
print("main: future: {}".format(f))
print("main: waiting for results")
result = f.result()
print("main: result: {}".format(result))
print("main: future after result: {}".format(f))

"""
main: starting
ThreadPoolExecutor-0_0: sleeping 5
main: future: <Future at 0x10b698550 state=running>
main: waiting for results
ThreadPoolExecutor-0_0: done with 5
main: result: 0.5
main: future after result: <Future at 0x10b698550 state=finished returned float>


main: starting
ThreadPoolExecutor-0_0: sleeping 5
ThreadPoolExecutor-0_0: done with 5

main: future: <Future at 0x10b698550 state=running>
main: waiting for results
main: result: 0.5
main: future after result: <Future at 0x10b698550 state=finished returned float>


"""
