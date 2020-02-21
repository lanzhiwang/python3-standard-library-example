#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016 Doug Hellmann.  All rights reserved.
# Written for https://pymotw.com
#
"""Running tasks in a managed group of processes.
"""

#end_pymotw_header
from concurrent import futures
import os
import time


def task(n):
    time.sleep(0.5)
    return (n, os.getpid())


ex = futures.ProcessPoolExecutor(max_workers=2)
results = ex.map(task, range(5, 0, -1))
for n, pid in results:
    print('ran task {} in process {}'.format(n, pid))

"""
ran task 5 in process 9372
ran task 4 in process 9373
ran task 3 in process 9372
ran task 2 in process 9373
ran task 1 in process 9372
"""