import asyncio


# 1. 明确返回类型注解
async def task_func() -> str:
    print("in task_func")
    return "the result"


async def main():
    """
    主协程: 演示 Task 的创建和状态跟踪
    """
    print("creating task")

    # 2. 直接使用 asyncio.create_task()
    # 它会自动获取当前的 running loop, 无需手动传递 loop 对象
    task = asyncio.create_task(task_func())

    # 3. 使用 f-string 和 !r (repr) 提高调试信息的可读性
    print(f"waiting for {task!r}")

    # 4. 等待任务完成
    return_value = await task

    print(f"task completed {task!r}")
    print(f"return value: {return_value!r}")


if __name__ == "__main__":
    # 5. 使用现代化的单入口, 自动处理事件循环的创建、运行和优雅关闭
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass

"""
在现代 asyncio 实践中, asyncio.create_task() 会自动获取当前运行的事件循环并提交任务, 这比手动通过 loop.create_task 更加简洁且符合"关注点分离"的原则.

高级工程师的深度解析:

asyncio.create_task() 的优越性:
旧写法: loop.create_task(coro) 需要你先有一个 loop 引用.
新写法: asyncio.create_task(coro) 是 Python 3.7+ 引入的推荐方式. 它在内部调用 get_running_loop(), 确保任务被提交到当前正在驱动 main() 的那个循环中.

移除 main(loop) 参数:
在高级工程实践中, 我们尽量避免"深层传递底层组件". 让 main 依赖于 loop 变量会降低函数的可重用性. 现代异步代码倾向于认为"循环已经作为基础设施存在于上下文中".

Task 与 Coroutine 的区别:
当你调用 task_func() 时, 你只是得到了一个协程对象(Coroutine Object), 它还没开始运行.
当你调用 asyncio.create_task() 时, 该协程被包装成一个 Task, 并被立即排入事件循环等待执行. 这意味着即使你没有立即 await 它, 它也可能已经开始在后台跑了.

asyncio.run() 的黑盒特性:
它不仅解决了 DeprecationWarning, 还负责了非常重要的收尾工作: 它会取消所有尚未完成的任务, 关闭异步生成器, 并彻底关闭线程池执行器. 这在生产环境下防止资源泄漏至关重要.

f-string 的 !r 技巧:
在打印对象(如 Task)时, 使用 {task!r} 会调用对象的 __repr__ 方法, 输出类似于 <Task pending name='Task-1' ...> 的详细信息. 这在异步编程的调试中非常有用, 可以直观看到 Task 的状态(pending/finished).

总结
改写后的代码不仅消除了过时的 API 调用, 还通过封装和解耦提升了代码质量. 现在, 你的 main 函数变得更加"纯粹", 只包含业务逻辑的调度, 而不包含底层循环的管理.

$ python 11_asyncio_create_task_02.py
creating task
waiting for <Task pending name='Task-2' coro=<task_func() running at /python3-standard-library-example/source/23_asyncio/11_asyncio_create_task_02.py:4>>
in task_func
task completed <Task finished name='Task-2' coro=<task_func() done, defined at /python3-standard-library-example/source/23_asyncio/11_asyncio_create_task_02.py:4> result='the result'>
return value: 'the result'
$

"""
