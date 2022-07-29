#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2014 Doug Hellmann.  All rights reserved.
"""Running a blocking function in a thread pool
"""

#end_pymotw_header
import asyncio
import concurrent.futures
import logging
import sys
import time


def blocks(n):
    log = logging.getLogger('blocks({})'.format(n))
    log.info('running')
    time.sleep(0.1)
    log.info('done')
    return n ** 2


async def run_blocking_tasks(executor):
    log = logging.getLogger('run_blocking_tasks')
    log.info('starting')

    log.info('creating executor tasks')
    loop = asyncio.get_event_loop()
    blocking_tasks = [
        loop.run_in_executor(executor, blocks, i)
        for i in range(6)
    ]
    log.info('waiting for executor tasks')
    completed, pending = await asyncio.wait(blocking_tasks)
    results = [t.result() for t in completed]
    log.info('results: {!r}'.format(results))

    log.info('exiting')


if __name__ == '__main__':
    # Configure logging to show the name of the thread
    # where the log message originates.
    logging.basicConfig(
        level=logging.INFO,
        format='%(threadName)10s %(name)18s: %(message)s',
        stream=sys.stderr,
    )

    # Create a limited thread pool.
    executor = concurrent.futures.ThreadPoolExecutor(
        max_workers=3,
    )

    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(
            run_blocking_tasks(executor)
        )
    finally:
        event_loop.close()

"""
MainThread run_blocking_tasks: starting
MainThread run_blocking_tasks: creating executor tasks
ThreadPoolExecutor-0_0          blocks(0): running
ThreadPoolExecutor-0_1          blocks(1): running
ThreadPoolExecutor-0_2          blocks(2): running
MainThread run_blocking_tasks: waiting for executor tasks
ThreadPoolExecutor-0_1          blocks(1): done
ThreadPoolExecutor-0_1          blocks(3): running
ThreadPoolExecutor-0_2          blocks(2): done
ThreadPoolExecutor-0_2          blocks(4): running
ThreadPoolExecutor-0_0          blocks(0): done
ThreadPoolExecutor-0_0          blocks(5): running
ThreadPoolExecutor-0_1          blocks(3): done
ThreadPoolExecutor-0_2          blocks(4): done
ThreadPoolExecutor-0_0          blocks(5): done
MainThread run_blocking_tasks: results: [9, 0, 16, 1, 25, 4]
MainThread run_blocking_tasks: exiting
"""