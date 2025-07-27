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

    # A name is made up of letters, and may include "."
    # for title abbreviations and middle initials.
    ((?P<name>
       ([\w.,]+\s+)*[\w.,]+)
       \s*
       # Email addresses are wrapped in angle
       # brackets < >, but only if a name is
       # found, so keep the start bracket in this
       # group.
       <
    )? # the entire name is optional

    # The address itself: username@domain.tld
    (?P<email>
      [\w\d.+-]+       # username
      @
      ([\w\d.]+\.)+    # domain name prefix
      (com|org|edu)    # limit the allowed top-level domains
    )

    >? # optional closing angle bracket
    """,
    re.VERBOSE,
)

candidates = [
    "first.last@example.com",
    "first.last+category@gmail.com",
    "valid-address@mail.example.com",
    "not-valid@example.foo",
    "First Last <first.last@example.com>",
    "No Brackets first.last@example.com",
    "First Last",
    "First Middle Last <first.last@example.com>",
    "First M. Last <first.last@example.com>",
    "<first.last@example.com>",
]

for candidate in candidates:
    print("Candidate:", candidate)
    match = address.search(candidate)
    if match:
        print("  Name :", match.groupdict()["name"])
        print("  Email:", match.groupdict()["email"])
    else:
        print("  No match")

"""
Candidate: first.last@example.com
  Name : None
  Email: first.last@example.com
Candidate: first.last+category@gmail.com
  Name : None
  Email: first.last+category@gmail.com
Candidate: valid-address@mail.example.com
  Name : None
  Email: valid-address@mail.example.com
Candidate: not-valid@example.foo
  No match
Candidate: First Last <first.last@example.com>
  Name : First Last
  Email: first.last@example.com
Candidate: No Brackets first.last@example.com
  Name : None
  Email: first.last@example.com
Candidate: First Last
  No match
Candidate: First Middle Last <first.last@example.com>
  Name : First Middle Last
  Email: first.last@example.com
Candidate: First M. Last <first.last@example.com>
  Name : First M. Last
  Email: first.last@example.com
Candidate: <first.last@example.com>
  Name : None
  Email: first.last@example.com
"""
