#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2014 Doug Hellmann.  All rights reserved.
"""Scheduling a callback with call_soon"""

# end_pymotw_header
import asyncio
import functools


# 建议使用类型注解增强代码健壮性
def callback(arg: int, *, kwarg: str = "default"):
    """普通同步回调函数"""
    print(f"callback invoked with {arg} and {kwarg}")


async def main():
    """
    主协程: 演示如何注册回调
    """
    # 1. 获取当前正在运行的事件循环, 无需显式从外部传入
    loop = asyncio.get_running_loop()

    print("registering callbacks")

    # 2. call_soon 的基本用法: 注册后在下一次循环迭代中执行
    loop.call_soon(callback, 1)

    # 3. 使用 functools.partial 包装带关键字参数的回调
    wrapped = functools.partial(callback, kwarg="not default")
    loop.call_soon(wrapped, 2)

    # 4. 必须 await 某些东西(如 sleep), 控制权才会回到事件循环,
    # 从而让上面注册的 call_soon 回调有机会执行.
    await asyncio.sleep(0.1)


if __name__ == "__main__":
    # 5. 使用现代化的单入口启动方式
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass

"""
在早期的 asyncio 代码中, 开发者习惯于四处传递 loop 对象.
在现代 Python 中, 我们通过 asyncio.get_running_loop() 在需要的地方动态获取当前运行的循环, 或者直接使用高层 API.

高级工程师的改进深度解析:

消除 loop 参数传递:
旧代码: async def main(loop): .... 这种做法会让函数签名变得臃肿, 且在大型项目中很难追踪 loop 的来源.
现代做法: loop = asyncio.get_running_loop(). 这个函数专门用于在协程内部安全地获取当前循环. 如果当前没有循环在运行, 它会直接抛出错误, 这比 get_event_loop() 的隐式创建行为要安全得多.

统一的入口: asyncio.run():
它取代了 get_event_loop -> run_until_complete -> close 的繁琐三部曲.
重要细节: asyncio.run() 每次调用都会创建一个全新的事件循环, 并在完成后彻底关闭它. 这保证了测试环境的隔离性, 避免了全局状态干扰.

回调函数的执行时机:
loop.call_soon 注册的函数并不会立即执行, 而是被放进一个 FIFO(先进先出)队列.
在 main 协程中执行 await asyncio.sleep(0.1) 时, main 挂起, 事件循环开始处理队列中的任务, 此时 callback 才会被调用.

字符串格式化:
继续推崇使用 f-strings (f"..."), 在处理日志输出和打印时更直观.

关于 functools.partial:
你的原代码中使用了 partial, 这在处理回调时非常专业.
小贴士: 其实 loop.call_soon(callback, 1) 内部也支持传参, 但如果是复杂的关键字参数(kwargs), partial 依然是目前最优雅、最 Pythonic 的处理方式.

什么时候还需要显式用到 loop?
只有当你编写非常底层的网络协议(如自定义 Protocol 或 Transport)或者需要与非异步库(通过 run_in_executor)进行深度整合时, 才需要频繁操作 loop 对象. 对于 95% 的业务开发, asyncio.run() 加 get_running_loop() 就是黄金标准.

$ python 05_asyncio_call_soon_02.py
registering callbacks
callback invoked with 1 and default
callback invoked with 2 and not default
$

"""
