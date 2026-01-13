#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2014 Doug Hellmann.  All rights reserved.
"""Using a condition primitive"""

# end_pymotw_header
import asyncio


async def consumer(condition, n):
    async with condition:
        print("consumer {} is waiting".format(n))
        await condition.wait()
        print("consumer {} triggered".format(n))
    print("ending consumer {}".format(n))


async def manipulate_condition(condition):
    print("starting manipulate_condition")

    # pause to let consumers start
    await asyncio.sleep(0.1)

    for i in range(1, 3):
        async with condition:
            print("notifying {} consumers".format(i))
            condition.notify(n=i)
        await asyncio.sleep(0.1)

    async with condition:
        print("notifying remaining consumers")
        condition.notify_all()

    print("ending manipulate_condition")


async def main(loop):
    # Create a condition
    condition = asyncio.Condition()

    # Set up tasks watching the condition
    consumers = [consumer(condition, i) for i in range(5)]

    # Schedule a task to manipulate the condition variable
    loop.create_task(manipulate_condition(condition))

    # Wait for the consumers to be done
    await asyncio.wait(consumers)


event_loop = asyncio.get_event_loop()
try:
    result = event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()

"""
$ python 21_asyncio_condition_01.py
/python3-standard-library-example/source/23_asyncio/21_asyncio_condition_01.py:52: DeprecationWarning: There is no current event loop
  event_loop = asyncio.get_event_loop()
starting manipulate_condition
Traceback (most recent call last):
  File "/python3-standard-library-example/source/23_asyncio/21_asyncio_condition_01.py", line 54, in <module>
    result = event_loop.run_until_complete(main(event_loop))
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/asyncio/base_events.py", line 684, in run_until_complete
    return future.result()
           ^^^^^^^^^^^^^^^
  File "/python3-standard-library-example/source/23_asyncio/21_asyncio_condition_01.py", line 49, in main
    await asyncio.wait(consumers)
  File "/usr/local/lib/python3.12/asyncio/tasks.py", line 461, in wait
    raise TypeError("Passing coroutines is forbidden, use tasks explicitly.")
TypeError: Passing coroutines is forbidden, use tasks explicitly.
Task was destroyed but it is pending!
task: <Task pending name='Task-2' coro=<manipulate_condition() done, defined at /python3-standard-library-example/source/23_asyncio/21_asyncio_condition_01.py:19> wait_for=<Future pending cb=[Task.task_wakeup()]>>
sys:1: RuntimeWarning: coroutine 'consumer' was never awaited
$
"""
