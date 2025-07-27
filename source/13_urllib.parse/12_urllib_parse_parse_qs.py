#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
""" """

# end_pymotw_header
from urllib.parse import parse_qs, parse_qsl

encoded = "foo=foo1&foo=foo2"

print("parse_qs :", parse_qs(encoded))
print("parse_qsl:", parse_qsl(encoded))

"""
parse_qs : {'foo': ['foo1', 'foo2']}
parse_qsl: [('foo', 'foo1'), ('foo', 'foo2')]
"""
