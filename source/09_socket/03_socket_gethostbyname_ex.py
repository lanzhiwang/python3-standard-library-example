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
    print(host)
    try:
        name, aliases, addresses = socket.gethostbyname_ex(host)
        print('  Hostname:', name)
        print('  Aliases :', aliases)
        print(' Addresses:', addresses)
    except socket.error as msg:
        print('ERROR:', msg)
    print()

"""
apu
ERROR: [Errno 8] nodename nor servname provided, or not known

pymotw.com
  Hostname: pymotw.com
  Aliases : []
 Addresses: ['66.33.211.242']

www.python.org
  Hostname: dualstack.python.map.fastly.net
  Aliases : ['www.python.org']
 Addresses: ['151.101.228.223']

nosuchname
ERROR: [Errno 8] nodename nor servname provided, or not known

"""