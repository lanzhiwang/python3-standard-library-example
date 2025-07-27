#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Show the objects with references to a given object."""

# end_pymotw_header
import gc
import pprint
import queue


class Graph:

    def __init__(self, name):
        self.name = name
        self.next = None

    def set_next(self, next):
        print("Linking nodes {}.next = {}".format(self, next))
        self.next = next

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, self.name)


# Construct a graph cycle
one = Graph("one")
two = Graph("two")
three = Graph("three")
one.set_next(two)
two.set_next(three)
three.set_next(one)

print()

seen = set()
to_process = queue.Queue()

# Start with an empty object chain and Graph three.
to_process.put(([], three))

# Look for cycles, building the object chain for each object
# found in the queue so the full cycle can be printed at the
# end.
while not to_process.empty():
    chain, next = to_process.get()
    chain = chain[:]
    chain.append(next)
    print("Examining:", repr(next))
    seen.add(id(next))

    print(gc.get_referents(next))
    for r in gc.get_referents(next):
        print(r)
        if isinstance(r, str) or isinstance(r, type):
            # Ignore strings and classes
            print("Ignore strings and classes")
            pass
        elif id(r) in seen:
            print()
            print("Found a cycle to {}:".format(r))
            for i, link in enumerate(chain):
                print("  {}: ".format(i), end=" ")
                pprint.pprint(link)
        else:
            print("to_process.put")
            to_process.put((chain, r))

"""
Linking nodes Graph(one).next = Graph(two)
Linking nodes Graph(two).next = Graph(three)
Linking nodes Graph(three).next = Graph(one)

Examining: Graph(three)
[{'name': 'three', 'next': Graph(one)}, <class '__main__.Graph'>]
{'name': 'three', 'next': Graph(one)}
to_process.put
<class '__main__.Graph'>
Ignore strings and classes
Examining: {'name': 'three', 'next': Graph(one)}
['three', Graph(one)]
three
Ignore strings and classes
Graph(one)
to_process.put
Examining: Graph(one)
[{'name': 'one', 'next': Graph(two)}, <class '__main__.Graph'>]
{'name': 'one', 'next': Graph(two)}
to_process.put
<class '__main__.Graph'>
Ignore strings and classes
Examining: {'name': 'one', 'next': Graph(two)}
['one', Graph(two)]
one
Ignore strings and classes
Graph(two)
to_process.put
Examining: Graph(two)
[{'name': 'two', 'next': Graph(three)}, <class '__main__.Graph'>]
{'name': 'two', 'next': Graph(three)}
to_process.put
<class '__main__.Graph'>
Ignore strings and classes
Examining: {'name': 'two', 'next': Graph(three)}
['two', Graph(three)]
two
Ignore strings and classes
Graph(three)

Found a cycle to Graph(three):
  0:  Graph(three)
  1:  {'name': 'three', 'next': Graph(one)}
  2:  Graph(one)
  3:  {'name': 'one', 'next': Graph(two)}
  4:  Graph(two)
  5:  {'name': 'two', 'next': Graph(three)}

"""
