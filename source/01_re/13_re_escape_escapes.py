#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Escaping escape codes"""

import re


def test_patterns(text, patterns):
    """Given source text and a list of patterns, look for
    matches for each pattern within the text and print
    them to stdout.
    """
    # Look for each pattern in the text and print the results
    for pattern, desc in patterns:
        print("'{}' ({})\n".format(pattern, desc))
        print("  '{}'".format(text))
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            substr = text[s:e]
            n_backslashes = text[:s].count("\\")
            prefix = "." * (s + n_backslashes)
            print("  {}'{}'".format(prefix, substr))
        print()
    return


test_patterns(
    r"\d+ \D+ \s+",
    [(r"\\.\+", "escape code")],
)

"""
'\\.\+' (escape code)

  '\d+ \D+ \s+'
  '\d+'
  .....'\D+'
  ..........'\s+'

"""
