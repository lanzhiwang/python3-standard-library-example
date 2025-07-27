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

for section_name in parser:
    print("Section:", section_name)
    section = parser[section_name]
    print("  Options:", list(section.keys()))
    for name in section:
        print("  {} = {}".format(name, section[name]))
    print()

"""
(venv) huzhi@huzhideMacBook-Pro 29_configparser % python 05_configparser_structure_dict.py
Section: DEFAULT
  Options: []

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
