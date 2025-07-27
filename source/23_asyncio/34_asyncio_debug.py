#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2014 Doug Hellmann.  All rights reserved.
"""Enabling debugging"""

# end_pymotw_header
import argparse
import asyncio
import logging
import sys
import time
import warnings

parser = argparse.ArgumentParser("debugging asyncio")
parser.add_argument(
    "-v",
    dest="verbose",
    default=False,
    action="store_true",
)
args = parser.parse_args()

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)7s: %(message)s",
    stream=sys.stderr,
)
LOG = logging.getLogger("")


async def inner():
    LOG.info("inner starting")
    # Use a blocking sleep to simulate
    # doing work inside the function.
    time.sleep(0.1)
    LOG.info("inner completed")


async def outer(loop):
    LOG.info("outer starting")
    await asyncio.ensure_future(loop.create_task(inner()))
    LOG.info("outer completed")


event_loop = asyncio.get_event_loop()
if args.verbose:
    LOG.info("enabling debugging")

    # Enable debugging
    event_loop.set_debug(True)

    # Make the threshold for "slow" tasks very very small for
    # illustration. The default is 0.1, or 100 milliseconds.
    event_loop.slow_callback_duration = 0.001

    # Report all mistakes managing asynchronous resources.
    warnings.simplefilter("always", ResourceWarning)

LOG.info("entering event loop")
event_loop.run_until_complete(outer(event_loop))

"""
$ python 34_asyncio_debug.py
  DEBUG: Using selector: EpollSelector
   INFO: entering event loop
   INFO: outer starting
   INFO: inner starting
   INFO: inner completed
   INFO: outer completed


$ python 34_asyncio_debug.py -v
  DEBUG: Using selector: EpollSelector
   INFO: enabling debugging
   INFO: entering event loop
   INFO: outer starting
   INFO: inner starting
   INFO: inner completed
WARNING: Executing <Task finished name='Task-2' coro=<inner() done, defined at 34_asyncio_debug.py:33> result=None created at 34_asyncio_debug.py:43> took 0.104 seconds
   INFO: outer completed

"""
