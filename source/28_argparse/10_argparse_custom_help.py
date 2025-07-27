#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
""" """

# end_pymotw_header
import argparse

parser = argparse.ArgumentParser(add_help=True)

parser.add_argument("-a", action="store_true", default=False)
parser.add_argument("-b", action="store", dest="b")
parser.add_argument("-c", action="store", dest="c", type=int)

print("print_usage output:")
parser.print_usage()
print()

print("print_help output:")
parser.print_help()
"""
(venv) huzhi@huzhideMacBook-Pro argparse % python 10_argparse_custom_help.py
print_usage output:
usage: 10_argparse_custom_help.py [-h] [-a] [-b B] [-c C]

print_help output:
usage: 10_argparse_custom_help.py [-h] [-a] [-b B] [-c C]

optional arguments:
  -h, --help  show this help message and exit
  -a
  -b B
  -c C
(venv) huzhi@huzhideMacBook-Pro argparse %
"""
