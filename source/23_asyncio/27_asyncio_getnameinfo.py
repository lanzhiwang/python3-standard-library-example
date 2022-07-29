#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2014 Doug Hellmann.  All rights reserved.
"""IP addresses and port numbers to host and protocol names
"""

#end_pymotw_header
import asyncio
import logging
import socket
import sys


TARGETS = [
    ('66.33.211.242', 443),
    ('104.130.43.121', 443),
]


async def main(loop, targets):
    for target in targets:
        info = await loop.getnameinfo(target)
        print('{:15}: {} {}'.format(target[0], *info))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop, TARGETS))
finally:
    event_loop.close()

"""
66.33.211.242  : apache2-zoo.george-washington.dreamhost.com https
Traceback (most recent call last):
  File "27_asyncio_getnameinfo.py", line 29, in <module>
    event_loop.run_until_complete(main(event_loop, TARGETS))
  File "/usr/local/lib/python3.8/asyncio/base_events.py", line 616, in run_until_complete
    return future.result()
  File "27_asyncio_getnameinfo.py", line 23, in main
    info = await loop.getnameinfo(target)
  File "/usr/local/lib/python3.8/asyncio/base_events.py", line 829, in getnameinfo
    return await self.run_in_executor(
  File "/usr/local/lib/python3.8/concurrent/futures/thread.py", line 57, in run
    result = self.fn(*self.args, **self.kwargs)
socket.gaierror: [Errno -3] Temporary failure in name resolution
"""