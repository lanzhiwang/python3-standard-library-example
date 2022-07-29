#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
忽略信号
为了忽略信号，注册 SIG_IGN 为信号处理方法。
这个脚本中将信号 SIGINT 的处理方法替换为 SIG_IGN，
并且为信号 SIGUSR1 注册了一个处理方法。
然后使用 signal.pause() 去等待接收一个信号。


正常的 SIGINT （通过 Ctrl-C 由 shell 发送给 程序的信号）会引发 KeyboardInterrupt。 这个例子中忽略了 SIGINT
然而当接收到信号 SIGUSR1 时会引起 SystemExit。
输出中的每个 ^C 表示尝试在终端使用 Ctrl-C 杀死程序。
从另一个终端使用 kill -USR1 72598 最终造成程序退出。

"""


#end_pymotw_header
import signal
import os
import time


def do_exit(sig, stack):
    raise SystemExit('Exiting')


signal.signal(signal.SIGINT, signal.SIG_IGN)
signal.signal(signal.SIGUSR1, do_exit)

print('My PID:', os.getpid())

signal.pause()  # signal.pause() 去等待接收一个信号

"""
$ python3 signal_ignore.py

My PID: 72598
^C^C^C^CExiting
"""
