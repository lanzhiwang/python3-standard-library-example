#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2016 Doug Hellmann.  All rights reserved.
# Written for https://pymotw.com
#
""" """

# end_pymotw_header
import ipaddress


ADDRESSES = [
    "10.9.0.6/24",
    "fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa/64",
]


for ip in ADDRESSES:
    iface = ipaddress.ip_interface(ip)
    print("{!r}".format(iface))
    print("network:\n  ", iface.network)
    print("ip:\n  ", iface.ip)
    print("IP with prefixlen:\n  ", iface.with_prefixlen)
    print("netmask:\n  ", iface.with_netmask)
    print("hostmask:\n  ", iface.with_hostmask)
    print()

"""
IPv4Interface('10.9.0.6/24')
network:
   10.9.0.0/24
ip:
   10.9.0.6
IP with prefixlen:
   10.9.0.6/24
netmask:
   10.9.0.6/255.255.255.0
hostmask:
   10.9.0.6/0.0.0.255

IPv6Interface('fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa/64')
network:
   fdfd:87b5:b475:5e3e::/64
ip:
   fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa
IP with prefixlen:
   fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa/64
netmask:
   fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa/ffff:ffff:ffff:ffff::
hostmask:
   fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa/::ffff:ffff:ffff:ffff

"""
