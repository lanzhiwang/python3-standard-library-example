import asyncio


async def phase1():
    print("in phase1")
    await asyncio.sleep(0.1)  # 模拟 IO 操作
    return "result1"


async def phase2():
    print("in phase2")
    await asyncio.sleep(0.1)  # 模拟 IO 操作
    return f"result2"


async def outer():
    """
    作为异步逻辑的主体, 负责编排子协程
    """
    print("in outer")

    # 同时启动两个任务
    # 如果 phase1 和 phase2 是独立的, 应该这样写以提高效率:
    results = await asyncio.gather(phase1(), phase2())
    return results


async def main():
    """
    程序的总入口, 处理最高层级的逻辑
    """
    try:
        # asyncio.run 只能在最外层调用一次
        return_value = await outer()
        print(f"return value: {return_value!r}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # 使用 Python 3.7+ 推荐的最高层入口
    asyncio.run(main())

"""
$ python 03_asyncio_coroutine_chain_03.py
in outer
in phase1
in phase2
return value: ['result1', 'result2']
$
"""
