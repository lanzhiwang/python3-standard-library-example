#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2014 Doug Hellmann.  All rights reserved.
"""Returning a value from a coroutine"""

# end_pymotw_header
import asyncio


async def coroutine():
    print("in coroutine")
    return "result"


event_loop = asyncio.get_event_loop()
try:
    return_value = event_loop.run_until_complete(coroutine())
    print("it returned: {!r}".format(return_value))
finally:
    event_loop.close()

"""
$ python 02_asyncio_coroutine_return_01.py
/python3-standard-library-example/source/23_asyncio/02_asyncio_coroutine_return_01.py:16: DeprecationWarning: There is no current event loop
  event_loop = asyncio.get_event_loop()
in coroutine
it returned: 'result'
$
"""
