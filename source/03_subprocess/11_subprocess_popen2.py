#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
""" """


# end_pymotw_header
import subprocess

print("popen2:")

proc = subprocess.Popen(
    ["cat", "-"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
)
msg = "through stdin to stdout".encode("utf-8")
stdout_value = proc.communicate(msg)[0].decode("utf-8")
print("pass through:", repr(stdout_value))

"""
[root@huzhi-code subprocess]# python3 11_subprocess_popen2.py
popen2:
pass through: 'through stdin to stdout'
[root@huzhi-code subprocess]#
"""
