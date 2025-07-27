#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
""" """

# end_pymotw_header
import collections

Person = collections.namedtuple("Person", "name age")

pat = Person(name="Pat", age=12)
print("\nRepresentation:", pat)

pat.age = 21

"""
$ python 22_collections_namedtuple_immutable.py

Representation: Person(name='Pat', age=12)
Traceback (most recent call last):
  File "/python3-standard-library-example/source/30_collections/22_collections_namedtuple_immutable.py", line 17, in <module>
    pat.age = 21
AttributeError: can't set attribute
$
"""
