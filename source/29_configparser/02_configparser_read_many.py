#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Reading a configuration file.
"""

#end_pymotw_header
from configparser import ConfigParser
import glob

parser = ConfigParser()

candidates = ['does_not_exist.ini', 'also-does-not-exist.ini',
              'simple.ini', 'multisection.ini']

found = parser.read(candidates)

missing = set(candidates) - set(found)

print('Found config files:', sorted(found))
print('Missing files     :', sorted(missing))

"""
(venv) huzhi@huzhideMacBook-Pro 29_configparser % python 02_configparser_read_many.py
Found config files: ['multisection.ini', 'simple.ini']
Missing files     : ['also-does-not-exist.ini', 'does_not_exist.ini']
(venv) huzhi@huzhideMacBook-Pro 29_configparser %
"""