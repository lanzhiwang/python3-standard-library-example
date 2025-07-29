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
    To generate numbers in a specific numerical range, use uniform() instead.
    要生成特定数值范围内的数字, 请使用 uniform() 反而.

    Pass minimum and maximum values,
    and uniform() adjusts the return values from random() using the formula min + (max - min) * random().
    传递最小值和最大值,  uniform() 使用公式 min + (max - min) * random() 调整 random() () 的返回值.
    """
    print("{:04.3f}".format(random.uniform(1, 100)), end=" ")
print()

"""
$ python 02_random_uniform.py
99.661 74.516 32.392 12.312 86.012
$ python 02_random_uniform.py
9.054 79.037 12.853 18.468 27.275
$ python 02_random_uniform.py
16.735 6.694 11.922 28.751 77.354
$ python 02_random_uniform.py
5.569 90.662 16.641 64.485 48.618
$
"""
