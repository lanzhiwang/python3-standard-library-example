import asyncio


def callback(n: int):
    """同步回调函数"""
    print(f"callback {n} invoked")


async def main():
    """
    主协程: 演示事件循环的任务调度
    """
    # 1. 动态获取当前正在运行的事件循环
    # 相比 get_event_loop, 它在没有循环运行时会报错, 更安全且符合预期
    loop = asyncio.get_running_loop()

    print("registering callbacks")

    # 2. 调度延时任务
    # call_later(延迟秒数, 回调函数, 参数)
    loop.call_later(0.2, callback, 1)  # 0.2 秒后执行
    loop.call_later(0.1, callback, 2)  # 0.1 秒后执行
    loop.call_soon(callback, 3)  # 尽快执行(通常是下一次迭代)

    # 3. 阻塞主协程, 让出控制权
    # 必须 sleep 足够长的时间, 否则主协程结束导致循环停止, 延时回调可能来不及执行
    await asyncio.sleep(0.4)


if __name__ == "__main__":
    # 4. 使用 asyncio.run 自动管理循环的创建、运行和关闭
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass

"""
作为一名高级 Python 开发工程师, 针对这段涉及 延时回调(Scheduled Callbacks) 的代码, 改写的核心目标是:
消除显式的循环传递, 并利用 Python 3.7+ 引入的结构化生命周期管理.

在现代异步编程中, 我们通常不再将 loop 对象作为参数在函数间传递, 而是让协程在需要时动态获取它.

高级工程师的改进深度解析:

使用 asyncio.get_running_loop():
弃用旧方法: 避免在 main 的参数中手动传入 loop.
原因: 在异步函数内部, get_running_loop() 是获取当前循环的最佳实践. 它明确表示"我期望现在已经有一个循环在跑了", 这比 get_event_loop() 的模棱两可(可能创建新循环)要清晰得多.

理解调度顺序(执行逻辑):
虽然我们在代码里先写了 callback 1, 再写了 callback 3, 但执行顺序如下:
第一步: callback 3 (由 call_soon 注册, 几乎立即执行).
第二步: callback 2 (0.1 秒后).
第三步: callback 1 (0.2 秒后).
这种非阻塞的调度特性是 asyncio 底层高效的核心, 改写后的代码依然完美保留了这一行为.

生命周期自动化:
原代码使用 try...finally 配合 loop.close() 是为了防止资源泄露.
asyncio.run() 内部不仅执行了 run_until_complete, 还会在退出前自动取消所有未完成的任务(Pending Tasks)并彻底关闭循环, 大大减少了模板代码(Boilerplate Code).

f-string 与 类型注解:
使用了 f"callback {n} invoked" 替代 .format().

为 callback 添加了类型注解 (n: int), 这在现代团队开发中是必不可少的, 有助于静态检查工具(如 MyPy)发现潜在 Bug.

专家提示:
如果你在开发中发现自己频繁使用 call_later, 请思考是否可以改用 asyncio.create_task 配合 asyncio.sleep.
通常情况下, 基于 await 的代码比基于回调(Callback)的代码更易于维护和调试. 但在需要极高性能或与底层 C 扩展交互时, 保留 call_later 是正确的选择.

$ python 06_asyncio_call_later_02.py
registering callbacks
callback 3 invoked
callback 2 invoked
callback 1 invoked
$

"""
