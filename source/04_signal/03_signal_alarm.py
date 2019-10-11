#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""


#end_pymotw_header
import signal
import time


def receive_alarm(signum, stack):
    print('Alarm :', time.ctime())


# Call receive_alarm in 2 seconds
signal.signal(signal.SIGALRM, receive_alarm)
signal.alarm(2)

print('Before:', time.ctime())
time.sleep(4)
print('After :', time.ctime())

"""
('Before:', 'Fri Oct 11 13:40:30 2019')
('Alarm :', 'Fri Oct 11 13:40:32 2019')
('After :', 'Fri Oct 11 13:40:32 2019')
"""