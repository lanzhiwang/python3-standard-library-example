#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
threading — 管理单个进程里的并行操作

使用线程允许一个程序在同一个进程空间中并发运行多个操作。

Thread 对象
最简单的使用一个 Thread 是去使用一个目标函数实例化它，然后调用 start() 让线程运行。

"""

#end_pymotw_header
import threading


def worker():
    """thread worker function"""
    print('Worker')


threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

"""
Worker
Worker
Worker
Worker
Worker
"""