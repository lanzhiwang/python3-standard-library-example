#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Generating random integers."""

# end_pymotw_header
import random

"""
random() generates floating point numbers.
It is possible to convert the results to integers,
but using randint() to generate integers directly is more convenient.
random() 生成浮点数. 可以将结果转换为整数, 但使用 randint() 直接生成整数更为方便.

The arguments to randint() are the ends of the inclusive range for the values.
The numbers can be positive or negative, but the first value should be less than the second.
randint() 的参数是数值包含范围的两端. 数值可以是正数或负数, 但第一个值必须小于第二个值.

"""
print("[1, 100]:", end=" ")

for i in range(3):
    print(random.randint(1, 100), end=" ")

print("\n[-5, 5]:", end=" ")
for i in range(3):
    print(random.randint(-5, 5), end=" ")
print()

"""
$ python 05_random_randint.py
[1, 100]: 76 80 48
[-5, 5]: -2 3 1

$ python 05_random_randint.py
[1, 100]: 36 52 18
[-5, 5]: 3 -3 4

$ python 05_random_randint.py
[1, 100]: 25 13 88
[-5, 5]: -4 3 2

$ python 05_random_randint.py
[1, 100]: 94 25 30
[-5, 5]: 1 4 0
$
"""
