#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Repetition of patterns"""

# end_pymotw_header
import re

text = "abbaaabbbbaaaaa"

pattern = "ab"

for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print("Found {!r} at {:d}:{:d}".format(text[s:e], s, e))

"""
huzhi@huzhideMacBook-Pro 01_re % python3 04_re_finditer.py
Found 'ab' at 0:2
Found 'ab' at 5:7
huzhi@huzhideMacBook-Pro 01_re %
"""
