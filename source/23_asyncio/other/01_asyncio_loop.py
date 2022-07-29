#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2014 Doug Hellmann.  All rights reserved.
# https://github.com/lanzhiwang/Python_Parallel_Programming/blob/master/Asynchronous_programming/asyncio_loop.py
#
"""Asyncio.loop - Chapter 4 Asynchronous Programming
"""

#end_pymotw_header
import asyncio
import datetime
import time

def function_1(end_time, loop):
    print('function_1: ', loop.time())
    print ("function_1 called")
    print (end_time)
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, function_2, end_time, loop)
    else:
        loop.stop()

def function_2(end_time, loop):
    print('function_2: ', loop.time())
    print ("function_2 called ")
    print (end_time)
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, function_3, end_time, loop)
    else:
        loop.stop()

def function_3(end_time, loop):
    print('function_3: ', loop.time())
    print ("function_3 called")
    print (end_time)
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, function_4, end_time, loop)
    else:
        loop.stop()

def function_4(end_time, loop):
    print('function_4: ', loop.time())
    print ("function_4 called")
    print (end_time)
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, function_1, end_time, loop)
    else:
        loop.stop()

loop = asyncio.get_event_loop()

# Schedule the first call to display_date()
print('main: ', loop.time())
end_loop_1 = loop.time() + 9.0
loop.call_soon(function_1, end_loop_1, loop)
#loop.call_soon(function_4, end_loop_1, loop)

# Blocking call interrupted by loop.stop()
print('run_forever')
loop.run_forever()
loop.close()

"""
main:  0.122551883
run_forever
function_1:  0.122632356
function_1 called
9.122583724
function_2:  1.127779176
function_2 called
9.122583724
function_3:  2.128241551
function_3 called
9.122583724
function_4:  3.133440338
function_4 called
9.122583724
function_1:  4.137383423
function_1 called
9.122583724
function_2:  5.141521592
function_2 called
9.122583724
function_3:  6.144285939
function_3 called
9.122583724
function_4:  7.147034259
function_4 called
9.122583724
function_1:  8.149709994
function_1 called
9.122583724
"""
