#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2016 Doug Hellmann.  All rights reserved.
# Written for https://pymotw.com
#
""" """

# end_pymotw_header
import binascii
import ipaddress


ADDRESSES = [
    "10.9.0.6",
    "fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa",
]

for ip in ADDRESSES:
    addr = ipaddress.ip_address(ip)
    print("{!r}".format(addr))
    print("   IP version:", addr.version)
    print("   is private:", addr.is_private)
    print("  packed form:", binascii.hexlify(addr.packed))
    print("      integer:", int(addr))
    print()

"""
IPv4Address('10.9.0.6')
   IP version: 4
   is private: True
  packed form: b'0a090006'
      integer: 168361990

IPv6Address('fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa')
   IP version: 6
   is private: True
  packed form: b'fdfd87b5b4755e3eb1bce121a8eb14aa'
      integer: 337611086560236126439725644408160982186

"""
