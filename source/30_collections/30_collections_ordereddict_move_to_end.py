#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Re-ordering an OrderedDict"""

# end_pymotw_header
import collections

d = collections.OrderedDict([("a", "A"), ("b", "B"), ("c", "C")])

print("Before:")
for k, v in d.items():
    print(k, v)

d.move_to_end("b")

print("\nmove_to_end():")
for k, v in d.items():
    print(k, v)

d.move_to_end("b", last=False)

print("\nmove_to_end(last=False):")
for k, v in d.items():
    print(k, v)

"""
$ python 30_collections_ordereddict_move_to_end.py
Before:
a A
b B
c C

move_to_end():
a A
c C
b B

move_to_end(last=False):
b B
a A
c C
$
"""
