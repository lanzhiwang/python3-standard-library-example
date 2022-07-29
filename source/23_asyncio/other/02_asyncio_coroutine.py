#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2014 Doug Hellmann.  All rights reserved.
# https://github.com/lanzhiwang/Python_Parallel_Programming/blob/master/Asynchronous_programming/Asyncio_coroutine.py
# 
"""Asyncio Finite State Machine
"""

#end_pymotw_header
import asyncio
import time
from random import randint


@asyncio.coroutine
def StartState():
    print ("Start State called")
    input_value = randint(0,1)
    time.sleep(1)
    print('input_value: %s\n' % input_value)
    if (input_value == 0):
        result = yield from State2(input_value)
    else :
        result = yield from State1(input_value)
    print("StartState result: %s" % result)
    
    
@asyncio.coroutine
def State1(transition_value):
    print('State1')
    input_value = randint(0,1)
    time.sleep(1)
    print("...Evaluating...")
    print('input_value: %s\n' % input_value)
    if (input_value == 0):
        result =  yield from State3(input_value)
    else :
        result = yield from State2(input_value)
    print('state1 return: %s' % result)
    return 'state1'

@asyncio.coroutine
def State2(transition_value):
    print('State2')
    input_value = randint(0,1)
    time.sleep(1)
    print("...Evaluating...")
    print('input_value: %s\n' % input_value)
    if (input_value == 0):
        result = yield from State1(input_value)
    else :
        result = yield from State3(input_value)
    print('state2 return: %s' % result)
    return 'state2'


@asyncio.coroutine
def State3(transition_value):
    print('State3')
    input_value = randint(0,1)
    time.sleep(1)
    print("...Evaluating...")
    print('input_value: %s\n' % input_value)
    if (input_value == 0):
        result = yield from State1(input_value)
    else :
        result = yield from EndState(input_value)
    print('state3 return: %s' % result)
    return 'state3'


@asyncio.coroutine
def EndState(transition_value):
    print('EndState')
    print("...Stop Computation...")
    return "End State"


if __name__ == "__main__":
    print("Finite State Machine simulation with Asyncio Coroutine")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(StartState())

"""
% python3 02_asyncio_coroutine.py
Finite State Machine simulation with Asyncio Coroutine
Start State called
input_value: 0

State2
...Evaluating...
input_value: 0

State1
...Evaluating...
input_value: 0

State3
...Evaluating...
input_value: 0

State1
...Evaluating...
input_value: 0

State3
...Evaluating...
input_value: 1

EndState
...Stop Computation...
state3 return: End State
state1 return: state3
state3 return: state1
state1 return: state3
state2 return: state1
StartState result: state2
"""