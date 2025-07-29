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
Some operating systems provide a random number generator that has access to more sources of entropy that can be introduced into the generator.
random exposes this feature through the SystemRandom class,
which has the same API as Random but uses os.urandom() to generate the values that form the basis of all of the other algorithms.
一些操作系统提供了一个 random 数生成器, 它可以访问更多可以引入生成器的熵源.
random 通过以下方式公开此功能: SystemRandom 类, 具有与 Random 相同的 API 但使用 os.urandom() 来生成构成所有其他算法基础的值.

Sequences produced by SystemRandom are not reproducible because the randomness is coming from the system,
rather than software state (in fact, seed() and setstate() have no effect at all).
SystemRandom 生成的序列是不可重现的, 因为随机性来自系统, 而不是软件状态(事实上, seed() 和 setstate() 根本没有效果).
"""

print("Default initializiation:\n")

r1 = random.SystemRandom()
r2 = random.SystemRandom()

for i in range(3):
    print("{:04.3f}  {:04.3f}".format(r1.random(), r2.random()))

print("\nSame seed:\n")

seed = time.time()
r1 = random.SystemRandom(seed)
r2 = random.SystemRandom(seed)

for i in range(3):
    print("{:04.3f}  {:04.3f}".format(r1.random(), r2.random()))
