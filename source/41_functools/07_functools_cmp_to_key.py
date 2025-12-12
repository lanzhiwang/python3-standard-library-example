#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Fill in missing rich comparison methods."""

# end_pymotw_header
import functools


class MyObject:

    def __init__(self, val):
        self.val = val

    def __str__(self):
        return "MyObject({})".format(self.val)


def compare_obj(a, b):
    """Old-style comparison function."""
    print("comparing {} and {}".format(a, b))
    if a.val < b.val:
        return -1
    elif a.val > b.val:
        return 1
    return 0


# Make a key function using cmp_to_key()
get_key = functools.cmp_to_key(compare_obj)


def get_key_wrapper(o):
    "Wrapper function for get_key to allow for print statements."
    new_key = get_key(o)
    print("key_wrapper({}) -> {!r}".format(o, new_key))
    return new_key


objs = [MyObject(x) for x in range(5, 0, -1)]

for o in sorted(objs, key=get_key_wrapper):
    print(o)

"""
$ python 07_functools_cmp_to_key.py
key_wrapper(MyObject(5)) -> <functools.KeyWrapper object at 0x7f5e3ae16e60>
key_wrapper(MyObject(4)) -> <functools.KeyWrapper object at 0x7f5e3ae16e90>
key_wrapper(MyObject(3)) -> <functools.KeyWrapper object at 0x7f5e3ae16ec0>
key_wrapper(MyObject(2)) -> <functools.KeyWrapper object at 0x7f5e3ae16ef0>
key_wrapper(MyObject(1)) -> <functools.KeyWrapper object at 0x7f5e3ae17070>
comparing MyObject(4) and MyObject(5)
comparing MyObject(3) and MyObject(4)
comparing MyObject(2) and MyObject(3)
comparing MyObject(1) and MyObject(2)
MyObject(1)
MyObject(2)
MyObject(3)
MyObject(4)
MyObject(5)
$
"""
