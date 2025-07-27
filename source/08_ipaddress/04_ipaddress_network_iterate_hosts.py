#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2016 Doug Hellmann.  All rights reserved.
# Written for https://pymotw.com
#
""" """

# end_pymotw_header
import ipaddress

NETWORKS = [
    "10.9.0.0/24",
    "fdfd:87b5:b475:5e3e::/64",
]

for n in NETWORKS:
    net = ipaddress.ip_network(n)
    print("{!r}".format(net))
    for i, ip in zip(range(3), net.hosts()):
        print(ip)
    print()

"""
IPv4Network('10.9.0.0/24')
10.9.0.1
10.9.0.2
10.9.0.3

IPv6Network('fdfd:87b5:b475:5e3e::/64')
fdfd:87b5:b475:5e3e::1
fdfd:87b5:b475:5e3e::2
fdfd:87b5:b475:5e3e::3

"""
