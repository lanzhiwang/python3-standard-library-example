#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Random values from a range"""

# end_pymotw_header
import random

"""
randrange() is a more general form of selecting values from a range.
randrange() 是从范围中选择值的更通用的形式.

randrange() supports a step argument,
in addition to start and stop values,
so it is fully equivalent to selecting a random value from range(start, stop, step).
It is more efficient, because the range is not actually constructed.
randrange() 除了起始值和终止值之外, 还支持 step 参数, 因此它完全等同于从 range(start, stop, step) 中选择一个随机值.
它效率更高, 因为实际上并未构建范围.
"""

for i in range(3):
    print(random.randrange(0, 101, 5), end=" ")
print()

"""
$ python 06_random_randrange.py
40 55 95
$ python 06_random_randrange.py
30 65 55
$ python 06_random_randrange.py
75 95 90
$
"""
