#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Creating and waiting for a process"""

# end_pymotw_header
import multiprocessing


class Worker(multiprocessing.Process):

    def run(self):
        print("In {}".format(self.name))
        return


if __name__ == "__main__":
    jobs = []
    for i in range(5):
        p = Worker()
        jobs.append(p)
        p.start()
    for j in jobs:
        j.join()

"""
$ python 12_multiprocessing_subclass.py
In Worker-1
In Worker-2
In Worker-3
In Worker-4
In Worker-5
$
"""
