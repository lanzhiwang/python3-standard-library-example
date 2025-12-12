#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Fill in missing rich comparison methods."""

# end_pymotw_header
import functools
import inspect
from pprint import pprint


@functools.total_ordering
class MyObject:

    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        print("  testing __eq__({}, {})".format(self.val, other.val))
        return self.val == other.val

    def __gt__(self, other):
        print("  testing __gt__({}, {})".format(self.val, other.val))
        return self.val > other.val


print("Methods:\n")
pprint(inspect.getmembers(MyObject, inspect.isfunction))

a = MyObject(1)
b = MyObject(2)

print("\nComparisons:")
for expr in ["a < b", "a <= b", "a == b", "a >= b", "a > b"]:
    print("\n{:<6}:".format(expr))
    result = eval(expr)
    print("  result of {}: {}".format(expr, result))

"""
$ python 06_functools_total_ordering.py
Methods:

[('__eq__', <function MyObject.__eq__ at 0x7f84635e5da0>),
 ('__ge__', <function _ge_from_gt at 0x7f84637c23e0>),
 ('__gt__', <function MyObject.__gt__ at 0x7f84635e5e40>),
 ('__init__', <function MyObject.__init__ at 0x7f84635b5440>),
 ('__le__', <function _le_from_gt at 0x7f84637c3f60>),
 ('__lt__', <function _lt_from_gt at 0x7f84637c2ca0>)]

Comparisons:

a < b :
  testing __gt__(1, 2)
  testing __eq__(1, 2)
  result of a < b: True

a <= b:
  testing __gt__(1, 2)
  result of a <= b: True

a == b:
  testing __eq__(1, 2)
  result of a == b: False

a >= b:
  testing __gt__(1, 2)
  testing __eq__(1, 2)
  result of a >= b: False

a > b :
  testing __gt__(1, 2)
  result of a > b: False
$
"""
