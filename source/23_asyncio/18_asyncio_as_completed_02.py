import asyncio


# 1. 添加类型注解, 提高代码可维护性
async def phase(i: int) -> str:
    """
    模拟一个异步阶段, 耗时随 i 的增大而减少.
    这意味着 phase(2) 会比 phase(0) 先完成.
    """
    print(f"in phase {i}")
    # 逻辑: phase 0 耗时 0.5s, phase 1 耗时 0.4s, phase 2 耗时 0.3s
    await asyncio.sleep(0.5 - (0.1 * i))
    print(f"done with phase {i}")
    return f"phase {i} result"


async def main(num_phases: int):
    print("starting main")

    # 2. 创建协程列表
    # 注意: as_completed 内部会自动将协程包装为 Task
    phases = [phase(i) for i in range(num_phases)]

    print("waiting for phases to complete")
    results = []

    # 3. 使用 as_completed 迭代器
    # 它返回一个迭代器, 每次 yield 一个最先完成任务的 future
    for next_to_complete in asyncio.as_completed(phases):
        # 只要有一个任务完成, 这里就会立即恢复执行
        answer = await next_to_complete
        print(f"received answer {answer!r}")
        results.append(answer)

    print(f"results: {results!r}")
    return results


if __name__ == "__main__":
    # 4. 使用现代标准入口 asyncio.run
    # 它负责创建循环、运行主协程并彻底清理资源
    try:
        asyncio.run(main(3))
    except KeyboardInterrupt:
        pass

"""
与 asyncio.gather 不同, as_completed 不保证结果的顺序, 而是允许你在任务完成的第一时间就获取并处理结果, 这在需要降低首个结果响应延迟(TTFB)的场景下非常有用.

高级工程师的深度解析:

as_completed 的核心价值:
非阻塞处理: 在你的例子中, phase(2) 只需要 0.3s, 而 phase(0) 需要 0.5s. 使用 as_completed, 你会看到 phase 2 的结果最先被打印.
适用场景: 当你需要并发请求多个 API, 且希望谁先返回就先处理谁的数据(例如更新进度条或流式展示结果)时, 这是最佳选择.

移除过时的 Loop 管理:
删除了 get_event_loop() 和 loop.close().
理由: asyncio.run() 是自 Python 3.7+ 以来的官方推荐做法. 它能确保每次运行都在干净的循环中进行, 并自动处理诸如取消遗留任务、关闭异步生成器和清理线程池执行器等复杂操作.

语法现代化:
f-strings: 使用 f"{answer!r}" 代替 .format(). !r 标记等同于调用 repr(), 这在打印字符串结果时能清晰显示引号, 是调试时的良好习惯.
类型提示 (Type Hints): 给函数加上 i: int 和 -> str, 这在高级工程实践中是标准要求, 有助于静态分析和 IDE 错误提示.

关于 phases 列表的进阶思考:
虽然 as_completed 可以直接接受协程对象列表, 但在极其复杂的场景下, 手动先用 asyncio.create_task() 封装它们也是一种选择. 不过对于 as_completed 来说, 直接传入协程列表是其最地道的用法, 因为它内部会高效地处理这些任务的挂载.

Python 3.11+ 的补充建议:
如果你的项目已经升级到 3.11+, 虽然 as_completed 依然有效, 但如果你需要更强大的错误处理和任务追踪, 可以关注 asyncio.TaskGroup. 不过 TaskGroup 默认是等待所有任务结束, 若要实现"完成一个处理一个", as_completed 依然是目前的标准工具.

总结
改写后的代码更加精简(Pythonic), 逻辑重心从"如何管理循环"转移到了"如何编排业务逻辑". 这不仅消除了弃用警告, 也让代码具备了更强的健壮性.

$ python 18_asyncio_as_completed_02.py
starting main
waiting for phases to complete
in phase 1
in phase 2
in phase 0
done with phase 2
received answer 'phase 2 result'
done with phase 1
received answer 'phase 1 result'
done with phase 0
received answer 'phase 0 result'
results: ['phase 2 result', 'phase 1 result', 'phase 0 result']
$

"""
