import asyncio


# 1. 使用 async def 定义原生协程, 取代 @asyncio.coroutine 装饰器
async def phase1():
    print("in phase1")
    return "result1"


async def phase2(arg):
    print("in phase2")
    return f"result2 derived from {arg}"


async def outer():
    print("in outer")

    print("waiting for result1")
    # 2. 使用 await 取代 yield from
    result1 = await phase1()

    print("waiting for result2")
    result2 = await phase2(result1)

    return (result1, result2)


def main():
    # 3. 使用 asyncio.run() 自动管理生命周期, 取代手动 loop 操作
    try:
        return_value = asyncio.run(outer())
        print(f"return value: {return_value!r}")
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()

"""
$ python 04_asyncio_generator_02.py
in outer
waiting for result1
in phase1
waiting for result2
in phase2
return value: ('result1', 'result2 derived from result1')
$

核心改进解析:

从"基于生成器的协程"迁移到"原生协程":
旧写法: @asyncio.coroutine + yield from. 这是在 Python 引入 async/await 关键字之前的过渡方案.
新写法: async def + await. 这在底层实现上更高效, 且能提供更好的类型检查支持和更清晰的堆栈跟踪(Stack Traces).

彻底删除旧的循环管理代码:
去掉了 event_loop = asyncio.get_event_loop(), 因为它在 3.10+ 版本中会触发警告甚至报错.
去掉了 loop.close(), 因为 asyncio.run() 会在程序结束时自动关闭循环、取消剩余任务并清理底层的执行器.

语法现代化:
使用了 f-strings (f'...'), 这比 .format() 更符合现代 Python 规范, 且运行效率更高.
使用了 !r 转换符, 确保在打印结果时保留其 __repr__ 格式(如字符串带引号), 这与你原代码的 {!r} 保持逻辑一致.

为什么必须这样改? (高级开发的视角)
版本兼容性: Python 3.11 已经正式删除了 @asyncio.coroutine. 如果你使用 Python 3.11 或更高版本运行你原来的代码, 会直接抛出 AttributeError.
性能提升: 原生协程(async def)比基于生成器的协程(yield from)在调用开销上更小.
可读性: async/await 语义明确, 一眼就能看出哪些代码是异步的.

总结: 这种改写不仅仅是为了消除警告, 更是为了从"过时的过渡语法"进化到"现代生产环境标准".
如果你在维护一个旧项目, 建议分批次将所有的 yield from 替换为 await.
"""
