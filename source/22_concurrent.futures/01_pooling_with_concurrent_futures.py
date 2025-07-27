#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016 Doug Hellmann.  All rights reserved.
# Written for https://pymotw.com
#
# https://github.com/lanzhiwang/Python_Parallel_Programming/blob/master/Asynchronous_programming/pooling_with_concurrent_futures.py

"""Concurrent.Futures Pooling - Chapter 4 Asynchronous Programming"""

import concurrent.futures
import time

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def evaluate_item(x):
    # count...just to make an operation
    result_item = count(x)
    # print the input item and the result
    print("item " + str(x) + " result " + str(result_item))


def count(number):
    for i in range(0, 10000000):
        i = i + 1
    return i * number


if __name__ == "__main__":
    ##Sequential Execution
    start_time = time.perf_counter()
    for item in number_list:
        evaluate_item(item)
    print("Sequential execution in " + str(time.perf_counter() - start_time), "seconds")

    ##Thread pool Execution
    start_time_1 = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for item in number_list:
            executor.submit(evaluate_item, item)
    print(
        "Thread pool execution in " + str(time.perf_counter() - start_time_1), "seconds"
    )

    ##Process pool Execution
    start_time_2 = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        for item in number_list:
            executor.submit(evaluate_item, item)
    print(
        "Process pool execution in " + str(time.perf_counter() - start_time_2),
        "seconds",
    )

"""
item 1 result 10000000
item 2 result 20000000
item 3 result 30000000
item 4 result 40000000
item 5 result 50000000
item 6 result 60000000
item 7 result 70000000
item 8 result 80000000
item 9 result 90000000
item 10 result 100000000
Sequential execution in 4.020373966999999 seconds
item 3 result 30000000
item 5 result 50000000
item 1 result 10000000
item 4 result 40000000
item 2 result 20000000
item 6 result 60000000
item 9 result 90000000
item 10 result 100000000
item 7 result 70000000
item 8 result 80000000
Thread pool execution in 3.9380919830000005 seconds
item 1 result 10000000
item 4 result 40000000
item 3 result 30000000
item 5 result 50000000
item 2 result 20000000
item 6 result 60000000
item 7 result 70000000
item 8 result 80000000
item 9 result 90000000
item 10 result 100000000
Process pool execution in 0.9513409060000004 seconds

"""
