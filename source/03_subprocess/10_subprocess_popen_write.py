#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""


#end_pymotw_header
import subprocess

print('write:')
proc = subprocess.Popen(
    ['cat', '-'],
    stdin=subprocess.PIPE,
)
proc.communicate('stdin: to stdin\n'.encode('utf-8'))

"""
[root@huzhi-code subprocess]# python3 10_subprocess_popen_write.py
write:
stdin: to stdin
[root@huzhi-code subprocess]#
"""