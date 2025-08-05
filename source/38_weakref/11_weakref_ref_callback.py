#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Example using weakref.ref to manage a reference to an object
with a callback.
"""

# end_pymotw_header
import weakref


class ExpensiveObject:

    def __del__(self):
        print("(Deleting {})".format(self))


def callback(reference):
    """Invoked when referenced object is deleted"""
    print("callback({!r})".format(reference))


obj = ExpensiveObject()
r = weakref.ref(obj, callback)

print("obj:", obj)
print("ref:", r)
print("r():", r())

print("deleting obj")
del obj
print("r():", r())

"""
$ python 11_weakref_ref_callback.py
obj: <__main__.ExpensiveObject object at 0x7fa7970affd0>
ref: <weakref at 0x7fa7970c33d0; to 'ExpensiveObject' at 0x7fa7970affd0>
r(): <__main__.ExpensiveObject object at 0x7fa7970affd0>
deleting obj
(Deleting <__main__.ExpensiveObject object at 0x7fa7970affd0>)
callback(<weakref at 0x7fa7970c33d0; dead>)
r(): None
$
"""
