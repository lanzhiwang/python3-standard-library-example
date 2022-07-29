#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2014 Doug Hellmann.  All rights reserved.
"""Running a blocking function in a process pool
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


# changes from asyncio_executor_thread.py

if __name__ == '__main__':
    # Configure logging to show the id of the process
    # where the log message originates.
    logging.basicConfig(
        level=logging.INFO,
        format='PID %(process)5s %(name)18s: %(message)s',
        stream=sys.stderr,
    )

    # Create a limited process pool.
    executor = concurrent.futures.ProcessPoolExecutor(
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
PID    40 run_blocking_tasks: starting
PID    40 run_blocking_tasks: creating executor tasks
PID    40 run_blocking_tasks: waiting for executor tasks
PID    41          blocks(0): running
PID    42          blocks(1): running
PID    43          blocks(2): running
PID    41          blocks(0): done
PID    43          blocks(2): done
PID    42          blocks(1): done
PID    41          blocks(3): running
PID    43          blocks(4): running
PID    42          blocks(5): running
PID    43          blocks(4): done
PID    41          blocks(3): done
PID    42          blocks(5): done
PID    40 run_blocking_tasks: results: [9, 1, 16, 4, 25, 0]
PID    40 run_blocking_tasks: exiting
"""