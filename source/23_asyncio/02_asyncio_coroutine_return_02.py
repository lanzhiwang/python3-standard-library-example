import asyncio


async def coroutine():
    print("in coroutine")
    return "result"


def main():
    # asyncio.run 会自动:
    # 1. 创建一个新的事件循环
    # 2. 将协程作为主入口点运行
    # 3. 返回协程的结果
    # 4. 关闭循环并清理异步生成器
    return_value = asyncio.run(coroutine())

    print(f"it returned: {return_value!r}")


if __name__ == "__main__":
    main()

"""
$ python 02_asyncio_coroutine_return_02.py
in coroutine
it returned: 'result'
$
"""
