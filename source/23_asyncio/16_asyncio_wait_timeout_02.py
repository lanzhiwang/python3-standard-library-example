import asyncio


async def phase(i: int):
    """模拟异步阶段, 支持优雅取消"""
    print(f"in phase {i}")
    try:
        # phase 0 等待 0s, phase 1 等待 0.1s, phase 2 等待 0.2s
        await asyncio.sleep(0.1 * i)
    except asyncio.CancelledError:
        print(f"phase {i} canceled")
        raise  # 必须重新抛出, 以符合协程取消协议
    else:
        print(f"done with phase {i}")
        return f"phase {i} result"


async def main(num_phases: int):
    print("starting main")

    # 1. 关键: 必须先创建 Task 对象. asyncio.wait 不再接受协程列表.
    tasks = [asyncio.create_task(phase(i)) for i in range(num_phases)]

    print("waiting 0.1s for phases to complete")
    # 2. asyncio.wait 返回 (done, pending) 集合
    done, pending = await asyncio.wait(tasks, timeout=0.1)

    print(f"{len(done)} completed and {len(pending)} pending")

    # 3. 处理超时后的挂起任务
    if pending:
        print("canceling pending tasks")
        for t in pending:
            t.cancel()

        # 4. 高级实践: 不仅要取消, 还要等待它们完成取消逻辑
        # 使用 return_exceptions=True 忽略 CancelledError 异常抛出
        await asyncio.gather(*pending, return_exceptions=True)

    print("exiting main")


if __name__ == "__main__":
    # 5. 使用现代入口函数, 自动处理 loop 生命周期
    try:
        asyncio.run(main(3))
    except KeyboardInterrupt:
        pass

"""
$ python 16_asyncio_wait_timeout_02.py
starting main
waiting 0.1s for phases to complete
in phase 0
in phase 1
in phase 2
done with phase 0
1 completed and 2 pending
canceling pending tasks
phase 1 canceled
phase 2 canceled
exiting main
$
"""
