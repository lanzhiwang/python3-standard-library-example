#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Double-ended queue."""

# end_pymotw_header
import collections

d = collections.deque("abcdefg")
print("Deque:", d)
print("Length:", len(d))
print("Left end:", d[0])
print("Right end:", d[-1])

d.remove("c")
print("remove(c):", d)

"""
$ python 14_collections_deque.py
Deque: deque(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
Length: 7
Left end: a
Right end: g
remove(c): deque(['a', 'b', 'd', 'e', 'f', 'g'])
$
"""
