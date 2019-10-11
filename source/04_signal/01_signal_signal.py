#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""


#end_pymotw_header
import signal
import os
import time


def receive_signal(signum, stack):
    print('Received:', signum)


# Register signal handlers
signal.signal(signal.SIGUSR1, receive_signal)
signal.signal(signal.SIGUSR2, receive_signal)

# Print the process ID so it can be used with 'kill'
# to send this program signals.
print('My PID is:', os.getpid())

while True:
    print('Waiting...')
    time.sleep(3)


"""
[root@huzhi-code 04_signal]# python 01_signal_signal.py
('My PID is:', 29012)
Waiting...
Waiting...
Waiting...
('Received:', 10)
Waiting...
Waiting...
Traceback (most recent call last):
  File "01_signal_signal.py", line 30, in <module>
    time.sleep(3)
KeyboardInterrupt
[root@huzhi-code 04_signal]#

[root@huzhi-code ~]# kill -USR1 29012
[root@huzhi-code ~]# kill -INT 29012
[root@huzhi-code ~]#
"""