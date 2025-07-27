#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2014 Doug Hellmann.  All rights reserved.
"""TCP echo server using asyncio with coroutines."""

# end_pymotw_header
import asyncio
import logging
import sys

SERVER_ADDRESS = ("localhost", 10000)


async def echo(reader, writer):
    address = writer.get_extra_info("peername")
    log = logging.getLogger("echo_{}_{}".format(*address))
    log.debug("connection accepted")
    while True:
        data = await reader.read(128)
        if data:
            log.debug("received {!r}".format(data))
            writer.write(data)
            await writer.drain()
            log.debug("sent {!r}".format(data))
        else:
            log.debug("closing")
            writer.close()
            return


logging.basicConfig(
    level=logging.DEBUG,
    format="%(name)s: %(message)s",
    stream=sys.stderr,
)
log = logging.getLogger("main")

event_loop = asyncio.get_event_loop()
# event_loop.set_debug(True)

# Create the server and let the loop finish the coroutine before
# starting the real event loop.
factory = asyncio.start_server(echo, *SERVER_ADDRESS)
server = event_loop.run_until_complete(factory)
log.debug("starting up on {} port {}".format(*SERVER_ADDRESS))

# Enter the event loop permanently to handle all connections.
try:
    event_loop.run_forever()
except KeyboardInterrupt:
    # pass
    log.debug("KeyboardInterrupt")
finally:
    log.debug("closing server")
    server.close()
    event_loop.run_until_complete(server.wait_closed())
    log.debug("closing event loop")
    event_loop.close()

"""
$ python 24_1_asyncio_echo_server_coroutine.py
asyncio: Using selector: EpollSelector
main: starting up on localhost port 10000

echo_::1_62100: connection accepted
echo_::1_62100: received b'This is the message. It will be sent in parts.'
echo_::1_62100: sent b'This is the message. It will be sent in parts.'
echo_::1_62100: closing

^Cmain: KeyboardInterrupt
main: closing server
main: closing event loop

"""
