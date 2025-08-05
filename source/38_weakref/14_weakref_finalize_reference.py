#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
""" """

# end_pymotw_header
import gc
import weakref


class ExpensiveObject:

    def __del__(self):
        print("(Deleting {})".format(self))


def on_finalize(*args):
    print("on_finalize({!r})".format(args))


obj = ExpensiveObject()
obj_id = id(obj)

# finalize 的参数是要跟踪的对象、当对象被垃圾收集时要调用的可调用函数以及要传递给可调用函数的任何位置参数或命名参数
# weakref.finalize(obj, on_finalize, "extra argument")
# f = weakref.finalize(obj, on_finalize, "extra argument")
# 为 finalize 实例提供对其跟踪的对象的引用会导致引用被保留, 因此该对象永远不会被垃圾收集
f = weakref.finalize(obj, on_finalize, obj)
f.atexit = False

del obj

for o in gc.get_objects():
    if id(o) == obj_id:
        print("found uncollected object in gc")

"""
$ python 14_weakref_finalize_reference.py
found uncollected object in gc
(Deleting <__main__.ExpensiveObject object at 0x7fb1e43affd0>)
$
"""
