#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2014 Doug Hellmann.  All rights reserved.
"""Starting a task, then canceling it"""

# end_pymotw_header
import asyncio


async def task_func():
    print("in task_func")
    return "the result"


async def main(loop):
    print("creating task")
    task = loop.create_task(task_func())

    print("canceling task")
    task.cancel()

    print("canceled task {!r}".format(task))
    try:
        await task
    except asyncio.CancelledError:
        print("caught error from canceled task")
    else:
        print("task result: {!r}".format(task.result()))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()

"""
$ python 12_asyncio_cancel_task_01.py
/python3-standard-library-example/source/23_asyncio/12_asyncio_cancel_task_01.py:32: DeprecationWarning: There is no current event loop
  event_loop = asyncio.get_event_loop()
creating task
canceling task
canceled task <Task cancelling name='Task-2' coro=<task_func() running at /python3-standard-library-example/source/23_asyncio/12_asyncio_cancel_task_01.py:11>>
caught error from canceled task
$
"""
