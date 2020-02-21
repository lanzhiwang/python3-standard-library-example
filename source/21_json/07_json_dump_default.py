#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""

#end_pymotw_header
import json
import json_myobj

obj = json_myobj.MyObj('instance value goes here')

data = [{'a': 'A', 'b': (2, 4), 'c': 3.0, 'o': obj}]
print('First attempt')
try:
    print(json.dumps(data))
except TypeError as err:
    print('ERROR:', err)


def convert_to_builtin_type(obj):
    print('default(', repr(obj), ')')
    # Convert objects to a dictionary of their representation
    d = {
        '__class__': obj.__class__.__name__,
        '__module__': obj.__module__,
    }
    d.update(obj.__dict__)
    return d


print()
print('With default')
print(json.dumps(data, default=convert_to_builtin_type))

print(json.dumps(obj, default=convert_to_builtin_type))

"""
First attempt
ERROR: Object of type MyObj is not JSON serializable

With default
default( <MyObj(instance value goes here)> )
[{"a": "A", "b": [2, 4], "c": 3.0, "o": {"__class__": "MyObj", "__module__": "json_myobj", "s": "instance value goes here"}}]

default( <MyObj(instance value goes here)> )
{"__class__": "MyObj", "__module__": "json_myobj", "s": "instance value goes here"}
"""