#!/usr/bin/env python3
"""Parsing URLs"""
# flake8: noqa

# end_pymotw_header
from urllib.parse import urlsplit

url = "http://user:pwd@NetLoc:80/p1;para/p2;para?query=arg#frag"
parsed = urlsplit(url)
print(parsed)
print("scheme  :", parsed.scheme)
print("netloc  :", parsed.netloc)
print("path    :", parsed.path)
print("query   :", parsed.query)
print("fragment:", parsed.fragment)
print("username:", parsed.username)
print("password:", parsed.password)
print("hostname:", parsed.hostname)
print("port    :", parsed.port)

"""
SplitResult(scheme='http', netloc='user:pwd@NetLoc:80', path='/p1;para/p2;para', query='query=arg', fragment='frag')
scheme  : http
netloc  : user:pwd@NetLoc:80
path    : /p1;para/p2;para
query   : query=arg
fragment: frag
username: user
password: pwd
hostname: netloc
port    : 80
"""
