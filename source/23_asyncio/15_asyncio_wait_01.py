#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2014 Doug Hellmann.  All rights reserved.
"""Waiting for multiple coroutines"""

# end_pymotw_header
import asyncio


async def phase(i):
    print("in phase {}".format(i))
    await asyncio.sleep(0.1 * i)
    print("done with phase {}".format(i))
    return "phase {} result".format(i)


async def main(num_phases):
    print("starting main")
    phases = [phase(i) for i in range(num_phases)]
    print("waiting for phases to complete")
    completed, pending = await asyncio.wait(phases)
    results = [t.result() for t in completed]
    print("results: {!r}".format(results))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(3))
finally:
    event_loop.close()

"""
$ python 15_asyncio_wait_01.py
/python3-standard-library-example/source/23_asyncio/15_asyncio_wait_01.py:27: DeprecationWarning: There is no current event loop
  event_loop = asyncio.get_event_loop()
starting main
waiting for phases to complete
Traceback (most recent call last):
  File "/python3-standard-library-example/source/23_asyncio/15_asyncio_wait_01.py", line 29, in <module>
    event_loop.run_until_complete(main(3))
  File "/usr/local/lib/python3.12/asyncio/base_events.py", line 684, in run_until_complete
    return future.result()
           ^^^^^^^^^^^^^^^
  File "/python3-standard-library-example/source/23_asyncio/15_asyncio_wait_01.py", line 22, in main
    completed, pending = await asyncio.wait(phases)
                         ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/asyncio/tasks.py", line 461, in wait
    raise TypeError("Passing coroutines is forbidden, use tasks explicitly.")
TypeError: Passing coroutines is forbidden, use tasks explicitly.
sys:1: RuntimeWarning: coroutine 'phase' was never awaited
$

作为高级 Python 开发工程师, 这段代码改写的重点在于解决一个非常关键的弃用:
在现代 asyncio 中, 不能直接将协程对象(Coroutines)列表传给 asyncio.wait(), 必须先将它们封装为任务(Tasks).
此外, 我还会向你展示在 Python 3.11+ 中处理此类需求的"黄金标准" - TaskGroup.

"""
