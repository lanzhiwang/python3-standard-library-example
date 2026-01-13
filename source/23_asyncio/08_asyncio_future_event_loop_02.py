import asyncio


def mark_done(future: asyncio.Future, result: str):
    """
    同步回调函数: 为 Future 设置结果
    """
    print(f"setting future result to {result!r}")
    # 当 set_result 被调用时, 所有 await 该 future 的地方都会被唤醒
    if not future.done():
        future.set_result(result)


async def main():
    """
    主协程: 演示 Future 的生命周期
    """
    # 1. 获取当前运行的事件循环
    loop = asyncio.get_running_loop()

    # 2. 创建一个 Future 对象
    # 推荐使用 loop.create_future(), 这是更符合工业标准的做法
    all_done = loop.create_future()

    print("scheduling mark_done")
    # 3. 安排在稍后执行回调
    loop.call_soon(mark_done, all_done, "the result")

    print("entering await (waiting for future)")
    # 4. 使用 await 直接等待 Future 完成, 取代 run_until_complete
    result = await all_done

    print(f"returned result: {result!r}")
    return all_done


if __name__ == "__main__":
    # 5. 使用 asyncio.run 开启现代异步入口
    # 它会处理循环的创建、运行和最后的清理
    try:
        final_future = asyncio.run(main())
        # 6. 验证 Future 的最终状态
        print(f"future result: {final_future.result()!r}")
    except KeyboardInterrupt:
        pass

"""
在现代 asyncio 中, 我们不再手动管理循环的启动和关闭, 而是利用 await 来等待 Future 的完成.
此外, 推荐使用 loop.create_future() 而不是直接实例化 asyncio.Future(), 以确保 Future 与当前运行的循环正确绑定.

高级工程师的深度解析:

loop.create_future() vs asyncio.Future():
虽然两者在大多数场景下效果相同, 但 loop.create_future() 是官方推荐的工厂方法. 它能确保生成的 Future 对象使用的是特定的事件循环实现(例如在某些三方库中使用自定义 loop 时非常重要).

await 替代 run_until_complete:
在旧代码中, 你必须通过 event_loop.run_until_complete(all_done) 来阻塞主线程直到 Future 完成.
在现代异步架构中, 整个程序运行在 asyncio.run 开启的上下文中, 你只需要简单的 await all_done 即可. 这让异步逻辑可以像同步逻辑一样线性书写.

Future 的状态管理:
在 mark_done 函数中, 我增加了一个 if not future.done(): 的判断.
在复杂的异步环境下, 这是一个防御性编程的好习惯, 防止因为多次设置结果而抛出 InvalidStateError.

解耦入口与逻辑:
原代码在全局作用域编写逻辑. 改写后, 逻辑被封装在 main() 协程中. 这种封装使得代码更易于测试(Unit Testing)和复用.

关于 asyncio.run() 的清理行为:
asyncio.run() 会在返回前关闭事件循环.
你在原代码最后打印了 all_done.result(). 在改写版中, 我通过 main() 返回了该 Future 对象. 由于 Future 的结果在循环关闭后依然存储在对象内存中, 所以我们在 asyncio.run() 之后依然可以安全地通过 .result() 读取它.

总结
现代 asyncio 的核心是 "由 await 驱动任务流, 由 asyncio.run 驱动生命周期". 手动操作 event_loop 对象的场景在业务开发中已经非常罕见, 只有在编写复杂的底层库或中间件时才会用到.

$ python 08_asyncio_future_event_loop_02.py
scheduling mark_done
entering await (waiting for future)
setting future result to 'the result'
returned result: 'the result'
future result: 'the result'
$

"""
