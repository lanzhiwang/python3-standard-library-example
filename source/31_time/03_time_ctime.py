#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
""" """

# end_pymotw_header
import time

print("The time is      :", time.ctime())
later = time.time() + 15
print("15 secs from now :", time.ctime(later))

"""
# python 03_time_ctime.py
The time is      : Sun Jul 20 08:45:25 2025
15 secs from now : Sun Jul 20 08:45:40 2025
#
"""
