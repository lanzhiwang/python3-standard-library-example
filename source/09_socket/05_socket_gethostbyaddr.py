#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Look up a hostname from its address."""

# end_pymotw_header
import socket

hostname, aliases, addresses = socket.gethostbyaddr("151.101.228.223")

print("Hostname :", hostname)
print("Aliases  :", aliases)
print("Addresses:", addresses)
