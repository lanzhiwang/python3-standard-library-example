#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2014 Doug Hellmann.  All rights reserved.
"""Waiting for multiple coroutines, with a timeout"""

# end_pymotw_header
import asyncio


async def phase(i):
    print("in phase {}".format(i))
    try:
        await asyncio.sleep(0.1 * i)
    except asyncio.CancelledError:
        print("phase {} canceled".format(i))
        raise
    else:
        print("done with phase {}".format(i))
        return "phase {} result".format(i)


async def main(num_phases):
    print("starting main")
    phases = [phase(i) for i in range(num_phases)]
    print("waiting 0.1 for phases to complete")
    completed, pending = await asyncio.wait(phases, timeout=0.1)
    print(
        "{} completed and {} pending".format(
            len(completed),
            len(pending),
        )
    )
    # Cancel remaining tasks so they do not generate errors
    # as we exit without finishing them.
    if pending:
        print("canceling tasks")
        for t in pending:
            t.cancel()
    print("exiting main")


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(3))
finally:
    event_loop.close()

"""
$ python 16_asyncio_wait_timeout_01.py
/python3-standard-library-example/source/23_asyncio/16_asyncio_wait_timeout_01.py:43: DeprecationWarning: There is no current event loop
  event_loop = asyncio.get_event_loop()
starting main
waiting 0.1 for phases to complete
Traceback (most recent call last):
  File "/python3-standard-library-example/source/23_asyncio/16_asyncio_wait_timeout_01.py", line 45, in <module>
    event_loop.run_until_complete(main(3))
  File "/usr/local/lib/python3.12/asyncio/base_events.py", line 684, in run_until_complete
    return future.result()
           ^^^^^^^^^^^^^^^
  File "/python3-standard-library-example/source/23_asyncio/16_asyncio_wait_timeout_01.py", line 27, in main
    completed, pending = await asyncio.wait(phases, timeout=0.1)
                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/asyncio/tasks.py", line 461, in wait
    raise TypeError("Passing coroutines is forbidden, use tasks explicitly.")
TypeError: Passing coroutines is forbidden, use tasks explicitly.
sys:1: RuntimeWarning: coroutine 'phase' was never awaited
$
"""
