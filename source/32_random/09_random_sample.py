#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Sampling from sequences"""

# end_pymotw_header
import random

with open("./words", "rt") as f:
    words = f.readlines()
words = [w.rstrip() for w in words]
print("words:", words)

for w in random.sample(words, 5):
    print(w)

"""
$ python 09_random_sample.py
words: ['A', 'a', 'aa', 'aal', 'aalii', 'aam', 'Aani', 'aardvark', 'aardwolf', 'Aaron', 'Aaronic', 'Aaronical', 'Aaronite', 'Aaronitic', 'Aaru', 'Ab', 'aba', 'Ababdeh', 'Ababua', 'abac', 'abaca', 'abacate', 'abacay', 'abacinate']
abacay
aam
Ababdeh
Aaru
Aaronical
$
$ python 09_random_sample.py
words: ['A', 'a', 'aa', 'aal', 'aalii', 'aam', 'Aani', 'aardvark', 'aardwolf', 'Aaron', 'Aaronic', 'Aaronical', 'Aaronite', 'Aaronitic', 'Aaru', 'Ab', 'aba', 'Ababdeh', 'Ababua', 'abac', 'abaca', 'abacate', 'abacay', 'abacinate']
Aaronitic
aardwolf
a
abacinate
abac
$
"""
