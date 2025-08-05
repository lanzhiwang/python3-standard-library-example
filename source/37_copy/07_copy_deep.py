#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright 2007 Doug Hellmann.
#
"""Deep copy example"""

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
dup = copy.deepcopy(my_list)

print("             my_list:", my_list)
print("                 dup:", dup)
print("      dup is my_list:", (dup is my_list))
print("      dup == my_list:", (dup == my_list))
print("dup[0] is my_list[0]:", (dup[0] is my_list[0]))
print("dup[0] == my_list[0]:", (dup[0] == my_list[0]))

"""
$ python 07_copy_deep.py
             my_list: [<__main__.MyClass object at 0x7fe51d6f3fd0>]
                 dup: [<__main__.MyClass object at 0x7fe51d71c0a0>]
      dup is my_list: False
      dup == my_list: True
dup[0] is my_list[0]: False
dup[0] == my_list[0]: True
$
"""
