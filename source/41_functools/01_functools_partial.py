#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
""" """

# end_pymotw_header
import functools


def myfunc(a, b=2):
    "Docstring for myfunc()."
    print("  called myfunc with:", (a, b))


def show_details(name, f, is_partial=False):
    "Show details of a callable object."
    print("{}:".format(name))
    print("  object:", f)
    if not is_partial:
        print("  __name__:", f.__name__)
    if is_partial:
        print("  func:", f.func)
        print("  args:", f.args)
        print("  keywords:", f.keywords)
    return


show_details("myfunc", myfunc)
myfunc("a", 3)
print()

# Set a different default value for 'b', but require
# the caller to provide 'a'.
p1 = functools.partial(myfunc, b=4)
show_details("partial with named default", p1, True)
p1("passing a")
p1("override b", b=5)
print()

# Set default values for both 'a' and 'b'.
p2 = functools.partial(myfunc, "default a", b=99)
show_details("partial with defaults", p2, True)
p2()
p2(b="override b")
print()

print("Insufficient arguments:")
p1()

"""
$ python 01_functools_partial.py
myfunc:
  object: <function myfunc at 0x7f9a69e922a0>
  __name__: myfunc
  called myfunc with: ('a', 3)

partial with named default:
  object: functools.partial(<function myfunc at 0x7f9a69e922a0>, b=4)
  func: <function myfunc at 0x7f9a69e922a0>
  args: ()
  keywords: {'b': 4}
  called myfunc with: ('passing a', 4)
  called myfunc with: ('override b', 5)

partial with defaults:
  object: functools.partial(<function myfunc at 0x7f9a69e922a0>, 'default a', b=99)
  func: <function myfunc at 0x7f9a69e922a0>
  args: ('default a',)
  keywords: {'b': 99}
  called myfunc with: ('default a', 99)
  called myfunc with: ('default a', 'override b')

Insufficient arguments:
Traceback (most recent call last):
  File "/python3-standard-library-example/source/41_functools/01_functools_partial.py", line 50, in <module>
    p1()
TypeError: myfunc() missing 1 required positional argument: 'a'
$
"""
