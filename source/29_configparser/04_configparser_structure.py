#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Reading a configuration file."""

# end_pymotw_header
from configparser import ConfigParser

parser = ConfigParser()
parser.read("multisection.ini")

for section_name in parser.sections():
    print("Section:", section_name)
    print("  Options:", parser.options(section_name))
    for name, value in parser.items(section_name):
        print("  {} = {}".format(name, value))
    print()

"""
(venv) huzhi@huzhideMacBook-Pro 29_configparser % python 04_configparser_structure.py
Section: bug_tracker
  Options: ['url', 'username', 'password']
  url = http://localhost:8080/bugs/
  username = dhellmann
  password = SECRET

Section: wiki
  Options: ['url', 'username', 'password']
  url = http://localhost:8080/wiki/
  username = dhellmann
  password = SECRET

(venv) huzhi@huzhideMacBook-Pro 29_configparser %
"""
