#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Reading a configuration file.
"""

#end_pymotw_header
from configparser import ConfigParser

parser = ConfigParser()
parser.read('multisection.ini')

for candidate in ['wiki', 'bug_tracker', 'dvcs']:
    print('{:<12}: {}'.format(
        candidate, parser.has_section(candidate)))

"""
(venv) huzhi@huzhideMacBook-Pro 29_configparser % python 06_configparser_has_section.py
wiki        : True
bug_tracker : True
dvcs        : False
(venv) huzhi@huzhideMacBook-Pro 29_configparser %
"""