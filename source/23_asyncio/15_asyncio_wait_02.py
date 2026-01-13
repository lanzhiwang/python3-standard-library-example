import asyncio


async def phase(i: int) -> str:
    print(f"in phase {i}")
    await asyncio.sleep(0.1 * i)
    print(f"done with phase {i}")
    return f"phase {i} result"


async def main(num_phases: int):
    print("starting main")

    # 1. 关键改进: 必须将协程显式转换为 Task
    # 直接传递协程列表给 asyncio.wait() 在新版本中会报 DeprecationWarning 或 TypeError
    tasks = [asyncio.create_task(phase(i)) for i in range(num_phases)]

    print("waiting for phases to complete")

    # 2. asyncio.wait 返回的是 (done, pending) 两个集合
    # 注意: done 集合中的顺序是随机的, 不保证与 tasks 列表顺序一致
    completed, pending = await asyncio.wait(tasks)

    # 3. 按照原始 tasks 列表的顺序提取结果(高级技巧)
    # 这样可以保证 results 的顺序是 [phase 0, phase 1, ...]
    results = [t.result() for t in tasks]

    print(f"results: {results!r}")


if __name__ == "__main__":
    # 4. 使用现代入口函数
    try:
        asyncio.run(main(3))
    except KeyboardInterrupt:
        pass

"""
$ python 15_asyncio_wait_02.py
starting main
waiting for phases to complete
in phase 0
in phase 1
in phase 2
done with phase 0
done with phase 1
done with phase 2
results: ['phase 0 result', 'phase 1 result', 'phase 2 result']
$
"""
