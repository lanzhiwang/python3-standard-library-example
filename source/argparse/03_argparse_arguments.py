#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Long option name example.
"""

#end_pymotw_header
import argparse

parser = argparse.ArgumentParser(
    description='Example with nonoptional arguments',
)

parser.add_argument('count', action="store", type=int)
parser.add_argument('units', action="store")

print(parser.parse_args())

"""
huzhi@huzhideMacBook-Pro argparse % python 03_argparse_arguments.py 3 inches
Namespace(count=3, units='inches')
huzhi@huzhideMacBook-Pro argparse %
huzhi@huzhideMacBook-Pro argparse % python 03_argparse_arguments.py some inches
usage: 03_argparse_arguments.py [-h] count units
03_argparse_arguments.py: error: argument count: invalid int value: 'some'
huzhi@huzhideMacBook-Pro argparse %
huzhi@huzhideMacBook-Pro argparse % python 03_argparse_arguments.py
usage: 03_argparse_arguments.py [-h] count units
03_argparse_arguments.py: error: too few arguments
huzhi@huzhideMacBook-Pro argparse %
"""
