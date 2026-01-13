import asyncio
import functools


# 1. 增加类型注解, 使用 f-string 优化输出
def callback(future: asyncio.Future, n: int):
    """
    注意: add_done_callback 会自动将 future 对象作为第一个参数传入
    """
    try:
        print(f"{n}: future done: {future.result()}")
    except Exception as e:
        print(f"{n}: future failed with: {e}")


async def register_callbacks(all_done: asyncio.Future):
    print("registering callbacks on future")
    # 2. 使用 functools.partial 绑定额外的参数
    # add_done_callback 会在 future 完成时, 将 future 自身传给 callback
    all_done.add_done_callback(functools.partial(callback, n=1))
    all_done.add_done_callback(functools.partial(callback, n=2))


async def main():
    """
    主协程: 负责逻辑编排
    """
    # 3. 通过 get_running_loop 动态获取循环并创建 Future
    loop = asyncio.get_running_loop()
    all_done = loop.create_future()

    # 4. 注册回调
    await register_callbacks(all_done)

    print("setting result of future")
    all_done.set_result("the result")

    # 5. [高级细节] 给事件循环一个机会去执行刚刚排队的回调
    # 虽然在 simple 场景下不是必须的, 但在复杂应用中,
    # 显式让出控制权确保回调被立即处理是一个好习惯.
    await asyncio.sleep(0)


if __name__ == "__main__":
    # 6. 使用现代入口函数, 自动处理 loop.close()
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass

"""
$ python 10_asyncio_future_callback_02.py
registering callbacks on future
setting result of future
1: future done: the result
2: future done: the result
$
"""
