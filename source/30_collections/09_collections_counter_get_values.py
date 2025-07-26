#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Updating counts.
"""

#end_pymotw_header
import collections

c = collections.Counter('abcdaab')

for letter in 'abcde':
    print('{} : {}'.format(letter, c[letter]))

"""
$ python 09_collections_counter_get_values.py
a : 3
b : 2
c : 1
d : 1
e : 0
$
"""
