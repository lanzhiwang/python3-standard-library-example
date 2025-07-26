#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""

#end_pymotw_header
import collections

try:
    collections.namedtuple('Person', 'name class age')
except ValueError as err:
    print(err)

try:
    collections.namedtuple('Person', 'name age age')
except ValueError as err:
    print(err)

"""
$ python 23_collections_namedtuple_bad_fields.py
Type names and field names cannot be a keyword: 'class'
Encountered duplicate field name: 'age'
$
"""
