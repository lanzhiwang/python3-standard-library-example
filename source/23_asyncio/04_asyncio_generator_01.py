#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2014 Doug Hellmann.  All rights reserved.
"""Using generators instead of coroutines"""

# end_pymotw_header
import asyncio


@asyncio.coroutine
def outer():
    print("in outer")
    print("waiting for result1")
    result1 = yield from phase1()
    print("waiting for result2")
    result2 = yield from phase2(result1)
    return (result1, result2)


@asyncio.coroutine
def phase1():
    print("in phase1")
    return "result1"


@asyncio.coroutine
def phase2(arg):
    print("in phase2")
    return "result2 derived from {}".format(arg)


event_loop = asyncio.get_event_loop()
try:
    return_value = event_loop.run_until_complete(outer())
    print("return value: {!r}".format(return_value))
finally:
    event_loop.close()

"""
$ python 04_asyncio_generator_01.py
Traceback (most recent call last):
  File "/python3-standard-library-example/source/23_asyncio/04_asyncio_generator_01.py", line 11, in <module>
    @asyncio.coroutine
     ^^^^^^^^^^^^^^^^^
AttributeError: module 'asyncio' has no attribute 'coroutine'. Did you mean: 'coroutines'?
$

作为一名高级开发人员, 看到这段代码时, 首先要注意到的是:
这段代码使用的是 Python 3.4 - 3.5 时代的"生成器语法(Generator-based Coroutines)".
在现代 Python(3.7+, 特别是 3.11 之后)中, @asyncio.coroutine 和 yield from 已经被废弃并在最新版本中移除.
现在的标准是使用 async def 和 await.
"""
