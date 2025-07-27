#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
""" """

# end_pymotw_header
from urllib.parse import urlencode

query_args = {
    "foo": ["foo1", "foo2"],
}
print("Single  :", urlencode(query_args))
print("Sequence:", urlencode(query_args, doseq=True))

"""
Single  : foo=%5B%27foo1%27%2C+%27foo2%27%5D
Sequence: foo=foo1&foo=foo2
"""
