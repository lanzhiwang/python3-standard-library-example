#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Lookup the constant for a named protocol.
"""

#end_pymotw_header
import socket


def get_constants(prefix):
    """Create a dictionary mapping socket module
    constants to their names.
    """
    return {
        getattr(socket, n): n
        for n in dir(socket)
        if n.startswith(prefix)
    }


protocols = get_constants('IPPROTO_')
print(protocols)

for name in ['icmp', 'udp', 'tcp']:
    proto_num = socket.getprotobyname(name)
    const_name = protocols[proto_num]
    print('{:>4} -> {:2d} (socket.{:<12} = {:2d})'.format(
        name, proto_num, const_name,
        getattr(socket, const_name)))

"""
{
51: 'IPPROTO_AH', 60: 'IPPROTO_DSTOPTS', 8: 'IPPROTO_EGP', 80: 'IPPROTO_EON', 
50: 'IPPROTO_ESP', 44: 'IPPROTO_FRAGMENT', 3: 'IPPROTO_GGP', 47: 'IPPROTO_GRE', 
63: 'IPPROTO_HELLO', 0: 'IPPROTO_IP', 1: 'IPPROTO_ICMP', 58: 'IPPROTO_ICMPV6', 
22: 'IPPROTO_IDP', 2: 'IPPROTO_IGMP', 108: 'IPPROTO_IPCOMP', 4: 'IPPROTO_IPV4', 
41: 'IPPROTO_IPV6', 256: 'IPPROTO_MAX', 77: 'IPPROTO_ND', 59: 'IPPROTO_NONE', 
103: 'IPPROTO_PIM', 12: 'IPPROTO_PUP', 255: 'IPPROTO_RAW', 43: 'IPPROTO_ROUTING', 
46: 'IPPROTO_RSVP', 132: 'IPPROTO_SCTP', 6: 'IPPROTO_TCP', 29: 'IPPROTO_TP', 
17: 'IPPROTO_UDP', 36: 'IPPROTO_XTP'}

icmp ->  1 (socket.IPPROTO_ICMP =  1)
 udp -> 17 (socket.IPPROTO_UDP  = 17)
 tcp ->  6 (socket.IPPROTO_TCP  =  6)
"""