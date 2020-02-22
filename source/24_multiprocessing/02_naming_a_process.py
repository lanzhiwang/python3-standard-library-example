#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Spawn a Process – Chapter 3: Process Based Parallelism
"""
#end_pymotw_header
import multiprocessing
import time

def foo():
    name = multiprocessing.current_process().name
    print ("Starting %s" % name)
    time.sleep(3)
    print ("Exiting %s" % name)

if __name__ == '__main__':
    process_with_name = multiprocessing.Process(name='foo_process', target=foo)
    process_with_name.start()

    process_with_default_name = multiprocessing.Process(target=foo)
    process_with_default_name.start()

"""
Starting foo_process
Starting Process-2
Exiting foo_process
Exiting Process-2
"""