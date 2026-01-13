import asyncio


async def phase(i: int) -> str:
    print(f"in phase {i}")
    await asyncio.sleep(0.1 * i)
    print(f"done with phase {i}")
    return f"phase {i} result"


async def main(num_phases: int):
    print("starting main")
    results = []

    # 使用 TaskGroup 自动管理任务生命周期
    async with asyncio.TaskGroup() as tg:
        tasks = [tg.create_task(phase(i)) for i in range(num_phases)]

    # 退出上下文管理器时, 所有任务已确保完成
    results = [t.result() for t in tasks]
    print(f"results: {results!r}")


if __name__ == "__main__":
    # 4. 使用现代入口函数
    try:
        asyncio.run(main(3))
    except KeyboardInterrupt:
        pass

"""
$ python 15_asyncio_wait_04.py
starting main
in phase 0
in phase 1
in phase 2
done with phase 0
done with phase 1
done with phase 2
results: ['phase 0 result', 'phase 1 result', 'phase 2 result']
$

高级工程师的深度解析:

asyncio.wait 的重大变化:
旧代码: 直接传入 [phase(i) ...](协程对象).
现代要求: 必须传入 set 或 list 的 Task 对象. 这是因为协程对象是"一次性"的, 而 wait 需要在内部更精细地控制任务状态.

结果顺序问题:
asyncio.wait 返回的 completed 是一个 set(集合). 集合是无序的.
如果你直接写 [t.result() for t in completed], 结果列表的顺序可能是随机的(比如 [phase 2, phase 0, phase 1]).
高级技巧: 通过遍历原始的 tasks 列表来获取结果, 可以完美保持顺序.

异常处理(Implicit Safety):
asyncio.run() 会处理遗留的任务.

TaskGroup (方案三) 是目前处理并发任务最安全的方式, 它能确保即便某个任务崩溃, 整个程序也不会陷入不确定的状态.

f-strings 和类型提示:
继续沿用 f-strings 提高性能和可读性.
添加 i: int 和 -> str 等类型注解, 使代码具备生产环境的严谨性.

总结
对于你的原始需求, 方案一是最标准的现代修正; 但从工程简洁度看, 方案二 (gather) 通常是首选; 如果追求极致的健壮性, 方案三 (TaskGroup) 代表了异步 Python 的未来.

"""
