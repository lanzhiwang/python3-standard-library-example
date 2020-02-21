#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""

#end_pymotw_header
import json

encoder = json.JSONEncoder()
data = [{'a': 'A', 'b': (2, 4), 'c': 3.0}]

for part in encoder.iterencode(data):
    print('PART:', part)

"""
PART: [
PART: {
PART: "a"
PART: :
PART: "A"
PART: ,
PART: "b"
PART: :
PART: [2
PART: , 4
PART: ]
PART: ,
PART: "c"
PART: :
PART: 3.0
PART: }
PART: ]
"""