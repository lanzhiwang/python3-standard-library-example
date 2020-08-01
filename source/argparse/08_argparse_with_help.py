#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""
"""

#end_pymotw_header
import argparse

parser = argparse.ArgumentParser(add_help=True)

parser.add_argument('-a', action="store_true", default=False)
parser.add_argument('-b', action="store", dest="b")
parser.add_argument('-c', action="store", dest="c", type=int)

print(parser.parse_args())
"""
(venv) huzhi@huzhideMacBook-Pro argparse % python 08_argparse_with_help.py -h
usage: 08_argparse_with_help.py [-h] [-a] [-b B] [-c C]

optional arguments:
  -h, --help  show this help message and exit
  -a
  -b B
  -c C
(venv) huzhi@huzhideMacBook-Pro argparse %
(venv) huzhi@huzhideMacBook-Pro argparse % python 09_argparse_without_help.py -h
usage: 09_argparse_without_help.py [-a] [-b B] [-c C]
09_argparse_without_help.py: error: unrecognized arguments: -h
(venv) huzhi@huzhideMacBook-Pro argparse %
"""