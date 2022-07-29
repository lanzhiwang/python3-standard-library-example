#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""

能够创建一个线程并且传递给它参数告诉它做什么是很有用的。
任何对象都可以作为参数传递给线程。这个例子传递了一个数字，然后在线程中打印出来。
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