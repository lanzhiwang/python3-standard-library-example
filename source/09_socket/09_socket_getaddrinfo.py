#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Get address info for a service"""

# end_pymotw_header
import socket


def get_constants(prefix):
    """Create a dictionary mapping socket module
    constants to their names.
    """
    return {getattr(socket, n): n for n in dir(socket) if n.startswith(prefix)}


families = get_constants("AF_")
print(families)
print()
types = get_constants("SOCK_")
print(types)
print()
protocols = get_constants("IPPROTO_")
print(protocols)
print()

for response in socket.getaddrinfo("www.python.org", "http"):

    # Unpack the response tuple
    family, socktype, proto, canonname, sockaddr = response

    print("Family        :", families[family])
    print("Type          :", types[socktype])
    print("Protocol      :", protocols[proto])
    print("Canonical name:", canonname)
    print("Socket address:", sockaddr)
    print()

"""
{<AddressFamily.AF_APPLETALK: 16>: 'AF_APPLETALK', 12: 'AF_DECnet', 
<AddressFamily.AF_INET: 2>: 'AF_INET', <AddressFamily.AF_INET6: 30>: 'AF_INET6', 
<AddressFamily.AF_IPX: 23>: 'AF_IPX', <AddressFamily.AF_LINK: 18>: 'AF_LINK', 
<AddressFamily.AF_ROUTE: 17>: 'AF_ROUTE', <AddressFamily.AF_SNA: 11>: 'AF_SNA', 
<AddressFamily.AF_SYSTEM: 32>: 'AF_SYSTEM', <AddressFamily.AF_UNIX: 1>: 'AF_UNIX', 
<AddressFamily.AF_UNSPEC: 0>: 'AF_UNSPEC'}

{<SocketKind.SOCK_DGRAM: 2>: 'SOCK_DGRAM', <SocketKind.SOCK_RAW: 3>: 'SOCK_RAW', 
<SocketKind.SOCK_RDM: 4>: 'SOCK_RDM', <SocketKind.SOCK_SEQPACKET: 5>: 'SOCK_SEQPACKET', 
<SocketKind.SOCK_STREAM: 1>: 'SOCK_STREAM'}

{51: 'IPPROTO_AH', 60: 'IPPROTO_DSTOPTS', 8: 'IPPROTO_EGP', 80: 'IPPROTO_EON', 50: 'IPPROTO_ESP', 
44: 'IPPROTO_FRAGMENT', 3: 'IPPROTO_GGP', 47: 'IPPROTO_GRE', 63: 'IPPROTO_HELLO', 0: 'IPPROTO_IP', 
1: 'IPPROTO_ICMP', 58: 'IPPROTO_ICMPV6', 22: 'IPPROTO_IDP', 2: 'IPPROTO_IGMP', 108: 'IPPROTO_IPCOMP', 
4: 'IPPROTO_IPV4', 41: 'IPPROTO_IPV6', 256: 'IPPROTO_MAX', 77: 'IPPROTO_ND', 59: 'IPPROTO_NONE', 
103: 'IPPROTO_PIM', 12: 'IPPROTO_PUP', 255: 'IPPROTO_RAW', 43: 'IPPROTO_ROUTING', 46: 'IPPROTO_RSVP', 
132: 'IPPROTO_SCTP', 6: 'IPPROTO_TCP', 29: 'IPPROTO_TP', 17: 'IPPROTO_UDP', 36: 'IPPROTO_XTP'}

Family        : AF_INET
Type          : SOCK_DGRAM
Protocol      : IPPROTO_UDP
Canonical name:
Socket address: ('151.101.228.223', 80)

Family        : AF_INET
Type          : SOCK_STREAM
Protocol      : IPPROTO_TCP
Canonical name:
Socket address: ('151.101.228.223', 80)

"""
