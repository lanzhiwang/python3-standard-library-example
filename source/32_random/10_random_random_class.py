#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Random class."""

# end_pymotw_header
import random
import time

"""
In addition to module-level functions,
random includes a Random class to manage the internal state for several random number generators.
All of the functions described earlier are available as methods of the Random instances,
and each instance can be initialized and used separately,
without interfering with the values returned by other instances.
除了模块级函数外, random 还包含一个 Random 类用于管理多个随机数生成器的内部状态.
前面描述的所有函数都可以作为 Random 实例的方法使用, 并且每个实例都可以单独初始化和使用, 而不会干扰其他实例的返回值.
"""

print("Default initializiation:\n")

r1 = random.Random()
r2 = random.Random()

for i in range(3):
    print("{:04.3f}  {:04.3f}".format(r1.random(), r2.random()))

print("\nSame seed:\n")

seed = time.time()
r1 = random.Random(seed)
r2 = random.Random(seed)

for i in range(3):
    print("{:04.3f}  {:04.3f}".format(r1.random(), r2.random()))

"""
$ python 10_random_random_class.py
Default initializiation:

0.442  0.905
0.461  0.902
0.293  1.000

Same seed:

0.669  0.669
0.876  0.876
0.219  0.219
$
$ python 10_random_random_class.py
Default initializiation:

0.858  0.895
0.901  0.262
0.499  0.513

Same seed:

0.840  0.840
0.314  0.314
0.439  0.439
$
"""
