#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
""" """

# end_pymotw_header
from urllib.parse import quote, quote_plus, urlencode

url = "http://localhost:8080/~hellmann/"
print("urlencode() :", urlencode({"url": url}))
print("quote()     :", quote(url))
print("quote_plus():", quote_plus(url))

"""
urlencode() : url=http%3A%2F%2Flocalhost%3A8080%2F~hellmann%2F
quote()     : http%3A//localhost%3A8080/~hellmann/
quote_plus(): http%3A%2F%2Flocalhost%3A8080%2F~hellmann%2F
"""
