#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
""" """

# end_pymotw_header
import sys
import weakref


class ExpensiveObject:

    def __del__(self):
        print("(Deleting {})".format(self))


def on_finalize(*args):
    print("on_finalize({!r})".format(args))


obj = ExpensiveObject()

# finalize 的参数是要跟踪的对象、当对象被垃圾收集时要调用的可调用函数以及要传递给可调用函数的任何位置参数或命名参数
# weakref.finalize(obj, on_finalize, "extra argument")
f = weakref.finalize(obj, on_finalize, "extra argument")
# finalize 实例具有可写属性 atexit 来控制在程序退出时是否调用回调(如果它尚未被调用)
f.atexit = bool(int(sys.argv[1]))

"""
$ python 13_weakref_finalize_atexit.py 1
on_finalize(('extra argument',))
(Deleting <__main__.ExpensiveObject object at 0x7f6ddf3c3fd0>)
$
$ python 13_weakref_finalize_atexit.py 0
(Deleting <__main__.ExpensiveObject object at 0x7f6e720f3fd0>)
$
"""
