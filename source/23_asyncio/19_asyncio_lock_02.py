import asyncio
import functools


# 1. 添加类型注解, 同步回调函数保持不变
def unlock(lock: asyncio.Lock):
    """同步回调函数, 用于释放锁"""
    print("callback releasing lock")
    # 注意: release() 是同步方法, 可以直接在回调中调用
    if lock.locked():
        lock.release()


async def coro1(lock: asyncio.Lock):
    """使用 async with 自动管理锁的获取和释放(推荐做法)"""
    print("coro1 waiting for the lock")
    async with lock:
        print("coro1 acquired lock")
    print("coro1 released lock")


async def coro2(lock: asyncio.Lock):
    """手动管理锁的获取和释放(演示用, 但在生产中优先考虑 async with)"""
    print("coro2 waiting for the lock")
    await lock.acquire()
    try:
        print("coro2 acquired lock")
    finally:
        # 确保锁一定会被释放, 防止死锁
        print("coro2 released lock")
        lock.release()


async def main():
    """主协程: 编排锁的竞争场景"""
    # 2. 在协程内部创建锁, 确保锁与当前运行的 loop 绑定
    lock = asyncio.Lock()

    print("acquiring the lock before starting coroutines")
    await lock.acquire()
    print(f"lock acquired: {lock.locked()}")

    # 3. 通过 get_running_loop 获取当前循环, 无需从外部传递
    loop = asyncio.get_running_loop()

    # 4. 安排 0.1 秒后执行回调解锁
    loop.call_later(0.1, functools.partial(unlock, lock))

    print("waiting for coroutines")

    # 5. 关键改进: 必须将协程包装为 Task 才能传给 asyncio.wait
    # 或者直接使用 asyncio.gather(通常更简洁)
    tasks = [asyncio.create_task(coro1(lock)), asyncio.create_task(coro2(lock))]

    await asyncio.wait(tasks)
    print("all coroutines finished")


if __name__ == "__main__":
    # 6. 使用现代标准入口, 自动管理 loop 的生命周期
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass

"""
在现代 Python (3.10+) 中, 主要的改进点在于消除弃用的 get_event_loop 警告、确保任务(Tasks)的正确创建, 以及遵循 RAII(资源获取即初始化) 原则使用上下文管理器.

高级工程师的深度解析:

解耦 Loop 对象:
旧代码: 将 loop 作为一个显式参数传递给 main.
现代做法: 使用 asyncio.get_running_loop(). 这符合现代异步设计的"环境感知"原则, 函数不再需要关心循环是从哪里来的, 只需在需要时从上下文中获取.

asyncio.wait 的语法要求:
在 Python 3.8+ 中, 直接将协程对象列表传给 asyncio.wait() 已被弃用.
必须步骤: 先用 asyncio.create_task() 将协程包装成任务, 然后再传递. 这样可以确保任务在被等待之前就已经在事件循环中开始调度.

锁的安全管理(RAII):
coro1 展示了 async with lock: 的用法. 这是最推荐的方式, 因为它利用了 Python 的上下文管理器协议, 即使在 with 块内部发生异常, 锁也会被自动释放, 有效避免死锁.
coro2 展示了手动 try...finally 的逻辑, 这在某些需要跨越多个非嵌套代码块持有锁的特殊场景下是必要的, 但必须严谨处理 finally.

同步与异步的桥梁:
unlock 函数是一个同步函数. asyncio.Lock.release() 也是一个同步方法. 这使得我们可以在 call_later 这种只能接受普通回调的底层调度器中操作异步锁.

消除弃用警告:
原代码中的 asyncio.get_event_loop() 在 Python 3.10 后如果在没有循环运行时调用会触发错误或警告.
使用 asyncio.run(main()) 封装了循环的整个生命周期(创建、运行、清理、关闭), 这是编写健壮异步代码的黄金法则.

总结
改写后的代码不仅更简洁, 而且修复了 asyncio.wait 传参不规范的潜在问题. 在编写涉及并发控制(如 Lock, Semaphore, Event)的代码时, 始终优先使用 上下文管理器 (async with) 和 现代入口函数 (asyncio.run).

$ python 19_asyncio_lock_02.py
acquiring the lock before starting coroutines
lock acquired: True
waiting for coroutines
coro1 waiting for the lock
coro2 waiting for the lock
callback releasing lock
coro1 acquired lock
coro1 released lock
coro2 acquired lock
coro2 released lock
all coroutines finished
$

"""
