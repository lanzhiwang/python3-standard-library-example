import asyncio
import time


def callback(n: int):
    """
    回调函数: 现在通过内部获取循环来读取时间, 减少参数传递
    """
    # 在回调执行时获取当前运行的循环以读取其内部时间
    loop = asyncio.get_running_loop()
    print(f"callback {n} invoked at {loop.time():.4f}")


async def main():
    """
    主协程: 演示基于绝对循环时间的调度
    """
    # 1. 获取当前运行的事件循环
    loop = asyncio.get_running_loop()

    # 2. 对比系统时间与循环内部时间
    # loop.time() 通常基于系统的单调时钟, 不受系统时间调整(如闰秒、手动调表)影响
    now = loop.time()
    print(f"clock time: {time.time():.4f}")
    print(f"loop  time: {now:.4f}")

    print("registering callbacks")

    # 3. 使用 call_at 进行绝对时间调度
    # 注意: call_at 接收的是 loop.time() 的绝对值
    loop.call_at(now + 0.2, callback, 1)
    loop.call_at(now + 0.1, callback, 2)

    # 4. 使用 call_soon 尽快执行
    loop.call_soon(callback, 3)

    # 等待足够长的时间以确保所有回调执行完毕
    await asyncio.sleep(1)


if __name__ == "__main__":
    # 5. 使用现代化的单入口, 自动处理循环生命周期
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass

"""
在 asyncio 中, loop.call_at() 使用的是事件循环内部的单调时钟(Monotonic Clock), 这与系统时间 time.time() 是不同的.

高级工程师的深度解析:

loop.time() 的重要性:
time.time() 返回的是 Unix 时间戳(可被修改, 不连续).
loop.time() 返回的是事件循环的内部时间(单调递增, 不可回退).

改进点: 在 callback 内部直接调用 asyncio.get_running_loop().time(), 这样就不需要把 loop 对象像传家宝一样在参数里传向每一个函数.

call_at 的调度逻辑:
call_later(delay, ...) 是相对时间调度.
call_at(when, ...) 是绝对时间调度.
在高级开发中, 如果你需要精确对齐多个异步任务的启动时间点, call_at 配合 loop.time() 是最可靠的方案.

移除 main(loop) 参数:
旧习惯: 手动获取 event_loop 并传给 main.
新标准: asyncio.run(main()) 启动后, 在 main 内部通过 asyncio.get_running_loop() 获取引用. 这符合"依赖查找"而非"依赖注入"的简洁风格.

格式化打印的优化:
使用了 :.4f 格式化浮点数, 这在处理时间戳时能让输出对齐, 更容易观察到 0.1s 和 0.2s 的延迟间隔.

继续使用 f-strings 提高可读性.

资源管理(RAII 思想):
asyncio.run() 封装了 try...finally: loop.close(). 在高级工程实践中, 手动关闭循环是非常危险的(可能导致正在运行的后台任务报错), 使用官方推荐的 run() 能确保异步生成器和执行器被正确关闭.

总结
这段代码演示了 asyncio 最底层的调度机制. 虽然现代开发更多使用 asyncio.create_task 或 asyncio.gather, 但在需要极低开销或精确时间控制的场景下(如高性能定时器或协议实现), call_at 依然是不可替代的工具. 改写后的代码在保持功能不变的同时, 完全符合 Python 3.10+ 的 API 规范.

$ python 07_asyncio_call_at_02.py
clock time: 1768287470.4445
loop  time: 5071.9472
registering callbacks
callback 3 invoked at 5071.9473
callback 2 invoked at 5072.0493
callback 1 invoked at 5072.1509
$

"""
