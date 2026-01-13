"""
方案 A: 使用 asyncio.run() (强烈推荐)
这是最标准、最现代的做法. asyncio.run() 会自动负责循环的创建、运行和最后的关闭清理工作, 代码极其整洁.
"""

import asyncio


async def coroutine():
    print("in coroutine")


async def main():
    print("starting coroutine")
    # 直接 await 协程, 不需要手动操作 loop
    await coroutine()
    print("coroutine finished")


if __name__ == "__main__":
    # asyncio.run 是 3.7+ 引入的最高层入口
    asyncio.run(main())

"""
$ python 01_asyncio_coroutine_02.py
starting coroutine
in coroutine
coroutine finished
$
"""
