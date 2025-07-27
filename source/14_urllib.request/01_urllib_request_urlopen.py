#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Simple example with urllib2.urlopen()."""

# end_pymotw_header
from urllib import request

response = request.urlopen("http://localhost:8080/")
print("RESPONSE:", response)
print("URL     :", response.geturl())

headers = response.info()
print("DATE    :", headers["date"])
print("HEADERS :")
print("---------")
print(headers)

data = response.read().decode("utf-8")
print("LENGTH  :", len(data))
print("DATA    :")
print("---------")
print(data)

"""
RESPONSE: <http.client.HTTPResponse object at 0x1054b3da0>
URL     : http://localhost:8080/
DATE    : Fri, 21 Feb 2020 08:54:14 GMT
HEADERS :
---------
Server: BaseHTTP/0.6 Python/3.7.3
Date: Fri, 21 Feb 2020 08:54:14 GMT
Content-Type: text/plain; charset=utf-8


LENGTH  : 349
DATA    :
---------
CLIENT VALUES:
client_address=('127.0.0.1', 52543) (127.0.0.1)
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
