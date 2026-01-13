import asyncio
import logging
import sys

# 建议使用命名元组或常量定义配置
SERVER_ADDRESS = ("localhost", 10000)


class EchoServer(asyncio.Protocol):
    """
    底层协议实现.
    注意: Protocol 实例是为每个连接运行一次的.
    """

    def connection_made(self, transport: asyncio.Transport):
        self.transport = transport
        self.address = transport.get_extra_info("peername")
        # 现代写法: 使用更加内聚的日志记录
        self.log = logging.getLogger(f"EchoServer_{self.address[0]}_{self.address[1]}")
        self.log.debug("connection accepted")

    def data_received(self, data: bytes):
        self.log.debug(f"received {data!r}")
        self.transport.write(data)
        self.log.debug(f"sent {data!r}")

    def eof_received(self):
        self.log.debug("received EOF")
        if self.transport.can_write_eof():
            self.transport.write_eof()
        # 返回 False 以便让传输层关闭连接
        return False

    def connection_lost(self, error):
        if error:
            self.log.error(f"ERROR: {error}")
        else:
            self.log.debug("closing connection")
        super().connection_lost(error)


async def main():
    """
    主程序协程: 管理服务器生命周期
    """
    log = logging.getLogger("main")

    # 1. 获取当前运行的事件循环
    loop = asyncio.get_running_loop()

    # 2. 创建服务器对象
    # 在 3.7+ 中, 建议配合 async with 使用 server 对象
    server = await loop.create_server(lambda: EchoServer(), *SERVER_ADDRESS)

    log.info(f"starting up on {SERVER_ADDRESS[0]} port {SERVER_ADDRESS[1]}")

    # 3. 使用异步上下文管理器自动处理 close() 和 wait_closed()
    async with server:
        try:
            # 持续运行直到被手动停止(如 Ctrl+C)
            await server.serve_forever()
        except asyncio.CancelledError:
            log.info("Server cancellation requested")
        finally:
            log.info("server is shutting down")


if __name__ == "__main__":
    # 配置日志
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        stream=sys.stderr,
    )

    # 4. 现代 Python 入口: asyncio.run 会处理 loop 的创建和销毁
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        # 优雅处理用户手动停止
        logging.getLogger("main").info("Server stopped by user")
