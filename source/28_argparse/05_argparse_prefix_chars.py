#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Set prefix_chars"""

# end_pymotw_header
import argparse

parser = argparse.ArgumentParser(
    description="Change the option prefix characters",
    prefix_chars="-+/",
)

parser.add_argument(
    "-a",
    action="store_false",
    default=None,
    help="Turn A off",
)
parser.add_argument(
    "+a",
    action="store_true",
    default=None,
    help="Turn A on",
)
parser.add_argument("//noarg", "++noarg", action="store_true", default=False)

print(parser.parse_args())

"""
huzhi@huzhideMacBook-Pro argparse % python 05_argparse_prefix_chars.py -h
usage: 05_argparse_prefix_chars.py [-h] [-a] [+a] [//noarg]

Change the option prefix characters

optional arguments:
  -h, --help        show this help message and exit
  -a                Turn A off
  +a                Turn A on
  //noarg, ++noarg
huzhi@huzhideMacBook-Pro argparse %
huzhi@huzhideMacBook-Pro argparse % python 05_argparse_prefix_chars.py +a
Namespace(a=True, noarg=False)
huzhi@huzhideMacBook-Pro argparse %
huzhi@huzhideMacBook-Pro argparse % python 05_argparse_prefix_chars.py -a
Namespace(a=False, noarg=False)
huzhi@huzhideMacBook-Pro argparse %
huzhi@huzhideMacBook-Pro argparse % python 05_argparse_prefix_chars.py //noarg
Namespace(a=None, noarg=True)
huzhi@huzhideMacBook-Pro argparse %
huzhi@huzhideMacBook-Pro argparse % python 05_argparse_prefix_chars.py ++noarg
Namespace(a=None, noarg=True)
huzhi@huzhideMacBook-Pro argparse %
huzhi@huzhideMacBook-Pro argparse % python 05_argparse_prefix_chars.py --noarg
usage: 05_argparse_prefix_chars.py [-h] [-a] [+a] [//noarg]
05_argparse_prefix_chars.py: error: unrecognized arguments: --noarg
huzhi@huzhideMacBook-Pro argparse %
"""
