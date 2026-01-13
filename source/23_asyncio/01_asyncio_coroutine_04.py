"""
方案 C: 在协程内部获取循环
如果你已经处于一个 async def 函数中, 需要获取当前的循环, 请永远使用 asyncio.get_running_loop(), 它不会触发警告且效率更高.
"""

import asyncio


async def coroutine():
    print("in coroutine")
    loop = asyncio.get_running_loop()  # 安全, 且专门用于获取"当前正在运行"的循环
    print(f"Running in loop: {loop}")


async def main():
    print("starting coroutine")
    # 直接 await 协程, 不需要手动操作 loop
    await coroutine()
    print("coroutine finished")


if __name__ == "__main__":
    # asyncio.run 是 3.7+ 引入的最高层入口
    asyncio.run(main())

"""
$ python 01_asyncio_coroutine_04.py
starting coroutine
in coroutine
Running in loop: <_UnixSelectorEventLoop running=True closed=False debug=False>
coroutine finished
$
"""
