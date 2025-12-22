#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
""" """

# end_pymotw_header
import multiprocessing
import pprint


def worker(d, key, value):
    d[key] = value


if __name__ == "__main__":
    mgr = multiprocessing.Manager()
    d = mgr.dict()
    jobs = [
        multiprocessing.Process(
            target=worker,
            args=(d, i, i * 2),
        )
        for i in range(10)
    ]
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
    print("Results:", d)

"""
$ python 19_multiprocessing_manager_dict.py
Results: {0: 0, 1: 2, 2: 4, 3: 6, 5: 10, 6: 12, 7: 14, 9: 18, 8: 16, 4: 8}
$
"""
