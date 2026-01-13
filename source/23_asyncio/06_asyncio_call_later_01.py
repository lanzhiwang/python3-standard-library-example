#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2014 Doug Hellmann.  All rights reserved.
"""Scheduling a callback with call_later"""

# end_pymotw_header
import asyncio


def callback(n):
    print("callback {} invoked".format(n))


async def main(loop):
    print("registering callbacks")
    loop.call_later(0.2, callback, 1)
    loop.call_later(0.1, callback, 2)
    loop.call_soon(callback, 3)

    await asyncio.sleep(0.4)


event_loop = asyncio.get_event_loop()
try:
    print("entering event loop")
    event_loop.run_until_complete(main(event_loop))
finally:
    print("closing event loop")
    event_loop.close()

"""
$ python 06_asyncio_call_later_01.py
/python3-standard-library-example/source/23_asyncio/06_asyncio_call_later_01.py:24: DeprecationWarning: There is no current event loop
  event_loop = asyncio.get_event_loop()
entering event loop
registering callbacks
callback 3 invoked
callback 2 invoked
callback 1 invoked
closing event loop
$
"""
