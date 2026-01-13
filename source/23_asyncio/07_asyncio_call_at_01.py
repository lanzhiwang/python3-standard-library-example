#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2014 Doug Hellmann.  All rights reserved.
"""Scheduling a callback with call_at"""

# end_pymotw_header
import asyncio
import time


def callback(n, loop):
    print("callback {} invoked at {}".format(n, loop.time()))


async def main(loop):
    now = loop.time()
    print("clock time: {}".format(time.time()))
    print("loop  time: {}".format(now))

    print("registering callbacks")
    loop.call_at(now + 0.2, callback, 1, loop)
    loop.call_at(now + 0.1, callback, 2, loop)
    loop.call_soon(callback, 3, loop)

    await asyncio.sleep(1)


event_loop = asyncio.get_event_loop()
try:
    print("entering event loop")
    event_loop.run_until_complete(main(event_loop))
finally:
    print("closing event loop")
    event_loop.close()

"""
$ python 07_asyncio_call_at_01.py
/python3-standard-library-example/source/23_asyncio/07_asyncio_call_at_01.py:29: DeprecationWarning: There is no current event loop
  event_loop = asyncio.get_event_loop()
entering event loop
clock time: 1768287465.7990425
loop  time: 5067.301678709
registering callbacks
callback 3 invoked at 5067.301872207
callback 2 invoked at 5067.405240657
callback 1 invoked at 5067.50716774
closing event loop
$
"""
