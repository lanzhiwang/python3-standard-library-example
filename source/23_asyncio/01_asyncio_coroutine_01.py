#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2014 Doug Hellmann.  All rights reserved.
"""Starting a coroutine"""

# end_pymotw_header
import asyncio


async def coroutine():
    print("in coroutine")


event_loop = asyncio.get_event_loop()
try:
    print("starting coroutine")
    coro = coroutine()
    print(coro)
    print("entering event loop")
    event_loop.run_until_complete(coro)
finally:
    print("closing event loop")
    event_loop.close()

"""
你好! 作为一名高级开发工程师, 我非常理解你在升级或编写 asyncio 代码时遇到的这个困惑.

这个 DeprecationWarning(弃用警告)是 Python 3.10 及之后版本中非常常见的一个变化. 下面我为你详细分析其原因并提供最佳实践的修改方案.

1. 警告的原因是什么?

在早期的 Python 版本中, asyncio.get_event_loop() 的行为比较"隐式": 如果你在主线程中调用它且当前没有运行中的事件循环, 它会自动创建一个新的循环并将其设置为当前循环.

这种机制带来了几个问题:

不确定性: 在多线程环境中, 这种隐式创建往往会导致难以察觉的 Bug.
资源管理: 开发者往往忘记手动关闭(loop.close())隐式创建的循环.
架构演进: Python 官方希望推动开发者使用更高级、更简洁的 API(如 asyncio.run()), 而不是手动去管理复杂的底层循环对象.

从 Python 3.10 开始, 如果在没有运行中的事件循环时调用 get_event_loop(), Python 就会抛出这个警告, 提醒你这种隐式创建循环的行为即将被废弃.

$ python --version
Python 3.12.1

$ python 01_asyncio_coroutine_01.py
/python3-standard-library-example/source/23_asyncio/01_asyncio_coroutine_01.py:15: DeprecationWarning: There is no current event loop
  event_loop = asyncio.get_event_loop()
starting coroutine
<coroutine object coroutine at 0x7fae62a5cd00>
entering event loop
in coroutine
closing event loop
$

$ python --version
Python 3.10.18

$ python 01_asyncio_coroutine_01.py
starting coroutine
<coroutine object coroutine at 0x7f236eb2e650>
entering event loop
in coroutine
closing event loop
$
"""
