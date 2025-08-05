#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Example using weakref.ref to manage a reference to an object."""

# end_pymotw_header
import weakref


class ExpensiveObject:

    def __del__(self):
        print("(Deleting {})".format(self))


obj = ExpensiveObject()
r = weakref.ref(obj)

print("obj:", obj)
print("ref:", r)
print("r():", r())

print("deleting obj")
del obj
print("r():", r())

"""
$ python 10_weakref_ref.py
obj: <__main__.ExpensiveObject object at 0x7fc071fdffd0>
ref: <weakref at 0x7fc071ff3380; to 'ExpensiveObject' at 0x7fc071fdffd0>
r(): <__main__.ExpensiveObject object at 0x7fc071fdffd0>
deleting obj
(Deleting <__main__.ExpensiveObject object at 0x7fc071fdffd0>)
r(): None
$
"""
