import asyncio


# 1. 增加类型注解, 使用 f-string 优化输出
async def consumer(n: int, q: asyncio.Queue):
    print(f"consumer {n}: starting")
    while True:
        print(f"consumer {n}: waiting for item")
        # 2. 这里的 await 会让出控制权, 直到队列中有数据
        item = await q.get()
        print(f"consumer {n}: has item {item}")

        if item is None:
            # None 是停止信号
            # 必须调用 task_done 以通知 q.join()
            q.task_done()
            break
        else:
            # 模拟 IO 密集型或计算密集型工作
            await asyncio.sleep(0.01 * item)
            # 告知队列该任务已处理完成
            q.task_done()

    print(f"consumer {n}: ending")


async def producer(q: asyncio.Queue, num_workers: int):
    print("producer: starting")

    # 模拟添加一些任务到队列
    for i in range(num_workers * 3):
        await q.put(i)
        print(f"producer: added task {i} to the queue")

    # 3. 添加停止信号(哨兵值)
    # 每个消费者都需要一个 None 来退出循环
    print("producer: adding stop signals to the queue")
    for _ in range(num_workers):
        await q.put(None)

    # 4. 等待队列中所有的任务(包括 None)被处理完成
    print("producer: waiting for queue to empty")
    await q.join()
    print("producer: ending")


async def main(num_consumers: int):
    # 5. 直接创建队列, 它会自动绑定到当前运行的 loop
    # 设置 maxsize 可以起到流量控制(Backpressure)的作用
    q = asyncio.Queue(maxsize=num_consumers)

    # 6. 使用 asyncio.create_task 启动消费者
    # 注意: 在现代 asyncio 中不需要手动传入 loop
    consumers = [asyncio.create_task(consumer(i, q)) for i in range(num_consumers)]

    # 7. 启动生产者
    prod = asyncio.create_task(producer(q, num_consumers))

    # 8. 等待所有协程完成
    # gather 比 wait 在这种场景下更简洁, 它会自动等待所有传入的 task 结束
    await asyncio.gather(*consumers, prod)
    print("All tasks are finished.")


if __name__ == "__main__":
    # 9. 现代标准入口: 处理 loop 的全生命周期, 解决弃用警告
    try:
        asyncio.run(main(num_consumers=2))
    except KeyboardInterrupt:
        pass

"""
作为高级 Python 开发工程师, 这段代码展示了异步编程中最经典的生产者-消费者模型(Producer-Consumer Pattern).

在现代 Python (3.10+) 的实践中, 改写的核心目标是:
消除显式的 loop 传递: 利用 asyncio.create_task 自动关联当前运行的循环.
规范化入口: 使用 asyncio.run() 替代手动的循环管理.
结构化并发: 虽然原有的 None 哨兵模式(Sentinel)依然有效, 但我们可以利用 asyncio.gather 或 TaskGroup 让任务管理更整洁.
性能与风格: 使用 f-strings 和类型提示.

高级工程师的深度解析:

为什么移除 loop 参数?
在旧版本中, asyncio.get_event_loop() 可能会在没有循环时创建新循环, 导致不可预期的行为.
现代 API 如 asyncio.create_task() 内部调用 get_running_loop(). 这确保了任务始终提交到"正在驱动 main() 执行"的那个循环中, 符合结构化并发的原则.

q.task_done() 与 q.join() 的配合:
这是 asyncio.Queue 的精髓. join() 会阻塞直到队列计数器归零.
每当消费者处理完一个 item 并调用 task_done() 时, 计数器减一. 即使是接收到 None 退出信号, 也必须调用 task_done(), 否则 producer 里的 await q.join() 将永远无法解锁, 导致程序死锁.

流量控制(Backpressure):
通过设置 asyncio.Queue(maxsize=num_consumers), 当生产者放得太快而消费者处理太慢时, await q.put() 会挂起. 这在生产环境中至关重要, 能防止因为任务堆积过多导致 OOM(内存溢出).

asyncio.run() 的优势:
它不仅解决了 DeprecationWarning, 还负责收尾: 取消所有未完成的任务、关闭异步生成器、关闭线程池. 如果你的 main 意外崩溃, asyncio.run 会确保资源被优雅释放.

关于 Python 3.11+ 的 TaskGroup:
如果你使用的是 Python 3.11, 我会建议使用 async with asyncio.TaskGroup() as tg: 来创建任务.
TaskGroup 的优势在于: 如果其中一个任务失败抛出异常, 它会自动取消组内其他任务. 这比 gather 更健壮, 避免了"孤儿任务"在后台静默运行.

总结
改写后的代码从"底层操作"转向了"声明式逻辑". 代码量更少, 但健壮性更强, 且完全适配未来版本的 Python.

$ python 22_asyncio_queue_02.py
consumer 0: starting
consumer 0: waiting for item
consumer 1: starting
consumer 1: waiting for item
producer: starting
producer: added task 0 to the queue
producer: added task 1 to the queue
consumer 0: has item 0
consumer 1: has item 1
producer: added task 2 to the queue
producer: added task 3 to the queue
consumer 0: waiting for item
consumer 0: has item 2
producer: added task 4 to the queue
consumer 1: waiting for item
consumer 1: has item 3
producer: added task 5 to the queue
producer: adding stop signals to the queue
consumer 0: waiting for item
consumer 0: has item 4
consumer 1: waiting for item
consumer 1: has item 5
producer: waiting for queue to empty
consumer 0: waiting for item
consumer 0: has item None
consumer 0: ending
consumer 1: waiting for item
consumer 1: has item None
consumer 1: ending
producer: ending
All tasks are finished.
$

"""
