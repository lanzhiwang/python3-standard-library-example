#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""
"""

#end_pymotw_header
import argparse

parser = argparse.ArgumentParser(description='Short sample app')

parser.add_argument('-a', action="store_true", default=False)  # 布尔型选项 (-a)
parser.add_argument('-b', action="store", dest="b")  # 简单的字符串选项 (-b)
parser.add_argument('-c', action="store", dest="c", type=int)  # 整数选项 (-c)
parser.add_argument('-d', action="store", dest="ddd")  # 整数选项 (-c)

print(parser.parse_args(['-a', '-bval', '-c', '3', '-dvdl']))
# Namespace(a=True, b='val', c=3, ddd='vdl')

print(parser.parse_args(['-a', '-bval', '-c', '3', '-dvdl']).ddd)  # vdl
