#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Spawn a Process – Chapter 3: Process Based Parallelism"""
# end_pymotw_header
import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time
from datetime import datetime


def test_with_barrier(synchronizer, serializer):
    name = multiprocessing.current_process().name
    synchronizer.wait()
    now = time()
    with serializer:
        print("process %s ----> %s" % (name, datetime.fromtimestamp(now)))


def test_without_barrier():
    name = multiprocessing.current_process().name
    now = time()
    print("process %s ----> %s" % (name, datetime.fromtimestamp(now)))


if __name__ == "__main__":
    synchronizer = Barrier(2)
    serializer = Lock()
    Process(
        name="p1 - test_with_barrier",
        target=test_with_barrier,
        args=(synchronizer, serializer),
    ).start()
    Process(
        name="p2 - test_with_barrier",
        target=test_with_barrier,
        args=(synchronizer, serializer),
    ).start()
    Process(name="p3 - test_without_barrier", target=test_without_barrier).start()
    Process(name="p4 - test_without_barrier", target=test_without_barrier).start()
