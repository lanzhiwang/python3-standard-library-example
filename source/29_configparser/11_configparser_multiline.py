#!/usr/bin/env python3
#
# Copyright 2015 Doug Hellmann.
"""Example use of ConfigParser module."""

# end_pymotw_header
from configparser import ConfigParser
import os

filename = "multiline.ini"
config = ConfigParser()
config.read([filename])

message = config["example"]["message"]

print(message)
"""
(venv) huzhi@huzhideMacBook-Pro 29_configparser % python 11_configparser_multiline.py
This is a multi-line string.
With two paragraphs.

They are separated by a completely empty line.
(venv) huzhi@huzhideMacBook-Pro 29_configparser %
"""
