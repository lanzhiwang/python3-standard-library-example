#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2014 Doug Hellmann.  All rights reserved.
"""Creating a Future with ensure_future"""

# end_pymotw_header
import asyncio


async def wrapped():
    print("wrapped")
    return "result"


async def inner(task):
    print("inner: starting")
    print("inner: waiting for {!r}".format(task))
    result = await task
    print("inner: task returned {!r}".format(result))


async def starter():
    print("starter: creating task")
    task = asyncio.ensure_future(wrapped())
    print("starter: waiting for inner")
    await inner(task)
    print("starter: inner returned")


event_loop = asyncio.get_event_loop()
try:
    print("entering event loop")
    result = event_loop.run_until_complete(starter())
finally:
    event_loop.close()

"""
$ python 14_asyncio_ensure_future_01.py
/python3-standard-library-example/source/23_asyncio/14_asyncio_ensure_future_01.py:31: DeprecationWarning: There is no current event loop
  event_loop = asyncio.get_event_loop()
entering event loop
starter: creating task
starter: waiting for inner
inner: starting
inner: waiting for <Task pending name='Task-2' coro=<wrapped() running at /python3-standard-library-example/source/23_asyncio/14_asyncio_ensure_future_01.py:11>>
wrapped
inner: task returned 'result'
starter: inner returned
$
"""
