#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Parent with shared options"""

# end_pymotw_header
import argparse
import argparse_parent_base

parser = argparse.ArgumentParser(
    parents=[argparse_parent_base.parser],
)

parser.add_argument("--local-arg", action="store_true", default=False)

print(parser.parse_args())

"""
(venv) huzhi@huzhideMacBook-Pro argparse % python 14_argparse_uses_parent.py
Namespace(local_arg=False, password=None, user=None)
(venv) huzhi@huzhideMacBook-Pro argparse %
(venv) huzhi@huzhideMacBook-Pro argparse %
(venv) huzhi@huzhideMacBook-Pro argparse % python 14_argparse_uses_parent.py -h
usage: 14_argparse_uses_parent.py [-h] [--user USER] [--password PASSWORD]
                                  [--local-arg]

optional arguments:
  -h, --help           show this help message and exit
  --user USER
  --password PASSWORD
  --local-arg
(venv) huzhi@huzhideMacBook-Pro argparse %
"""
