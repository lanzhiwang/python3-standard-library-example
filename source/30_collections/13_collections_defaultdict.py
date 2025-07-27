#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Initializing a defaultdict."""

# end_pymotw_header
import collections


def default_factory():
    return "default value"


d = collections.defaultdict(default_factory, foo="bar")
print("d:", d)
print("foo =>", d["foo"])
print("bar =>", d["bar"])
print("d:", d)

"""
$ python 13_collections_defaultdict.py
d: defaultdict(<function default_factory at 0x7fac3da76f80>, {'foo': 'bar'})
foo => bar
bar => default value
d: defaultdict(<function default_factory at 0x7fac3da76f80>, {'foo': 'bar', 'bar': 'default value'})
$
"""
