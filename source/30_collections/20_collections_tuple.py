#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Using a regular tuple"""

# end_pymotw_header
bob = ("Bob", 30, "male")
print("Representation:", bob)

jane = ("Jane", 29, "female")
print("\nField by index:", jane[0])

print("\nFields by index:")
for p in [bob, jane]:
    print("{} is a {} year old {}".format(*p))

"""
$ python 20_collections_tuple.py
Representation: ('Bob', 30, 'male')

Field by index: Jane

Fields by index:
Bob is a 30 year old male
Jane is a 29 year old female
$
"""
