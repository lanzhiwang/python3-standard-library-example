#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2014 Doug Hellmann.  All rights reserved.
"""IP addresses and port numbers to host and protocol names"""

# end_pymotw_header
import asyncio
import logging
import socket
import sys


TARGETS = [
    ("185.199.109.153", 443),
    ("151.101.128.223", 443),
]


async def main(loop, targets):
    for target in targets:
        info = await loop.getnameinfo(target)
        print("{:15}: {} {}".format(target[0], *info))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop, TARGETS))
finally:
    event_loop.close()

"""
$ python 27_asyncio_getnameinfo.py
185.199.109.153: cdn-185-199-109-153.github.com https
151.101.128.223: 151.101.128.223 https
$
"""
