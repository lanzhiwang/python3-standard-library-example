#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
""" """

# end_pymotw_header
import argparse

parser = argparse.ArgumentParser(
    add_help=True,
    formatter_class=argparse.MetavarTypeHelpFormatter,
)

parser.add_argument("-i", type=int, dest="notshown1")
parser.add_argument("-f", type=float, dest="notshown2")

parser.print_help()
"""
(venv) huzhi@huzhideMacBook-Pro argparse % python 13_argparse_metavar_type_help_formatter.py
usage: 13_argparse_metavar_type_help_formatter.py [-h] [-i int] [-f float]

optional arguments:
  -h, --help  show this help message and exit
  -i int
  -f float
(venv) huzhi@huzhideMacBook-Pro argparse %
"""
