#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#

#end_pymotw_header
import functools
import profile


@functools.lru_cache(maxsize=None)
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


if __name__ == '__main__':
    # profile.run('print(fib_seq(20)); print()')
    fib_seq(20)

"""
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]

         89 function calls (69 primitive calls) in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       21    0.000    0.000    0.000    0.000 02_profile_fibonacci_memoized.py:12(fib)
     21/1    0.000    0.000    0.000    0.000 02_profile_fibonacci_memoized.py:24(fib_seq)
       21    0.000    0.000    0.000    0.000 :0(append)
        1    0.000    0.000    0.000    0.000 :0(exec)
       20    0.000    0.000    0.000    0.000 :0(extend)
        2    0.000    0.000    0.000    0.000 :0(print)
        1    0.001    0.001    0.001    0.001 :0(setprofile)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.001    0.001 profile:0(print(fib_seq(20)); print())
        0    0.000             0.000          profile:0(profiler)


"""