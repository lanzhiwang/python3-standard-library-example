#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016 Doug Hellmann.  All rights reserved.
""" """

# end_pymotw_header
import threading
import time


def worker(barrier):
    print(
        threading.current_thread().name,
        "waiting for barrier with {} others".format(barrier.n_waiting),
    )
    try:
        worker_id = barrier.wait()
    except threading.BrokenBarrierError:
        print(threading.current_thread().name, "aborting")
    else:
        print(threading.current_thread().name, "after barrier", worker_id)


NUM_THREADS = 3

barrier = threading.Barrier(NUM_THREADS + 1)

threads = [
    threading.Thread(
        name="worker-%s" % i,
        target=worker,
        args=(barrier,),
    )
    for i in range(NUM_THREADS)
]

for t in threads:
    print(t.name, "starting")
    t.start()
    time.sleep(0.1)

barrier.abort()

for t in threads:
    t.join()

"""
% python threading_barrier_abort.py
worker-0 starting
worker-0 waiting for barrier with 0 others
worker-1 starting
worker-1 waiting for barrier with 1 others
worker-2 starting
worker-2 waiting for barrier with 2 others
worker-0 aborting
worker-1 aborting
worker-2 aborting
%
"""
