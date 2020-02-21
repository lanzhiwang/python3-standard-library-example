#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Convert hostname to IP address.
"""

#end_pymotw_header
import socket

HOSTS = [
    'apu',
    'pymotw.com',
    'www.python.org',
    'nosuchname',
]

for host in HOSTS:
    try:
        print('{} : {}'.format(host, socket.gethostbyname(host)))
    except socket.error as msg:
        print('{} : {}'.format(host, msg))

"""
apu : [Errno 8] nodename nor servname provided, or not known
pymotw.com : 66.33.211.242
www.python.org : 151.101.228.223
nosuchname : [Errno 8] nodename nor servname provided, or not known
"""