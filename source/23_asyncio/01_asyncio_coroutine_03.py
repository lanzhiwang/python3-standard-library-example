"""
方案 B: 如果确实需要手动管理(底层开发需求)
如果你在写底层框架, 或者确实需要保留对 event_loop 对象的引用, 你应该显式地创建它, 而不是让系统"猜":
"""

import asyncio


async def coroutine():
    print("in coroutine")


def main():
    # 显式创建新的循环对象
    loop = asyncio.new_event_loop()
    # 显式设置为当前线程的循环(可选, 取决于后续是否需要 get_event_loop)
    asyncio.set_event_loop(loop)

    try:
        print("starting coroutine")
        loop.run_until_complete(coroutine())
    finally:
        print("closing event loop")
        loop.close()


if __name__ == "__main__":
    main()

"""
$ python 01_asyncio_coroutine_03.py
starting coroutine
in coroutine
closing event loop
$
"""
