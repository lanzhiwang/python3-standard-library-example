#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Demonstrate WeakValueDictionary."""

# end_pymotw_header
import gc
from pprint import pprint
import weakref

gc.set_debug(gc.DEBUG_UNCOLLECTABLE)


class ExpensiveObject:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "ExpensiveObject({})".format(self.name)

    def __del__(self):
        print("    (Deleting {})".format(self))


def demo(cache_factory):
    # hold objects so any weak references
    # are not removed immediately
    all_refs = {}
    # create the cache using the factory
    print("CACHE TYPE:", cache_factory)
    cache = cache_factory()
    for name in ["one", "two", "three"]:
        o = ExpensiveObject(name)
        cache[name] = o
        all_refs[name] = o
        del o  # decref

    print("  all_refs =", end=" ")
    pprint(all_refs)
    print("\n  Before, cache contains:", list(cache.keys()))
    for name, value in cache.items():
        print("    {} = {}".format(name, value))
        del value  # decref

    # remove all references to the objects except the cache
    print("\n  Cleanup:")
    del all_refs
    gc.collect()

    print("\n  After, cache contains:", list(cache.keys()))
    for name, value in cache.items():
        print("    {} = {}".format(name, value))
    print("  demo returning")
    return


demo(dict)
print()

demo(weakref.WeakValueDictionary)

"""
$ python 17_weakref_valuedict.py
CACHE TYPE: <class 'dict'>
  all_refs = {'one': ExpensiveObject(one),
 'three': ExpensiveObject(three),
 'two': ExpensiveObject(two)}

  Before, cache contains: ['one', 'two', 'three']
    one = ExpensiveObject(one)
    two = ExpensiveObject(two)
    three = ExpensiveObject(three)

  Cleanup:

  After, cache contains: ['one', 'two', 'three']
    one = ExpensiveObject(one)
    two = ExpensiveObject(two)
    three = ExpensiveObject(three)
  demo returning
    (Deleting ExpensiveObject(one))
    (Deleting ExpensiveObject(two))
    (Deleting ExpensiveObject(three))

CACHE TYPE: <class 'weakref.WeakValueDictionary'>
  all_refs = {'one': ExpensiveObject(one),
 'three': ExpensiveObject(three),
 'two': ExpensiveObject(two)}

  Before, cache contains: ['one', 'two', 'three']
    one = ExpensiveObject(one)
    two = ExpensiveObject(two)
    three = ExpensiveObject(three)

  Cleanup:
    (Deleting ExpensiveObject(one))
    (Deleting ExpensiveObject(two))
    (Deleting ExpensiveObject(three))

  After, cache contains: []
  demo returning
$
"""
