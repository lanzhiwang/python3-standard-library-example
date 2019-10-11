#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""


#end_pymotw_header
import subprocess

print('read:')
proc = subprocess.Popen(
    ['echo', '"to stdout"'],
    stdout=subprocess.PIPE,
)
print(proc.communicate())
stdout_value = proc.communicate()[0].decode('utf-8')
print('stdout:', repr(stdout_value))

"""
[root@huzhi-code subprocess]# python3 09_subprocess_popen_read.py
read:
(b'"to stdout"\n', None)
Traceback (most recent call last):
  File "09_subprocess_popen_read.py", line 19, in <module>
    stdout_value = proc.communicate()[0].decode('utf-8')
  File "/usr/lib64/python3.6/subprocess.py", line 850, in communicate
    stdout = self.stdout.read()
ValueError: read of closed file
[root@huzhi-code subprocess]#
[root@huzhi-code subprocess]# python3 09_subprocess_popen_read.py
read:
stdout: '"to stdout"\n'
[root@huzhi-code subprocess]#
"""