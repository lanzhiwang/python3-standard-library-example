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


def show_details(name, f):
    "Show details of a callable object."
    print("{}:".format(name))
    print("  object:", f)
    print("  __name__:", end=" ")
    try:
        print(f.__name__)
    except AttributeError:
        print("(no __name__)")
    print("  __doc__", repr(f.__doc__))
    print()


show_details("myfunc", myfunc)

p1 = functools.partial(myfunc, b=4)
show_details("raw wrapper", p1)

print("Updating wrapper:")
print("  assign:", functools.WRAPPER_ASSIGNMENTS)
print("  update:", functools.WRAPPER_UPDATES)
print()

functools.update_wrapper(p1, myfunc)
show_details("updated wrapper", p1)

"""
$ python 02_functools_update_wrapper.py
myfunc:
  object: <function myfunc at 0x7fe42d2762a0>
  __name__: myfunc
  __doc__ 'Docstring for myfunc().'

raw wrapper:
  object: functools.partial(<function myfunc at 0x7fe42d2762a0>, b=4)
  __name__: (no __name__)
  __doc__ 'partial(func, *args, **keywords) - new function with partial application\n    of the given arguments and keywords.\n'

Updating wrapper:
  assign: ('__module__', '__name__', '__qualname__', '__doc__', '__annotations__', '__type_params__')
  update: ('__dict__',)

updated wrapper:
  object: functools.partial(<function myfunc at 0x7fe42d2762a0>, b=4)
  __name__: myfunc
  __doc__ 'Docstring for myfunc().'

$
"""
