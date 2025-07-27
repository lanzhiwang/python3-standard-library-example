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
entering event loop
clock time: 1582340582.6737978
loop  time: 0.10887285
registering callbacks
callback 3 invoked at 0.108962749
callback 2 invoked at 0.213985959
callback 1 invoked at 0.310122497
closing event loop
"""
