import asyncio


async def coroutine():
    print("in coroutine")
    return "result"


async def main():
    print("starting coroutine")
    # 直接 await 协程, 不需要手动操作 loop
    return_value = await coroutine()
    print(f"it returned: {return_value!r}")
    print("coroutine finished")


if __name__ == "__main__":
    # asyncio.run 是 3.7+ 引入的最高层入口
    asyncio.run(main())

"""
$ python 02_asyncio_coroutine_return_04.py
starting coroutine
in coroutine
it returned: 'result'
coroutine finished
$
"""
