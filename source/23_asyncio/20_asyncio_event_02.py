import asyncio
import functools


# 1. 使用类型提示 (Type Hints) 增加代码健壮性
def set_event(event: asyncio.Event):
    """同步回调函数, 用于触发事件"""
    print("setting event in callback")
    # set() 是同步方法, 可以直接调用
    event.set()


async def coro1(event: asyncio.Event):
    print("coro1 waiting for event")
    # wait() 会挂起协程, 直到 event.set() 被调用
    await event.wait()
    print("coro1 triggered")


async def coro2(event: asyncio.Event):
    print("coro2 waiting for event")
    await event.wait()
    print("coro2 triggered")


async def main():
    """主协程: 负责逻辑编排"""
    # 2. 在协程内部创建 Event, 确保它绑定到当前运行的 loop
    event = asyncio.Event()
    print(f"event start state: {event.is_set()}")

    # 3. 获取当前运行的 loop 以调度延迟任务
    # 现代做法: 不再从外部传递 loop, 而是在需要时动态获取
    loop = asyncio.get_running_loop()
    loop.call_later(0.1, functools.partial(set_event, event))

    # 4. 现代并发等待: 推荐使用 asyncio.gather
    # gather 会自动将协程包装为 Task 并并发运行
    print("waiting for coroutines to be triggered...")
    await asyncio.gather(coro1(event), coro2(event))

    print(f"event end state: {event.is_set()}")


if __name__ == "__main__":
    # 5. 使用现代标准入口 asyncio.run
    # 它会自动处理创建 loop、运行 main 以及最后的优雅关闭
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass

"""
在现代 Python (3.10+) 中, 改写的重点在于移除过时的显式 loop 传递, 并修正 asyncio.wait 对协程对象的直接使用.

高级工程师的深度解析:

解耦事件循环 (Loop Decoupling):
旧写法: main(loop) 需要调用者显式传入 event_loop. 这在大型框架中会导致参数传递非常混乱.
新写法: 使用 asyncio.get_running_loop(). 这体现了基础设施即环境的思想, 只有在真正需要与底层低级 API(如 call_later)交互时才获取 loop.

asyncio.gather vs asyncio.wait:
你原来的代码使用的是 asyncio.wait([coro1(), coro2()]). 在 Python 3.8+ 中, 直接向 wait 传递协程对象会触发 DeprecationWarning.
对于这种"等待所有任务完成且不关心细粒度控制"的情景, 使用 asyncio.gather 是最优雅的方案. 它更简洁, 且会自动处理协程到任务(Task)的转换.

Event 的线程安全与上下文:
asyncio.Event 并不是线程安全的(Thread-safe), 它仅设计用于同一个事件循环中的协程间同步.
由于 event.set() 是同步方法, 它非常适合在 call_later 或 add_done_callback 这种传统的基于回调的 API 中使用, 作为异步和同步逻辑的桥梁.

f-string 与 类型注解:
使用了 f-string 替代 .format(), 这在 Python 工程实践中已是标准, 性能更好且更易读.
添加了 asyncio.Event 的类型提示, 这对大型项目中的静态代码分析和 IDE 自动补全非常有帮助.

资源生命周期管理:
asyncio.run() 解决了之前代码中容易被忽略的 loop.close() 问题. 它会确保在主程序退出前, 所有的异步生成器被关闭, 并且如果此时还有未完成的任务, 它会打印相关的警告信息, 帮助开发者排查资源泄漏.

总结
这段改写后的代码符合 Python 3.10+ 的异步编程规范: 逻辑内聚、避免弃用警告、且利用了最高层的抽象 API. 在实际开发中, Event 常用于实现"启动信号"或"优雅停机"的广播通知.

$ python 20_asyncio_event_02.py
event start state: False
waiting for coroutines to be triggered...
coro1 waiting for event
coro2 waiting for event
setting event in callback
coro1 triggered
coro2 triggered
event end state: True
$

"""
