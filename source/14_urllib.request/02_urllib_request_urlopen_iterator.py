#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Simple example with urllib.urlopen()."""

# end_pymotw_header
from urllib import request

response = request.urlopen("http://localhost:8080/")
for line in response:
    print(line.decode("utf-8").rstrip())

"""
CLIENT VALUES:
client_address=('127.0.0.1', 52554) (127.0.0.1)
command=GET
path=/
real path=/
query=
request_version=HTTP/1.1

SERVER VALUES:
server_version=BaseHTTP/0.6
sys_version=Python/3.7.3
protocol_version=HTTP/1.0

HEADERS RECEIVED:
Accept-Encoding=identity
Connection=close
Host=localhost:8080
User-Agent=Python-urllib/3.7
"""
