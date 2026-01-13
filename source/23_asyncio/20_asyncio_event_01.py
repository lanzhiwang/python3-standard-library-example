#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2014 Doug Hellmann.  All rights reserved.
"""Using an event primitive"""

# end_pymotw_header
import asyncio
import functools


def set_event(event):
    print("setting event in callback")
    event.set()


async def coro1(event):
    print("coro1 waiting for event")
    await event.wait()
    print("coro1 triggered")


async def coro2(event):
    print("coro2 waiting for event")
    await event.wait()
    print("coro2 triggered")


async def main(loop):
    # Create a shared event
    event = asyncio.Event()
    print("event start state: {}".format(event.is_set()))

    loop.call_later(0.1, functools.partial(set_event, event))

    await asyncio.wait([coro1(event), coro2(event)])
    print("event end state: {}".format(event.is_set()))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()

"""
$ python 20_asyncio_event_01.py
/python3-standard-library-example/source/23_asyncio/20_asyncio_event_01.py:40: DeprecationWarning: There is no current event loop
  event_loop = asyncio.get_event_loop()
event start state: False
Traceback (most recent call last):
  File "/python3-standard-library-example/source/23_asyncio/20_asyncio_event_01.py", line 42, in <module>
    event_loop.run_until_complete(main(event_loop))
  File "/usr/local/lib/python3.12/asyncio/base_events.py", line 684, in run_until_complete
    return future.result()
           ^^^^^^^^^^^^^^^
  File "/python3-standard-library-example/source/23_asyncio/20_asyncio_event_01.py", line 36, in main
    await asyncio.wait([coro1(event), coro2(event)])
  File "/usr/local/lib/python3.12/asyncio/tasks.py", line 461, in wait
    raise TypeError("Passing coroutines is forbidden, use tasks explicitly.")
TypeError: Passing coroutines is forbidden, use tasks explicitly.
sys:1: RuntimeWarning: coroutine 'coro2' was never awaited
sys:1: RuntimeWarning: coroutine 'coro1' was never awaited
$
"""
