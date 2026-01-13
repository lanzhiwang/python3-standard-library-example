#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2014 Doug Hellmann.  All rights reserved.
"""TCP echo server using asyncio with a Protocol class."""

# end_pymotw_header
import asyncio
import logging
import sys

SERVER_ADDRESS = ("localhost", 10000)


class EchoServer(asyncio.Protocol):

    def connection_made(self, transport):
        """
        每个新的客户端连接都会触发对以下函数的调用: connection_made().
        """
        self.transport = transport
        self.address = transport.get_extra_info("peername")
        self.log = logging.getLogger("EchoServer_{}_{}".format(*self.address))
        self.log.debug("connection accepted")

    def data_received(self, data):
        """
        连接建立后, 当客户端向服务器发送数据时, 会调用协议的 data_received() 方法将数据传递给服务器进行处理.
        数据以字节字符串的形式传递, 由应用程序负责以适当的方式对其进行解码.
        解码结果会被记录下来, 然后立即调用 transport.write() 将响应发送回客户端.
        """
        self.log.debug("received {!r}".format(data))
        self.transport.write(data)
        self.log.debug("sent {!r}".format(data))

    def eof_received(self):
        """
        某些传输协议支持特殊的文件结束符("EOF"). 当遇到 EOF 时, 会调用 eof_received() 方法.
        在该实现中, EOF 会被发送回客户端, 以表明已接收到该文件. 由于并非所有传输协议都支持显式 EOF, 因此该协议会先询问传输协议是否可以安全地发送 EOF.
        """
        self.log.debug("received EOF")
        if self.transport.can_write_eof():
            self.transport.write_eof()

    def connection_lost(self, error):
        """
        当连接正常关闭或因错误而关闭时, 会调用协议的 connection_lost() 方法.
        如果发生错误, 则参数包含相应的异常对象; 否则, 参数为 None.
        """
        if error:
            self.log.error("ERROR: {}".format(error))
        else:
            self.log.debug("closing")
        super().connection_lost(error)


logging.basicConfig(
    level=logging.DEBUG,
    format="%(name)s: %(message)s",
    stream=sys.stderr,
)
log = logging.getLogger("main")

event_loop = asyncio.get_event_loop()

"""
启动服务器分为两个步骤.
首先是应用程序. 指示事件循环使用该协议创建一个新的服务器对象. 类名、主机名和要监听的套接字.
create_server() 方法是一个协程, 因此必须由事件循环处理其结果才能真正启动服务器.
协程执行完毕后会生成一个 asyncio.Server 对象. 与事件循环关联的实例.
"""
# Create the server and let the loop finish the coroutine before
# starting the real event loop.
factory = event_loop.create_server(EchoServer, *SERVER_ADDRESS)
server = event_loop.run_until_complete(factory)
log.debug("starting up on {} port {}".format(*SERVER_ADDRESS))

"""
然后需要运行事件循环来处理事件, 并且处理客户端请求.
对于长期运行的服务而言, run_forever() 方法是实现此目的的最简单方法.
当事件循环停止时(无论是通过应用程序代码停止还是通过向进程发送信号停止), 服务器可以关闭以正确清理套接字, 然后事件循环可以关闭以完成对任何其他协程的处理, 之后程序才会退出.
"""
# Enter the event loop permanently to handle all connections.
try:
    event_loop.run_forever()
finally:
    log.debug("closing server")
    server.close()
    event_loop.run_until_complete(server.wait_closed())
    log.debug("closing event loop")
    event_loop.close()

"""
$ python 23_1_asyncio_echo_server_protocol.py
asyncio: Using selector: EpollSelector
main: starting up on localhost port 10000

EchoServer_::1_62098: connection accepted

EchoServer_::1_62098: received b'This is the message. It will be sent in parts.'
EchoServer_::1_62098: sent b'This is the message. It will be sent in parts.'
EchoServer_::1_62098: received EOF

EchoServer_::1_62098: closing

^Cmain: closing server
main: closing event loop
Traceback (most recent call last):
  File "23_1_asyncio_echo_server_protocol.py", line 61, in <module>
    event_loop.run_forever()
  File "/usr/local/lib/python3.8/asyncio/base_events.py", line 570, in run_forever
    self._run_once()
  File "/usr/local/lib/python3.8/asyncio/base_events.py", line 1823, in _run_once
    event_list = self._selector.select(timeout)
  File "/usr/local/lib/python3.8/selectors.py", line 468, in select
    fd_event_list = self._selector.poll(timeout, max_ev)
KeyboardInterrupt

"""
