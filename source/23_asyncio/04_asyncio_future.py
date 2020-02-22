#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2014 Doug Hellmann.  All rights reserved.
# https://github.com/lanzhiwang/Python_Parallel_Programming/blob/master/Asynchronous_programming/asyncio_future.py
# 
"""Asyncio.Futures -  Chapter 4 Asynchronous Programming
"""

#end_pymotw_header
import asyncio
import sys

#SUM OF N INTEGERS
@asyncio.coroutine
def first_coroutine(future, n):
    count = 0
    for i in range(1, n+1):
        count = count + i
    yield from asyncio.sleep(4)
    future.set_result("first coroutine (sum of N integers) result = %s" % count)
 

#FACTORIAL(N)
@asyncio.coroutine
def second_coroutine(future, n):
    count = 1
    for i in range(2, n+1):
        count *= i
    yield from asyncio.sleep(3)
    future.set_result("second coroutine (factorial) result = %s" % count)
 
def got_result(future):
    print(future.result())

    
if __name__ == "__main__":
    n1 = 2
    n2 = 3

    loop = asyncio.get_event_loop()
    future1 = asyncio.Future()
    future2 = asyncio.Future()
   
    tasks = [first_coroutine(future1, n1), second_coroutine(future2, n2)]
 
    future1.add_done_callback(got_result)
    future2.add_done_callback(got_result)
 
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

"""
second coroutine (factorial) result = 6
first coroutine (sum of N integers) result = 3
"""