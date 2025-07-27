#!/usr/bin/env python3
#
# Copyright 2010 Doug Hellmann.
#
"""Checking exit codes from external processes"""

# end_pymotw_header
import subprocess

try:
    subprocess.run(["false"], check=True)
except subprocess.CalledProcessError as err:
    print("ERROR:", err)

"""
[root@huzhi-code subprocess]# python3 03_subprocess_run_check.py
ERROR: Command '['false']' returned non-zero exit status 1.
[root@huzhi-code subprocess]#
"""
