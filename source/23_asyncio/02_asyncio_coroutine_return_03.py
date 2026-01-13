import asyncio


async def coroutine():
    print("in coroutine")
    return "result"


# 显式创建并手动管理(仅在极少数高级底层场景下使用)
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
try:
    return_value = loop.run_until_complete(coroutine())
    print(f"it returned: {return_value!r}")
finally:
    loop.close()

"""
$ python 02_asyncio_coroutine_return_03.py
in coroutine
it returned: 'result'
$
"""
