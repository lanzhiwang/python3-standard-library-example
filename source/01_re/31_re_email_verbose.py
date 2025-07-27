#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Match email addresses"""

# end_pymotw_header
import re

address = re.compile(
    """
    [\w\d.+-]+       # username
    @
    ([\w\d.]+\.)+    # domain name prefix
    (com|org|edu)    # TODO: support more top-level domains
    """,
    re.VERBOSE,
)

candidates = [
    "first.last@example.com",
    "first.last+category@gmail.com",
    "valid-address@mail.example.com",
    "not-valid@example.foo",
]

for candidate in candidates:
    match = address.search(candidate)
    print(
        "{:<30}  {}".format(candidate, "Matches" if match else "No match"),
    )

"""
first.last@example.com          Matches
first.last+category@gmail.com   Matches
valid-address@mail.example.com  Matches
not-valid@example.foo           No match
"""
