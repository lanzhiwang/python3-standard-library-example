import asyncio


async def phase(i: int) -> str:
    print(f"in phase {i}")
    await asyncio.sleep(0.1 * i)
    print(f"done with phase {i}")
    return f"phase {i} result"


async def main(num_phases: int):
    print("starting main")
    # 直接并发运行并获取有序结果
    # gather 会自动处理协程到任务的转换
    results = await asyncio.gather(*(phase(i) for i in range(num_phases)))
    print(f"results: {results!r}")


if __name__ == "__main__":
    # 4. 使用现代入口函数
    try:
        asyncio.run(main(3))
    except KeyboardInterrupt:
        pass

"""
$ python 15_asyncio_wait_03.py
starting main
in phase 0
in phase 1
in phase 2
done with phase 0
done with phase 1
done with phase 2
results: ['phase 0 result', 'phase 1 result', 'phase 2 result']
$
"""
