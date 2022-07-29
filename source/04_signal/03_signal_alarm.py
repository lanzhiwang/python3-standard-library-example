#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
警报
警报是一种特殊的信号，程序要求操作系统在一段时间之后再去通知它。
由标准模块 os 的文档指出，这对于在系统 I/O 操作或者其他系统调用中无限阻塞。

# Call receive_alarm in 2 seconds
signal.signal(signal.SIGALRM, receive_alarm)
signal.alarm(2)

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