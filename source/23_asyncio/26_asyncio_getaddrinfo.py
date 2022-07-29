#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2014 Doug Hellmann.  All rights reserved.
"""Converting hostnames to IP addresses
"""

#end_pymotw_header
import asyncio
import logging
import socket
import sys


TARGETS = [
    ('pymotw.com', 'https'),
    ('doughellmann.com', 'https'),
    ('python.org', 'https'),
]


async def main(loop, targets):
    for target in targets:
        info = await loop.getaddrinfo(
            *target,
            proto=socket.IPPROTO_TCP,
        )

        for host in info:
            print('{:20}: {}'.format(target[0], host[4][0]))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop, TARGETS))
finally:
    event_loop.close()

"""
pymotw.com          : 185.199.111.153
pymotw.com          : 185.199.110.153
pymotw.com          : 185.199.109.153
pymotw.com          : 185.199.108.153
pymotw.com          : 2606:50c0:8003::153
pymotw.com          : 2606:50c0:8001::153
pymotw.com          : 2606:50c0:8002::153
pymotw.com          : 2606:50c0:8000::153
doughellmann.com    : 75.2.60.5
python.org          : 138.197.63.241
"""