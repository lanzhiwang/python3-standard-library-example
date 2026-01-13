#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2014 Doug Hellmann.  All rights reserved.
"""Waiting for a future to be done"""

# end_pymotw_header
import asyncio


def mark_done(future, result):
    print("setting future result to {!r}".format(result))
    future.set_result(result)


event_loop = asyncio.get_event_loop()
try:
    all_done = asyncio.Future()

    print("scheduling mark_done")
    event_loop.call_soon(mark_done, all_done, "the result")

    print("entering event loop")
    result = event_loop.run_until_complete(all_done)
    print("returned result: {!r}".format(result))
finally:
    print("closing event loop")
    event_loop.close()

print("future result: {!r}".format(all_done.result()))

"""
$ python 08_asyncio_future_event_loop_01.py
/python3-standard-library-example/source/23_asyncio/08_asyncio_future_event_loop_01.py:16: DeprecationWarning: There is no current event loop
  event_loop = asyncio.get_event_loop()
scheduling mark_done
entering event loop
setting future result to 'the result'
returned result: 'the result'
closing event loop
future result: 'the result'
$
"""
