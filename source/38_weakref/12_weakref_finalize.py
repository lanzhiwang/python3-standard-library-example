#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
""" """

# end_pymotw_header
import weakref


class ExpensiveObject:

    def __del__(self):
        print("(Deleting {})".format(self))


def on_finalize(*args):
    print("on_finalize({!r})".format(args))


obj = ExpensiveObject()
# finalize 的参数是要跟踪的对象、当对象被垃圾收集时要调用的可调用函数以及要传递给可调用函数的任何位置参数或命名参数
weakref.finalize(obj, on_finalize, "extra argument")

del obj

"""
$ python 12_weakref_finalize.py
(Deleting <__main__.ExpensiveObject object at 0x7f1af0287f40>)
on_finalize(('extra argument',))
$
"""
