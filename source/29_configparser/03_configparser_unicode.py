#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Reading a configuration file.
"""

#end_pymotw_header
from configparser import ConfigParser
import codecs

parser = ConfigParser()
# Open the file with the correct encoding
parser.read('unicode.ini', encoding='utf-8')

password = parser.get('bug_tracker', 'password')

print('Password:', password.encode('utf-8'))
print('Type    :', type(password))
print('repr()  :', repr(password))

"""
(venv) huzhi@huzhideMacBook-Pro 29_configparser % python 03_configparser_unicode.py
Password: b'\xc3\x9f\xc3\xa9\xc3\xa7\xc2\xae\xc3\xa9\xe2\x80\xa0'
Type    : <class 'str'>
repr()  : 'ßéç®é†'
(venv) huzhi@huzhideMacBook-Pro 29_configparser %
"""