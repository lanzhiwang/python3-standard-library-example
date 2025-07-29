#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Generate random numbers"""

# end_pymotw_header
import random

"""
random() produces different values each time it is called and has a very large period before it repeats any numbers.
This is useful for producing unique values or variations,
but there are times when having the same data set available to be processed in different ways is useful.
One technique is to use a program to generate random values and save them to be processed by a separate step.
That may not be practical for large amounts of data,
though, so random includes the seed() function for initializing the pseudorandom generator so that it produces an expected set of values.
random() 每次调用都会生成不同的值,
并且在重复任何数字之前都会有一段很长的周期.
这对于生成唯一值或变体非常有用, 但有时, 拥有相同的数据集以供不同的处理方式也很有用.
一种技术是使用程序生成随机值并保存它们, 以便由单独的步骤进行处理.
然而, 这对于大量数据来说可能并不实用, 因此 random 包含 seed() 函数来初始化伪随机生成器, 使其生成一组预期的值.

The seed value controls the first value produced by the formula used to produce pseudorandom numbers,
and since the formula is deterministic it also sets the full sequence produced after the seed is changed.
The argument to seed() can be any hashable object.
The default is to use a platform-specific source of randomness, if one is available. Otherwise, the current time is used.
种子值控制着用于生成伪随机数的公式生成的第一个值, 并且由于该公式是确定性的, 它还设置了种子更改后生成的完整序列.
seed() 的参数可以是任何可哈希的对象. 默认情况下, 如果存在平台特定的随机源, 则使用该源. 否则, 使用当前时间.
"""
random.seed(1)

for i in range(5):
    print("{:04.3f}".format(random.random()), end=" ")
print()

random.seed(2)

for i in range(5):
    print("{:04.3f}".format(random.random()), end=" ")
print()

"""
$ python 03_random_seed.py
0.134 0.847 0.764 0.255 0.495
0.956 0.948 0.057 0.085 0.835

$ python 03_random_seed.py
0.134 0.847 0.764 0.255 0.495
0.956 0.948 0.057 0.085 0.835

$ python 03_random_seed.py
0.134 0.847 0.764 0.255 0.495
0.956 0.948 0.057 0.085 0.835

$ python 03_random_seed.py
0.134 0.847 0.764 0.255 0.495
0.956 0.948 0.057 0.085 0.835
$
"""
