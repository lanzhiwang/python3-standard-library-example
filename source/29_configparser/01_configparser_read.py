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
parser.read('simple.ini')

print(parser.get('bug_tracker', 'url'))

"""
(venv) huzhi@huzhideMacBook-Pro 29_configparser % python 01_configparser_read.py
http://localhost:8080/bugs/
(venv) huzhi@huzhideMacBook-Pro 29_configparser %
"""