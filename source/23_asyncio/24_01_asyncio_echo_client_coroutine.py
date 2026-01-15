#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2014 Doug Hellmann.  All rights reserved.
"""Echo client using coroutines"""

# end_pymotw_header
import asyncio
import logging
import sys

MESSAGES = [
    b"This is the message. ",
    b"It will be sent ",
    b"in parts.",
]
SERVER_ADDRESS = ("127.0.0.1", 10000)


async def echo_client(address, messages):

    log = logging.getLogger("echo_client")

    log.debug("connecting to {} port {}".format(*address))
    reader, writer = await asyncio.open_connection(*address)

    # This could be writer.writelines() except that
    # would make it harder to show each part of the message
    # being sent.
    for msg in messages:
        writer.write(msg)
        log.debug("sending {!r}".format(msg))
    if writer.can_write_eof():
        writer.write_eof()
    await writer.drain()

    log.debug("waiting for response")
    while True:
        data = await reader.read(128)
        if data:
            log.debug("received {!r}".format(data))
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

try:
    event_loop.run_until_complete(echo_client(SERVER_ADDRESS, MESSAGES))
finally:
    log.debug("closing event loop")
    event_loop.close()

"""
$ python 24_01_asyncio_echo_client_coroutine.py
asyncio: Using selector: EpollSelector
echo_client: connecting to 127.0.0.1 port 10000
echo_client: sending b'This is the message. '
echo_client: sending b'It will be sent '
echo_client: sending b'in parts.'
echo_client: waiting for response
echo_client: received b'This is the message. It will be sent in parts.'
echo_client: closing
main: closing event loop
$
"""
