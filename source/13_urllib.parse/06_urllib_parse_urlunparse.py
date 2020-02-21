#!/usr/bin/env python3
"""Parsing URLs
"""

#end_pymotw_header
from urllib.parse import urlparse, urlunparse

original = 'http://netloc/path;param?query=arg#frag'
print('ORIG  :', original)
parsed = urlparse(original)
print('PARSED:', type(parsed), parsed)
t = parsed[:]
print('TUPLE :', type(t), t)
print('NEW   :', urlunparse(t))

"""
ORIG  : http://netloc/path;param?query=arg#frag
PARSED: <class 'urllib.parse.ParseResult'> ParseResult(scheme='http', netloc='netloc', path='/path', params='param', query='query=arg', fragment='frag')
TUPLE : <class 'tuple'> ('http', 'netloc', '/path', 'param', 'query=arg', 'frag')
NEW   : http://netloc/path;param?query=arg#frag
"""