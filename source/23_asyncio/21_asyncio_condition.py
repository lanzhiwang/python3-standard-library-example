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
starting manipulate_condition
consumer 4 is waiting
consumer 0 is waiting
consumer 3 is waiting
consumer 2 is waiting
consumer 1 is waiting

notifying 1 consumers
consumer 4 triggered
ending consumer 4

notifying 2 consumers
consumer 0 triggered
ending consumer 0

consumer 3 triggered
ending consumer 3
notifying remaining consumers
ending manipulate_condition
consumer 2 triggered
ending consumer 2
consumer 1 triggered
ending consumer 1
"""
