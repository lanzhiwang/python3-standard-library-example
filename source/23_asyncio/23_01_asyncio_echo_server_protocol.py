#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2014 Doug Hellmann.  All rights reserved.
"""TCP echo server using asyncio with a Protocol class."""

# end_pymotw_header
import asyncio
import logging
import sys

SERVER_ADDRESS = ("127.0.0.1", 10000)


class EchoServer(asyncio.Protocol):

    def connection_made(self, transport):
        self.transport = transport
        self.address = transport.get_extra_info("peername")
        self.log = logging.getLogger("EchoServer_{}_{}".format(*self.address))
        self.log.debug("connection accepted")

    def data_received(self, data):
        self.log.debug("received {!r}".format(data))
        self.transport.write(data)
        self.log.debug("sent {!r}".format(data))

    def eof_received(self):
        self.log.debug("received EOF")
        if self.transport.can_write_eof():
            self.transport.write_eof()

    def connection_lost(self, error):
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

# Create the server and let the loop finish the coroutine before
# starting the real event loop.
factory = event_loop.create_server(EchoServer, *SERVER_ADDRESS)
server = event_loop.run_until_complete(factory)
log.debug("starting up on {} port {}".format(*SERVER_ADDRESS))

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
$ python --version
Python 3.10.18
$

$ python 23_01_asyncio_echo_server_protocol.py
asyncio: Using selector: EpollSelector
main: starting up on 127.0.0.1 port 10000
EchoServer_127.0.0.1_51336: connection accepted
EchoServer_127.0.0.1_51336: received b'This is the message. It will be sent in parts.'
EchoServer_127.0.0.1_51336: sent b'This is the message. It will be sent in parts.'
EchoServer_127.0.0.1_51336: received EOF
EchoServer_127.0.0.1_51336: closing

^Cmain: closing server
main: closing event loop
Traceback (most recent call last):
  File "/python3-standard-library-example/source/23_asyncio/23_01_asyncio_echo_server_protocol.py", line 58, in <module>
    event_loop.run_forever()
  File "/usr/local/lib/python3.10/asyncio/base_events.py", line 603, in run_forever
    self._run_once()
  File "/usr/local/lib/python3.10/asyncio/base_events.py", line 1871, in _run_once
    event_list = self._selector.select(timeout)
  File "/usr/local/lib/python3.10/selectors.py", line 469, in select
    fd_event_list = self._selector.poll(timeout, max_ev)
KeyboardInterrupt

$

"""
