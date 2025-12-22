#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
""" """

# end_pymotw_header
import multiprocessing


def do_calculation(data):
    return data * 2


def start_process():
    print("Starting", multiprocessing.current_process().name)


if __name__ == "__main__":
    inputs = list(range(10))
    print("Input   :", inputs)

    builtin_outputs = map(do_calculation, inputs)
    print("Built-in:", builtin_outputs)

    pool_size = multiprocessing.cpu_count() * 2
    pool = multiprocessing.Pool(
        processes=pool_size,
        initializer=start_process,
    )
    pool_outputs = pool.map(do_calculation, inputs)
    pool.close()  # no more tasks
    pool.join()  # wrap up current tasks

    print("Pool    :", pool_outputs)

"""
$ python 22_multiprocessing_pool.py
Input   : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Built-in: <map object at 0x7f3d797762f0>
Starting ForkPoolWorker-1
Starting ForkPoolWorker-2
Starting ForkPoolWorker-3
Starting ForkPoolWorker-4
Starting ForkPoolWorker-5
Starting ForkPoolWorker-6
Starting ForkPoolWorker-7
Starting ForkPoolWorker-8
Starting ForkPoolWorker-9
Starting ForkPoolWorker-10
Starting ForkPoolWorker-11
Starting ForkPoolWorker-12
Starting ForkPoolWorker-13
Starting ForkPoolWorker-14
Starting ForkPoolWorker-15
Starting ForkPoolWorker-16
Starting ForkPoolWorker-17
Starting ForkPoolWorker-18
Starting ForkPoolWorker-19
Starting ForkPoolWorker-20
Starting ForkPoolWorker-21
Starting ForkPoolWorker-22
Starting ForkPoolWorker-23
Starting ForkPoolWorker-24
Starting ForkPoolWorker-25
Starting ForkPoolWorker-26
Starting ForkPoolWorker-27
Starting ForkPoolWorker-28
Starting ForkPoolWorker-29
Starting ForkPoolWorker-30
Starting ForkPoolWorker-31
Starting ForkPoolWorker-32
Pool    : [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
$
"""
