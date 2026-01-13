import asyncio


async def wrapped() -> str:
    """被包装的底层协程"""
    print("wrapped")
    return "result"


async def inner(task: asyncio.Task):
    """
    接收一个已经在运行的任务并等待它.
    展示了 Task 对象可以跨协程传递.
    """
    print("inner: starting")
    print(f"inner: waiting for {task!r}")

    # 等待传入的任务完成
    result = await task
    print(f"inner: task returned {result!r}")


async def starter():
    """业务逻辑入口"""
    print("starter: creating task")

    # 1. 使用 asyncio.create_task 代替 ensure_future
    # 这会将协程包装成 Task 并立即加入事件循环调度
    task = asyncio.create_task(wrapped())

    print("starter: waiting for inner")
    # 2. 将 task 对象作为参数传递给另一个协程
    await inner(task)

    print("starter: inner returned")


if __name__ == "__main__":
    # 3. 使用 asyncio.run() 自动管理循环生命周期
    # 彻底解决 DeprecationWarning
    try:
        asyncio.run(starter())
    except KeyboardInterrupt:
        pass

"""
高级工程师的深度解析:

create_task() vs ensure_future():
旧代码使用的是 asyncio.ensure_future(). 虽然它在现在依然有效, 但它的设计初衷是作为一个底层工具(用于兼容 Future 对象和协程).
现代实践: 在已知输入是协程(coroutine)的情况下, 强烈建议使用 asyncio.create_task(). 它的语义更明确, 是专门为"启动后台任务"设计的官方高层 API.

Task 对象的"一等公民"特性:
这段代码展示了 asyncio.Task 是一个可以作为参数传递的对象.
高级细节: 即便 starter 已经通过 create_task 启动了任务, 它也可以把这个 task 句柄丢给 inner. 这在构建复杂的异步流水线(如生产者-消费者模型)时非常有用.

彻底告别 event_loop 样板代码:
原代码通过 get_event_loop 获取对象并手动 close. 这在现代异步编程中被视为"反模式"(Anti-pattern).
使用 asyncio.run() 不仅让代码简洁, 还带来了更安全的资源清理逻辑, 确保在程序退出前, 异步生成器和线程池执行器都能得到妥善处理.

f-string 与 类型提示 (Type Hints):
使用了 f"inner: waiting for {task!r}". 这里的 !r 是 repr() 的缩写, 对于调试 Task 的状态(是 <Task pending ...> 还是 <Task finished ...>)非常有帮助.
添加了 task: asyncio.Task 类型注解. 在大型工程中, 这能让同事(以及 IDE)瞬间明白这个参数期望的是什么对象.

总结
改写后的代码从"面向底层循环编程"进化到了"面向任务编排编程". 逻辑更加清晰, 且完全符合 Python 3.10+ 的标准规范, 没有任何弃用警告.

$ python 14_asyncio_ensure_future_02.py
starter: creating task
starter: waiting for inner
inner: starting
inner: waiting for <Task pending name='Task-2' coro=<wrapped() running at /python3-standard-library-example/source/23_asyncio/14_asyncio_ensure_future_02.py:3>>
wrapped
inner: task returned 'result'
starter: inner returned
$

"""
