#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Show the built-in argument actions.
"""

#end_pymotw_header
import argparse

parser = argparse.ArgumentParser()


"""
参数动作
当一个参数被传递时可以触发任何 6 个内建动作的任何一个。

store 选择性地转换为一个不同的类型后保存参数值。如果没有特别声明动作时这是默认动作。

store_const 保存一个在参数声明时定义的值，而非解析参数时得到的值。这通常被用于实现非布尔型数值的命令行标志。

store_true / store_false 保存相应的布尔型数值，这个动作被用于实现布尔值开关。

append 将参数值保存在一个列表中。如果参数重复了，那么多个参数值将会被保存。

append_const 将参数值保存在参数声明时指定的列表中。

version 打印程序版本详情然后退出

"""

# store 选择性地转换为一个不同的类型后保存参数值。如果没有特别声明动作时这是默认动作。
parser.add_argument('-s', action='store',
                    dest='simple_value',
                    help='Store a simple value')

# store_const 保存一个在参数声明时定义的值，而非解析参数时得到的值。这通常被用于实现非布尔型数值的命令行标志。
parser.add_argument('-c', action='store_const',
                    dest='constant_value',
                    const='value-to-store',
                    help='Store a constant value')

# store_true / store_false 保存相应的布尔型数值，这个动作被用于实现布尔值开关。
parser.add_argument('-t', action='store_true',
                    default=False,
                    dest='boolean_t',
                    help='Set a switch to true')
parser.add_argument('-f', action='store_false',
                    default=True,
                    dest='boolean_f',
                    help='Set a switch to false')

# append 将参数值保存在一个列表中。如果参数重复了，那么多个参数值将会被保存。
parser.add_argument('-a', action='append',
                    dest='collection',
                    default=[],
                    help='Add repeated values to a list')

# append_const 将参数值保存在参数声明时指定的列表中。
parser.add_argument('-A', action='append_const',
                    dest='const_collection',
                    const='value-1-to-append',
                    default=[],
                    help='Add different values to list')
parser.add_argument('-B', action='append_const',
                    dest='const_collection',
                    const='value-2-to-append',
                    help='Add different values to list')

# version 打印程序版本详情然后退出
parser.add_argument('--version', action='version',
                    version='%(prog)s 1.0')

results = parser.parse_args()
print('simple_value     = {!r}'.format(results.simple_value))
print('constant_value   = {!r}'.format(results.constant_value))
print('boolean_t        = {!r}'.format(results.boolean_t))
print('boolean_f        = {!r}'.format(results.boolean_f))
print('collection       = {!r}'.format(results.collection))
print('const_collection = {!r}'.format(results.const_collection))

"""
huzhi@huzhideMacBook-Pro argparse % python 04_argparse_action.py -h
usage: 04_argparse_action.py [-h] [-s SIMPLE_VALUE] [-c] [-t] [-f]
                             [-a COLLECTION] [-A] [-B] [--version]

optional arguments:
  -h, --help       show this help message and exit
  -s SIMPLE_VALUE  Store a simple value
  -c               Store a constant value
  -t               Set a switch to true
  -f               Set a switch to false
  -a COLLECTION    Add repeated values to a list
  -A               Add different values to list
  -B               Add different values to list
  --version        show program's version number and exit
huzhi@huzhideMacBook-Pro argparse %

huzhi@huzhideMacBook-Pro argparse % python 04_argparse_action.py -s value
simple_value     = 'value'
constant_value   = None
boolean_t        = False
boolean_f        = True
collection       = []
const_collection = []
huzhi@huzhideMacBook-Pro argparse %

huzhi@huzhideMacBook-Pro argparse % python 04_argparse_action.py -c
simple_value     = None
constant_value   = 'value-to-store'
boolean_t        = False
boolean_f        = True
collection       = []
const_collection = []
huzhi@huzhideMacBook-Pro argparse %

huzhi@huzhideMacBook-Pro argparse % python 04_argparse_action.py -t
simple_value     = None
constant_value   = None
boolean_t        = True
boolean_f        = True
collection       = []
const_collection = []
huzhi@huzhideMacBook-Pro argparse %

huzhi@huzhideMacBook-Pro argparse % python 04_argparse_action.py -f
simple_value     = None
constant_value   = None
boolean_t        = False
boolean_f        = False
collection       = []
const_collection = []
huzhi@huzhideMacBook-Pro argparse %

huzhi@huzhideMacBook-Pro argparse % python 04_argparse_action.py -a one -a two -a three
simple_value     = None
constant_value   = None
boolean_t        = False
boolean_f        = True
collection       = ['one', 'two', 'three']
const_collection = []
huzhi@huzhideMacBook-Pro argparse %

huzhi@huzhideMacBook-Pro argparse % python 04_argparse_action.py -B -A
simple_value     = None
constant_value   = None
boolean_t        = False
boolean_f        = True
collection       = []
const_collection = ['value-2-to-append', 'value-1-to-append']
huzhi@huzhideMacBook-Pro argparse %

huzhi@huzhideMacBook-Pro argparse % python 04_argparse_action.py --version
04_argparse_action.py 1.0
huzhi@huzhideMacBook-Pro argparse %

"""