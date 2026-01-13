#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2014 Doug Hellmann.  All rights reserved.
"""Echo client using a Protocol class"""

# end_pymotw_header
import asyncio
import functools
import logging
import sys

MESSAGES = [
    b"This is the message. ",
    b"It will be sent ",
    b"in parts.",
]
SERVER_ADDRESS = ("localhost", 10000)


class EchoClient(asyncio.Protocol):

    def __init__(self, messages, future):
        """
        客户端协议类定义了与服务器相同的方法, 但实现方式不同.
        该类的构造函数接受两个参数: 要发送的消息列表和一个 Future 用于指示客户端已完成一个周期的实例
        通过接收服务器的响应来实现其功能.
        """
        super().__init__()
        self.messages = messages
        self.log = logging.getLogger("EchoClient")
        self.f = future

    def connection_made(self, transport):
        """
        客户端成功连接到服务器后, 会立即开始通信. 消息会逐条发送, 但底层网络代码可能会将多条消息合并到一次传输中.
        当所有消息都发送完毕后, 会发送文件结束符 (EOF).
        虽然看起来数据似乎立即发送, 但实际上传输对象会将发送的数据缓冲起来, 并设置一个回调函数, 以便在套接字的缓冲区准备好接收数据时才进行实际传输.
        这一切都是透明处理的, 因此应用程序代码可以像 I/O 操作立即发生一样编写.
        """
        self.transport = transport
        self.address = transport.get_extra_info("peername")
        self.log.debug("connecting to {} port {}".format(*self.address))
        # This could be transport.writelines() except that
        # would make it harder to show each part of the message
        # being sent.
        for msg in self.messages:
            transport.write(msg)
            self.log.debug("sending {!r}".format(msg))
        if transport.can_write_eof():
            transport.write_eof()

    def data_received(self, data):
        """
        当收到服务器的响应时, 会将其记录下来.
        """
        self.log.debug("received {!r}".format(data))

    def eof_received(self):
        """
        当收到文件结束标记或服务器端关闭连接时, 本地传输对象将被关闭, 并通过设置结果将未来对象标记为已完成.
        """
        self.log.debug("received EOF")
        self.transport.close()
        if not self.f.done():
            self.f.set_result(True)

    def connection_lost(self, exc):
        self.log.debug("server closed connection")
        self.transport.close()
        if not self.f.done():
            self.f.set_result(True)
        super().connection_lost(exc)


logging.basicConfig(
    level=logging.DEBUG,
    format="%(name)s: %(message)s",
    stream=sys.stderr,
)
log = logging.getLogger("main")

event_loop = asyncio.get_event_loop()

"""
通常情况下, 协议类会被传递给事件循环以创建连接.
但在本例中, 由于事件循环无法向协议构造函数传递额外的参数, 因此需要创建一个 partial 来包装客户端类, 并将要发送的消息列表和 Future 实例传递给它.
"""
client_completed = asyncio.Future()

client_factory = functools.partial(
    EchoClient,
    messages=MESSAGES,
    future=client_completed,
)
factory_coroutine = event_loop.create_connection(
    client_factory,
    *SERVER_ADDRESS,
)

"""
为了触发客户端运行, 事件循环会被调用一次.
用于创建客户端的协程, 然后再次使用 客户端会收到 Future 实例, 用于在通信完成后进行通知.
像这样使用两次调用可以避免客户端程序陷入无限循环, 因为客户端在与服务器通信完成后通常需要退出.
如果只使用第一次调用来等待协程创建客户端, 则可能无法正确处理所有响应数据并清理与服务器的连接.
"""
log.debug("waiting for client to complete")
try:
    event_loop.run_until_complete(factory_coroutine)
    event_loop.run_until_complete(client_completed)
finally:
    log.debug("closing event loop")
    event_loop.close()

"""
$ python 23_2_asyncio_echo_client_protocol.py
asyncio: Using selector: EpollSelector
main: waiting for client to complete

EchoClient: connecting to ::1 port 10000
EchoClient: sending b'This is the message. '
EchoClient: sending b'It will be sent '
EchoClient: sending b'in parts.'

EchoClient: received b'This is the message. It will be sent in parts.'
EchoClient: received EOF

EchoClient: server closed connection

main: closing event loop

"""
