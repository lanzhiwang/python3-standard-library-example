#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2014 Doug Hellmann.  All rights reserved.
"""Starting a task
"""

#end_pymotw_header
import asyncio


async def task_func():
    print('in task_func')
    return 'the result'


async def main(loop):
    print('creating task')
    task = loop.create_task(task_func())
    print('waiting for {!r}'.format(task))
    return_value = await task
    print('task completed {!r}'.format(task))
    print('return value: {!r}'.format(return_value))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()

"""
creating task
waiting for <Task pending name='Task-2' coro=<task_func() running at 11_asyncio_create_task.py:12>>
in task_func
task completed <Task finished name='Task-2' coro=<task_func() done, defined at 11_asyncio_create_task.py:12> result='the result'>
return value: 'the result'
"""