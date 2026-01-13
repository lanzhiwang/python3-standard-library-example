import asyncio


# 1. 使用类型提示 (Type Hints) 和 f-strings
async def consumer(condition: asyncio.Condition, n: int):
    """消费者: 等待条件变量的通知"""
    async with condition:
        print(f"consumer {n} is waiting")
        # wait() 会释放底层锁, 直到被 notify 唤醒并重新获得锁
        await condition.wait()
        print(f"consumer {n} triggered")
    print(f"ending consumer {n}")


async def manipulate_condition(condition: asyncio.Condition):
    """逻辑控制者: 负责发送通知"""
    print("starting manipulate_condition")

    # 稍微等待, 确保消费者都已经进入 wait 状态
    await asyncio.sleep(0.1)

    # 逐步通知: 第一次通知 1 个, 第二次通知 2 个
    for i in range(1, 3):
        async with condition:
            print(f"notifying {i} consumers")
            condition.notify(n=i)
        await asyncio.sleep(0.1)

    # 最后通知剩余的所有消费者
    async with condition:
        print("notifying remaining consumers")
        condition.notify_all()

    print("ending manipulate_condition")


async def main():
    """主协程: 负责初始化和并发编排"""
    # 2. 在协程内部创建 Condition 变量
    condition = asyncio.Condition()

    # 3. 将协程包装为 Task 对象
    # 现代标准: 不再向 wait 直接传协程列表, 必须先使用 create_task
    consumers = [asyncio.create_task(consumer(condition, i)) for i in range(5)]

    # 4. 启动控制协程作为背景任务
    # 使用 asyncio.create_task 而不是 loop.create_task
    asyncio.create_task(manipulate_condition(condition))

    # 5. 等待所有消费者完成
    # 也可以使用 asyncio.gather(*consumers)
    await asyncio.wait(consumers)
    print("All consumers have finished.")


if __name__ == "__main__":
    # 6. 使用现代标准入口, 自动处理创建、运行和关闭 loop 的细节
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass

"""
$ python 21_asyncio_condition_02.py
consumer 0 is waiting
consumer 1 is waiting
consumer 2 is waiting
consumer 3 is waiting
consumer 4 is waiting
starting manipulate_condition
notifying 1 consumers
consumer 0 triggered
ending consumer 0
notifying 2 consumers
consumer 1 triggered
ending consumer 1
consumer 2 triggered
ending consumer 2
notifying remaining consumers
ending manipulate_condition
consumer 3 triggered
ending consumer 3
consumer 4 triggered
ending consumer 4
All consumers have finished.
$
"""
