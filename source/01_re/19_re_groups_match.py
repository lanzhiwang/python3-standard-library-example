#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Looking at groups on a match object"""

# end_pymotw_header
import re

text = "This is some text -- with punctuation."

print(text)
print()

patterns = [
    (r"^(\w+)", "word at start of string"),
    (r"(\w+)\S*$", "word at end, with optional punctuation"),
    (r"(\bt\w+)\W+(\w+)", "word starting with t, another word"),
    (r"(\w+t)\b", "word ending with t"),
]

for pattern, desc in patterns:
    regex = re.compile(pattern)
    match = regex.search(text)
    print("'{}' ({})\n".format(pattern, desc))
    print("  ", match.groups())
    print()

"""
huzhi@huzhideMacBook-Pro 01_re % python3 19_re_groups_match.py
This is some text -- with punctuation.

'^(\w+)' (word at start of string)

   ('This',)

'(\w+)\S*$' (word at end, with optional punctuation)

   ('punctuation',)

'(\bt\w+)\W+(\w+)' (word starting with t, another word)

   ('text', 'with')

'(\w+t)\b' (word ending with t)

   ('text',)

huzhi@huzhideMacBook-Pro 01_re %
"""
