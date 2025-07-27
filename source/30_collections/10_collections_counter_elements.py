#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Produce the elements of the counter."""

# end_pymotw_header
import collections

c = collections.Counter("extremely")
c["z"] = 0
print(c)
print(list(c.elements()))

"""
$ python 10_collections_counter_elements.py
Counter({'e': 3, 'x': 1, 't': 1, 'r': 1, 'm': 1, 'l': 1, 'y': 1, 'z': 0})
['e', 'e', 'e', 'x', 't', 'r', 'm', 'l', 'y']
$
"""
