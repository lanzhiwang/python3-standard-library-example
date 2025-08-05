#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Using proxy instead of ref."""

# end_pymotw_header
import weakref


class ExpensiveObject:

    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("(Deleting {})".format(self))


obj = ExpensiveObject("My Object")
r = weakref.ref(obj)
p = weakref.proxy(obj)

print("via obj:", obj.name)
print("via ref:", r().name)
print("via proxy:", p.name)
del obj
print("via proxy:", p.name)

"""
$ python 16_weakref_proxy.py
via obj: My Object
via ref: My Object
via proxy: My Object
(Deleting <__main__.ExpensiveObject object at 0x7f04e2353fa0>)
Traceback (most recent call last):
  File "/python3-standard-library-example/source/38_weakref/16_weakref_proxy.py", line 29, in <module>
    print("via proxy:", p.name)
ReferenceError: weakly-referenced object no longer exists
$
"""
