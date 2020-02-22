#!/usr/bin/env python3
"""Example of using timeit programatically.

Time various ways to populate and check a dictionary
using a long list of strings and integers.
"""

#end_pymotw_header
import timeit

# using setitem
t = timeit.Timer("print('main statement')", "print('setup')")

print('TIMEIT:')
print(t.timeit(2))

print('REPEAT:')
print(t.repeat(3, 2))

"""
TIMEIT:
setup
main statement
main statement
5.2609999999994606e-06

REPEAT:
setup
main statement
main statement
setup
main statement
main statement
setup
main statement
main statement
[4.4379999999989705e-06, 4.501000000000505e-06, 4.259999999998987e-06]
"""