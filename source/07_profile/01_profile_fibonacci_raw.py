#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#

#end_pymotw_header
import profile


def fib(n):
    # from literateprograms.org
    # http://bit.ly/hlOQ5m
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib_seq(n):
    seq = []
    if n > 0:
        seq.extend(fib_seq(n - 1))
    seq.append(fib(n))
    return seq


profile.run('print(fib_seq(20)); print()')

"""
调用次数 函数的总时间花费 每次调用的时间 函数的累积花费时间 累积时间在原生调用中所占比率
ncalls    tottime       percall       cumtime           percall
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
()
         57356 function calls (66 primitive calls) in 0.229 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
 57291/21    0.228    0.000    0.228    0.011 01_profile_fibonacci_raw.py:11(fib)
     21/1    0.000    0.000    0.228    0.228 01_profile_fibonacci_raw.py:22(fib_seq)
       21    0.000    0.000    0.000    0.000 :0(append)
       20    0.000    0.000    0.000    0.000 :0(extend)
        1    0.000    0.000    0.000    0.000 :0(setprofile)
        1    0.000    0.000    0.228    0.228 <string>:1(<module>)
        1    0.001    0.001    0.229    0.229 profile:0(print(fib_seq(20)); print())
        0    0.000             0.000          profile:0(profiler)


"""