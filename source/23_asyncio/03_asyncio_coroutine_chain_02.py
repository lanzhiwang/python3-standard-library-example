import asyncio


async def phase1():
    print("in phase1")
    await asyncio.sleep(0.1)  # 模拟 IO 操作
    return "result1"


async def phase2(arg):
    print("in phase2")
    await asyncio.sleep(0.1)  # 模拟 IO 操作
    return f"result2 derived from {arg}"


async def outer():
    """
    作为异步逻辑的主体, 负责编排子协程
    """
    print("in outer")

    print("waiting for result1")
    # 显式使用 await 等待协程结果
    result1 = await phase1()

    print("waiting for result2")
    # 依赖上一步结果的协程
    result2 = await phase2(result1)

    return (result1, result2)


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
$ python 03_asyncio_coroutine_chain_02.py
in outer
waiting for result1
in phase1
waiting for result2
in phase2
return value: ('result1', 'result2 derived from result1')
$
"""
