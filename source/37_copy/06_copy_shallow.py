#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright 2007 Doug Hellmann.
#
"""Shallow copy example"""

# end_pymotw_header
import copy
import functools


@functools.total_ordering
class MyClass:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self, other):
        return self.name > other.name


a = MyClass("a")
my_list = [a]
dup = copy.copy(my_list)

print("             my_list:", my_list)
print("                 dup:", dup)
print("      dup is my_list:", (dup is my_list))
print("      dup == my_list:", (dup == my_list))
print("dup[0] is my_list[0]:", (dup[0] is my_list[0]))
print("dup[0] == my_list[0]:", (dup[0] == my_list[0]))

"""
$ python 06_copy_shallow.py
             my_list: [<__main__.MyClass object at 0x7fa7f7b93fd0>]
                 dup: [<__main__.MyClass object at 0x7fa7f7b93fd0>]
      dup is my_list: False
      dup == my_list: True
dup[0] is my_list[0]: True
dup[0] == my_list[0]: True
$
"""
