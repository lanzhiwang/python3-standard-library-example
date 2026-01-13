import asyncio


# 1. 使用类型提示增加代码严谨性
async def phase1() -> str:
    print("in phase1")
    # 模拟耗时 2s 的 IO 操作
    await asyncio.sleep(2)
    print("done with phase1")
    return "phase1 result"


async def phase2() -> str:
    print("in phase2")
    # 模拟耗时 1s 的 IO 操作
    await asyncio.sleep(1)
    print("done with phase2")
    return "phase2 result"


async def main():
    print("starting main")
    print("waiting for phases to complete")

    # 2. asyncio.gather 是并发执行任务并获取顺序结果的最佳方案
    # 它会自动将协程封装成 Task
    results = await asyncio.gather(
        phase1(),
        phase2(),
    )

    # 3. 使用 f-string 替代 .format(), !r 保持原样以输出 repr 格式
    print(f"results: {results!r}")


if __name__ == "__main__":
    # 4. 现代 Python 3.7+ 的标准启动方式
    # 它会自动处理创建 loop、运行 main 以及最后的关闭清理
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        # 优雅处理 Ctrl+C
        pass

"""
$ python 17_asyncio_gather_02.py
starting main
waiting for phases to complete
in phase1
in phase2
done with phase2
done with phase1
results: ['phase1 result', 'phase2 result']
$
"""
