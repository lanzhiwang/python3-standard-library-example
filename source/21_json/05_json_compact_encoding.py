#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
""" """

# end_pymotw_header
import json

data = [{"a": "A", "b": (2, 4), "c": 3.0}]
print("DATA:", repr(data))
print("repr(data)             :", len(repr(data)))

plain_dump = json.dumps(data)
print(plain_dump)
print("dumps(data)            :", len(plain_dump))

small_indent = json.dumps(data, indent=2)
print(small_indent)
print("dumps(data, indent=2)  :", len(small_indent))

with_separators = json.dumps(data, separators=(",", ":"))
print(with_separators)
print("dumps(data, separators):", len(with_separators))

"""
DATA: [{'a': 'A', 'b': (2, 4), 'c': 3.0}]
repr(data)             : 35
[{"a": "A", "b": [2, 4], "c": 3.0}]
dumps(data)            : 35
[
  {
    "a": "A",
    "b": [
      2,
      4
    ],
    "c": 3.0
  }
]
dumps(data, indent=2)  : 73
[{"a":"A","b":[2,4],"c":3.0}]
dumps(data, separators): 29
"""
