#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Count the most common letters in words."""

# end_pymotw_header
import collections

c = collections.Counter()
with open("../words", "rt") as f:
    for line in f:
        print("line:", line)
        print(line.rstrip().lower())
        c.update(line.rstrip().lower())

print("c:", c)

print("Most common:")
for letter, count in c.most_common(3):
    print("{}: {:>7}".format(letter, count))

"""
$ python 11_collections_counter_most_common.py
line: A

a
line: a

a
line: aa

aa
line: aal

aal
line: aalii

aalii
line: aam

aam
line: Aani

aani
line: aardvark

aardvark
line: aardwolf

aardwolf
line: Aaron

aaron
line: Aaronic

aaronic
line: Aaronical

aaronical
line: Aaronite

aaronite
line: Aaronitic

aaronitic
line: Aaru

aaru
line: Ab

ab
line: aba

aba
line: Ababdeh

ababdeh
line: Ababua
ababua
c: Counter({'a': 38, 'r': 9, 'i': 8, 'n': 6, 'o': 6, 'b': 6, 'l': 4, 'd': 3, 'c': 3, 't': 2, 'e': 2, 'u': 2, 'm': 1, 'v': 1, 'k': 1, 'w': 1, 'f': 1, 'h': 1})
Most common:
a:      38
r:       9
i:       8
$
"""
