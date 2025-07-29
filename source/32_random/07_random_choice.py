#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Random choice"""

# end_pymotw_header
import random

"""
One common use for random number generators is to select a random item from a sequence of enumerated values,
even if those values are not numbers.
random includes the choice() function for making a random selection from a sequence.
This example simulates flipping a coin 10,000 times to count how many times it comes up heads and how many times tails.
随机数生成器的一个常见用途是从枚举值序列中随机选择一个项, 即使这些值不是数字.
random 包含 random choice() 函数, 用于从序列中进行随机选择.
此示例模拟抛硬币 10,000 次, 以计算正面朝上的次数和反面朝上的次数.

There are only two outcomes allowed,
so rather than use numbers and convert them the words "heads" and "tails" are used with choice().
The results are tabulated in a dictionary using the outcome names as keys.
只允许两种结果, 因此不要使用数字和 将它们转换为"头"和"尾"的单词 choice(). 结果以结果名称作为键, 列在字典中.
"""

outcomes = {
    "heads": 0,
    "tails": 0,
}
sides = list(outcomes.keys())

for i in range(10000):
    outcomes[random.choice(sides)] += 1

print("Heads:", outcomes["heads"])
print("Tails:", outcomes["tails"])

"""
$ python 07_random_choice.py
Heads: 4997
Tails: 5003

$ python 07_random_choice.py
Heads: 5046
Tails: 4954

$ python 07_random_choice.py
Heads: 4975
Tails: 5025
$
"""
