#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2014 Doug Hellmann.  All rights reserved.
"""Using a queue"""

# end_pymotw_header
import asyncio


async def consumer(n, q):
    print("consumer {}: starting".format(n))
    while True:
        print("consumer {}: waiting for item".format(n))
        item = await q.get()
        print("consumer {}: has item {}".format(n, item))
        if item is None:
            # None is the signal to stop.
            q.task_done()
            break
        else:
            await asyncio.sleep(0.01 * item)
            q.task_done()
    print("consumer {}: ending".format(n))


async def producer(q, num_workers):
    print("producer: starting")
    # Add some numbers to the queue to simulate jobs
    for i in range(num_workers * 3):
        await q.put(i)
        print("producer: added task {} to the queue".format(i))
    # Add None entries in the queue
    # to signal the consumers to exit
    print("producer: adding stop signals to the queue")
    for i in range(num_workers):
        await q.put(None)
    print("producer: waiting for queue to empty")
    await q.join()
    print("producer: ending")


async def main(loop, num_consumers):
    # Create the queue with a fixed size so the producer
    # will block until the consumers pull some items out.
    q = asyncio.Queue(maxsize=num_consumers)

    # Scheduled the consumer tasks.
    consumers = [loop.create_task(consumer(i, q)) for i in range(num_consumers)]

    # Schedule the producer task.
    prod = loop.create_task(producer(q, num_consumers))

    # Wait for all of the coroutines to finish.
    await asyncio.wait(consumers + [prod])


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop, 2))
finally:
    event_loop.close()

"""
consumer 0: starting
consumer 0: waiting for item
consumer 1: starting
consumer 1: waiting for item
producer: starting
producer: added task 0 to the queue
producer: added task 1 to the queue
consumer 0: has item 0
consumer 1: has item 1
producer: added task 2 to the queue
producer: added task 3 to the queue
consumer 0: waiting for item
consumer 0: has item 2
producer: added task 4 to the queue
consumer 1: waiting for item
consumer 1: has item 3
producer: added task 5 to the queue
producer: adding stop signals to the queue
consumer 0: waiting for item
consumer 0: has item 4
consumer 1: waiting for item
consumer 1: has item 5
producer: waiting for queue to empty
consumer 0: waiting for item
consumer 0: has item None
consumer 0: ending
consumer 1: waiting for item
consumer 1: has item None
consumer 1: ending
producer: ending
"""

"""
consumer 0: starting
consumer 0: waiting for item
consumer 1: starting
consumer 1: waiting for item
producer: starting

producer: added task 0 to the queue
producer: added task 1 to the queue
producer: added task 2 to the queue
producer: added task 3 to the queue
producer: added task 4 to the queue
producer: added task 5 to the queue
producer: adding stop signals to the queue
producer: waiting for queue to empty
producer: ending

consumer 0: has item 0
consumer 0: waiting for item
consumer 0: has item 2
consumer 0: waiting for item
consumer 0: has item 4
consumer 0: waiting for item
consumer 0: has item None
consumer 0: ending

consumer 1: has item 1
consumer 1: waiting for item
consumer 1: has item 3
consumer 1: waiting for item
consumer 1: has item 5
consumer 1: waiting for item
consumer 1: has item None
consumer 1: ending

"""
