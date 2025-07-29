#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Save and restore state"""

# end_pymotw_header

"""
The internal state of the pseudorandom algorithm used by random() can be saved and used to control the numbers produced in subsequent runs.
Restoring the previous state before continuing reduces the likelihood of repeating values or sequences of values from the earlier input.
The getstate() function returns data that can be used to re-initialize the random number generator later with setstate().
使用的伪随机算法的内部状态 random() 可以保存并用于控制后续运行产生的数字.
在继续之前恢复先前的状态可以降低重复先前输入的值或值序列的可能性.
getstate() 函数返回的数据 稍后可用于重新初始化随机数生成器 setstate().

The data returned by getstate() is an implementation detail,
so this example saves the data to a file with pickle but otherwise treats it as a black box.
If the file exists when the program starts,
it loads the old state and continues.
Each run produces a few numbers before and after saving the state,
to show that restoring the state causes the generator to produce the same values again.
getstate() 返回的数据是一个实现细节, 因此本示例使用 pickle 将数据保存到文件中,
但除此之外, 将其视为黑盒. 如果程序启动时该文件存在, 它将加载旧状态并继续运行.
每次运行都会在保存状态之前和之后生成一些数字, 以表明恢复状态会导致生成器再次生成相同的值.
"""

import random
import os
import pickle

if os.path.exists("state.dat"):
    # Restore the previously saved state
    print("Found state.dat, initializing random module")
    with open("state.dat", "rb") as f:
        state = pickle.load(f)
    random.setstate(state)
else:
    # Use a well-known start state
    print("No state.dat, seeding")
    random.seed(1)

# Produce random values
for i in range(3):
    print("{:04.3f}".format(random.random()), end=" ")
print()

# Save state for next time
with open("state.dat", "wb") as f:
    pickle.dump(random.getstate(), f)

# Produce more random values
print("\nAfter saving state:")
for i in range(3):
    print("{:04.3f}".format(random.random()), end=" ")
print()

"""
$ ls state.dat
ls: cannot access 'state.dat': No such file or directory
$

$ python 04_random_state.py
No state.dat, seeding
0.134 0.847 0.764

After saving state:
0.255 0.495 0.449

$ ls state.dat
state.dat

$ python 04_random_state.py
Found state.dat, initializing random module
0.255 0.495 0.449

After saving state:
0.652 0.789 0.094

$ python 04_random_state.py
Found state.dat, initializing random module
0.652 0.789 0.094

After saving state:
0.028 0.836 0.433
$
"""
