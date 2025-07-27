#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Client half of echo example"""

# end_pymotw_header
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port on the server
# given by the caller
server_address = (sys.argv[1], 10000)
print("connecting to {} port {}".format(*server_address))
sock.connect(server_address)

try:

    message = b"This is the message.  It will be repeated."
    print("sending {!r}".format(message))
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print("received {!r}".format(data))

finally:
    sock.close()
