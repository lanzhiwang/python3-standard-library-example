#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2014 Doug Hellmann.  All rights reserved.
"""Starting a coroutine
"""

#end_pymotw_header
import asyncio


async def coroutine():
    print('in coroutine')


event_loop = asyncio.get_event_loop()
try:
    print('starting coroutine')
    coro = coroutine()
    print(coro)
    print('entering event loop')
    event_loop.run_until_complete(coro)
finally:
    print('closing event loop')
    event_loop.close()

"""
starting coroutine
<coroutine object coroutine at 0x7f7632ac8d40>
entering event loop
in coroutine
closing event loop
"""