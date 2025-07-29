#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Generate random numbers"""

# end_pymotw_header
import random

for i in range(5):
    """
    The random() function returns the next random floating point value from the generated sequence.
    All of the return values fall within the range 0 <= n < 1.0.
    """
    print("%04.3f" % random.random(), end=" ")
print()

"""
Running the program repeatedly produces different sequences of numbers.
重复运行该程序会产生不同的数字序列.

$ python 01_random_random.py
0.672 0.656 0.077 0.350 0.558

$ python 01_random_random.py
0.817 0.867 0.674 0.471 0.302

$ python 01_random_random.py
0.900 0.560 0.253 0.173 0.866
$
"""
