#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""

#end_pymotw_header
import collections

Person = collections.namedtuple('Person', 'name age')

bob = Person(name='Bob', age=30)
print('Representation:', bob)
print('As Dictionary:', bob._asdict())

"""
$ python 26_collections_namedtuple_asdict.py
Representation: Person(name='Bob', age=30)
As Dictionary: {'name': 'Bob', 'age': 30}
$
"""
