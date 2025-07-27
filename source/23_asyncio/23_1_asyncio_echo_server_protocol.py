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
