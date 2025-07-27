#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Reading a configuration file."""

# end_pymotw_header
import configparser

# Require values
try:
    parser = configparser.ConfigParser()
    parser.read("allow_no_value.ini")
except configparser.ParsingError as err:
    print("Could not parse:", err)

# Allow stand-alone option names
print("\nTrying again with allow_no_value=True")
parser = configparser.ConfigParser(allow_no_value=True)
parser.read("allow_no_value.ini")
for flag in ["turn_feature_on", "turn_other_feature_on"]:
    print("\n", flag)
    exists = parser.has_option("flags", flag)
    print("  has_option:", exists)
    if exists:
        print("         get:", parser.get("flags", flag))

"""
(venv) huzhi@huzhideMacBook-Pro 29_configparser % python 10_configparser_allow_no_value.py
Could not parse: Source contains parsing errors: 'allow_no_value.ini'
	[line  2]: 'turn_feature_on\n'

Trying again with allow_no_value=True

 turn_feature_on
  has_option: True
         get: None

 turn_other_feature_on
  has_option: False
(venv) huzhi@huzhideMacBook-Pro 29_configparser %
"""
