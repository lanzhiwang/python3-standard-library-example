#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Looking for a specific group in a match"""

# end_pymotw_header
import re

text = "This is some text -- with punctuation."

print("Input text            :", text)

# word starting with 't' then another word
regex = re.compile(r"(\bt\w+)\W+(\w+)")
print("Pattern               :", regex.pattern)

match = regex.search(text)
print("Entire match          :", match.group(0))
print('Word starting with "t":', match.group(1))
print('Word after "t" word   :', match.group(2))

"""
huzhi@huzhideMacBook-Pro 01_re % python3 20_re_groups_individual.py
Input text            : This is some text -- with punctuation.
Pattern               : (\bt\w+)\W+(\w+)
Entire match          : text -- with
Word starting with "t": text
Word after "t" word   : with
huzhi@huzhideMacBook-Pro 01_re %
"""
