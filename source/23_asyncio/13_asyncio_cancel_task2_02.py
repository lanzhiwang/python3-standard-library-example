import asyncio


async def task_func():
    """
    子任务: 演示如何优雅地处理取消信号
    """
    print("in task_func, sleeping")
    try:
        # 模拟耗时操作
        await asyncio.sleep(1)
    except asyncio.CancelledError:
        # 高级实践: 在捕获取消异常后进行清理, 然后必须重新抛出
        print("task_func was canceled - performing cleanup if needed")
        raise
    return "the result"


def task_canceller(t: asyncio.Task):
    """
    同步回调函数: 用于执行取消操作
    """
    print("in task_canceller")
    t.cancel()
    print("canceled the task")


async def main():
    """
    主协程: 编排任务生命周期
    """
    # 1. 直接使用高层 API 创建任务
    print("creating task")
    task = asyncio.create_task(task_func())

    # 2. 获取当前运行的循环以调度同步回调
    loop = asyncio.get_running_loop()
    loop.call_soon(task_canceller, task)

    try:
        # 3. 等待任务完成
        await task
    except asyncio.CancelledError:
        # 4. 当子任务抛出 CancelledError 且被 await 时, 调用方也会捕获到
        print("main() also sees task as canceled")


if __name__ == "__main__":
    # 5. 使用现代入口函数, 自动处理 loop 的创建与关闭
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass

"""
$ python 13_asyncio_cancel_task2_02.py
creating task
in task_func, sleeping
in task_canceller
canceled the task
task_func was canceled - performing cleanup if needed
main() also sees task as canceled
$
"""
