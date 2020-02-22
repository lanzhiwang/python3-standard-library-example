#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Spawn a Process – Chapter 3: Process Based Parallelism
"""
#end_pymotw_header
import multiprocessing

class MyProcess(multiprocessing.Process):
    def run(self):
        print ('called run method in %s' % self.name)
        return

if __name__ == '__main__':
    jobs = []

    for i in range(5):
        p = MyProcess()
        jobs.append(p)
        p.start()
        p.join()

"""
called run method in MyProcess-1
called run method in MyProcess-2
called run method in MyProcess-3
called run method in MyProcess-4
called run method in MyProcess-5
"""