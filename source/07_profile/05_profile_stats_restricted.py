#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
""" """

# end_pymotw_header
import profile
import pstats
import functools


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


# Create 5 set of stats
for i in range(5):
    filename = "profile_stats_{}.stats".format(i)
    profile.run("print({}, fib_seq(20))".format(i), filename)


# Read all 5 stats files into a single object
stats = pstats.Stats("profile_stats_0.stats")
for i in range(1, 5):
    stats.add("profile_stats_{}.stats".format(i))
stats.strip_dirs()
stats.sort_stats("cumulative")

# limit output to lines with "(fib" in them
stats.print_stats("\(fib")
