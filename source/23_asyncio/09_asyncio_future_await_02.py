import asyncio


# 1. 使用类型注解增强代码可读性
def mark_done(future: asyncio.Future, result: str):
    """
    同步回调: 为 Future 对象设置结果.
    """
    print(f"setting future result to {result!r}")
    if not future.done():
        future.set_result(result)


async def main():
    """
    主协程: 演示 Future 的异步等待.
    """
    # 2. 在协程内部通过 get_running_loop 获取当前循环
    # 这避免了将 loop 作为参数从外部层层传递
    loop = asyncio.get_running_loop()

    # 3. 推荐使用 loop.create_future()
    # 这比直接实例化 asyncio.Future() 更符合框架设计规范
    all_done = loop.create_future()

    print("scheduling mark_done")
    # 4. 安排回调执行
    loop.call_soon(mark_done, all_done, "the result")

    # 5. 直接使用 await 等待 Future 完成
    result = await all_done
    print(f"returned result: {result!r}")


if __name__ == "__main__":
    # 6. 统一使用 asyncio.run()
    # 它会自动处理事件循环的创建、运行和最后的优雅关闭
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass

"""
$ python 09_asyncio_future_await_02.py
scheduling mark_done
setting future result to 'the result'
returned result: 'the result'
$
"""
