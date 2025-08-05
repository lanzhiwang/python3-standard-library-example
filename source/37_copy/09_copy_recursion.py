#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright 2007 Doug Hellmann.
#
"""Shallow copy example"""

# end_pymotw_header
import copy


class Graph:

    def __init__(self, name, connections):
        self.name = name
        self.connections = connections

    def add_connection(self, other):
        self.connections.append(other)

    def __repr__(self):
        return "Graph(name={}, id={})".format(self.name, id(self))

    def __deepcopy__(self, memo):
        print("\nCalling __deepcopy__ for {!r}".format(self))
        if self in memo:
            existing = memo.get(self)
            print("  Already copied to {!r}".format(existing))
            return existing
        print("  Memo dictionary:")
        if memo:
            for k, v in memo.items():
                print("    {}: {}".format(k, v))
        else:
            print("    (empty)")
        dup = Graph(copy.deepcopy(self.name, memo), [])
        print("  Copying to new object {}".format(dup))
        memo[self] = dup
        for c in self.connections:
            dup.add_connection(copy.deepcopy(c, memo))
        return dup


root = Graph("root", [])
a = Graph("a", [root])
b = Graph("b", [a, root])
root.add_connection(a)
root.add_connection(b)

dup = copy.deepcopy(root)

"""
$ python 09_copy_recursion.py

Calling __deepcopy__ for Graph(name=root, id=140478937808848)
  Memo dictionary:
    (empty)
  Copying to new object Graph(name=root, id=140478937807456)

Calling __deepcopy__ for Graph(name=a, id=140478937808560)
  Memo dictionary:
    Graph(name=root, id=140478937808848): Graph(name=root, id=140478937807456)
  Copying to new object Graph(name=a, id=140478937795600)

Calling __deepcopy__ for Graph(name=root, id=140478937808848)
  Already copied to Graph(name=root, id=140478937807456)

Calling __deepcopy__ for Graph(name=b, id=140478937808368)
  Memo dictionary:
    Graph(name=root, id=140478937808848): Graph(name=root, id=140478937807456)
    Graph(name=a, id=140478937808560): Graph(name=a, id=140478937795600)
    140478937808848: Graph(name=root, id=140478937807456)
    140478937952256: [Graph(name=root, id=140478937808848), Graph(name=a, id=140478937808560)]
    140478937808560: Graph(name=a, id=140478937795600)
  Copying to new object Graph(name=b, id=140478937795408)
$
"""
