#!/usr/bin/env python3
"""Parsing URLs"""

# end_pymotw_header
from urllib.parse import urlparse, urlunparse

original = "http://netloc/path;?#"
print("ORIG  :", original)
parsed = urlparse(original)
print("PARSED:", type(parsed), parsed)
t = parsed[:]
print("TUPLE :", type(t), t)
print("NEW   :", urlunparse(t))

"""
ORIG  : http://netloc/path;?#
PARSED: <class 'urllib.parse.ParseResult'> ParseResult(scheme='http', netloc='netloc', path='/path', params='', query='', fragment='')
TUPLE : <class 'tuple'> ('http', 'netloc', '/path', '', '', '')
NEW   : http://netloc/path
"""
