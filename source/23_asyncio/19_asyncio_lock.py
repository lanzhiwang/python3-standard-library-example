#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2014 Doug Hellmann.  All rights reserved.
"""Using a lock primitive"""

# end_pymotw_header
import asyncio
import functools


def unlock(lock):
    print("callback releasing lock")
    lock.release()  # 释放锁


async def coro1(lock):
    print("coro1 waiting for the lock")
    async with lock:
        print("coro1 acquired lock")
    print("coro1 released lock")


async def coro2(lock):
    print("coro2 waiting for the lock")
    await lock.acquire()  # 获取锁
    try:
        print("coro2 acquired lock")
    finally:
        print("coro2 released lock")
        lock.release()


async def main(loop):
    # Create and acquire a shared lock.
    lock = asyncio.Lock()
    print("acquiring the lock before starting coroutines")
    await lock.acquire()  # 获取锁
    print("lock acquired: {}".format(lock.locked()))

    # Schedule a callback to unlock the lock.
    loop.call_later(0.1, functools.partial(unlock, lock))

    # Run the coroutines that want to use the lock.
    print("waiting for coroutines")
    await asyncio.wait([coro1(lock), coro2(lock)]),


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()

"""
acquiring the lock before starting coroutines
lock acquired: True
waiting for coroutines
coro2 waiting for the lock
coro1 waiting for the lock
callback releasing lock
coro2 acquired lock
coro2 released lock
coro1 acquired lock
coro1 released lock
"""
