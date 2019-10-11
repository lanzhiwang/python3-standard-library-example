#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Passing arguments to threads when they are created
"""

#end_pymotw_header
import threading


def worker(num):
    """thread worker function"""
    print('Worker: %s' % num)


threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

"""
Worker: 0
Worker: 1
Worker: 2
Worker: 3
Worker: 4
"""