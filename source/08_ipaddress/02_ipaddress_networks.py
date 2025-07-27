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
    print("     is private:", net.is_private)
    print("      broadcast:", net.broadcast_address)
    print("     compressed:", net.compressed)
    print("   with netmask:", net.with_netmask)
    print("  with hostmask:", net.with_hostmask)
    print("  num addresses:", net.num_addresses)
    print()

"""
IPv4Network('10.9.0.0/24')
     is private: True
      broadcast: 10.9.0.255
     compressed: 10.9.0.0/24
   with netmask: 10.9.0.0/255.255.255.0
  with hostmask: 10.9.0.0/0.0.0.255
  num addresses: 256

IPv6Network('fdfd:87b5:b475:5e3e::/64')
     is private: True
      broadcast: fdfd:87b5:b475:5e3e:ffff:ffff:ffff:ffff
     compressed: fdfd:87b5:b475:5e3e::/64
   with netmask: fdfd:87b5:b475:5e3e::/ffff:ffff:ffff:ffff::
  with hostmask: fdfd:87b5:b475:5e3e::/::ffff:ffff:ffff:ffff
  num addresses: 18446744073709551616

"""
