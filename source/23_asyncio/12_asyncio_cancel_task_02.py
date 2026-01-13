import asyncio


async def task_func():
    """
    一个简单的异步任务
    """
    print("in task_func")
    # 模拟异步操作
    await asyncio.sleep(1)
    return "the result"


async def main():
    """
    主协程: 演示任务的创建、取消与异常捕获
    """
    print("creating task")
    # 1. 使用高层 API 创建任务, 无需显式传递 loop
    task = asyncio.create_task(task_func())

    print("canceling task")
    # 2. 请求取消任务
    # cancel() 只是发送一个请求, 任务会在下一次进入事件循环时抛出 CancelledError
    task.cancel()

    print(f"canceled task {task!r}")

    try:
        # 3. 必须 await 已经被取消的任务, 否则会产生 "Task was destroyed but it is pending" 警告
        await task
    except asyncio.CancelledError:
        # 4. 捕获取消异常, 这是处理任务取消的标准方式
        print("caught error from canceled task")
    except Exception as e:
        # 捕获其他可能的异常
        print(f"task failed with other error: {e}")
    else:
        # 如果任务没被取消且成功完成
        print(f"task result: {task.result()!r}")


if __name__ == "__main__":
    # 5. 使用 asyncio.run() 自动管理循环, 解决 DeprecationWarning
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass

"""
$ python 12_asyncio_cancel_task_02.py
creating task
canceling task
canceled task <Task cancelling name='Task-2' coro=<task_func() running at /python3-standard-library-example/source/23_asyncio/12_asyncio_cancel_task_02.py:3>>
caught error from canceled task
$
"""
