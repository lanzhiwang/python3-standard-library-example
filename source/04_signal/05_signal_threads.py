#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
信号和线程
信号和线程通常不会很好结合在一起，因为只有进程的主线程才会接受信号。
下列的列子设置了一个信号处理方法，在一个线程中等待信号到达，然后从另一个线程中发送信号。

信号处理程序都在主线程中注册，因为这是 Python 的 signal 模块实现的要求，无论底层平台是否支持线程和信号混合开发。
尽管接收线程调用了 signal.pause()，但是它不会接收到信号。
脚本结束位置的 signal.alarm(2) 阻止了无限循环，否则接收者线程永远不会退出。

"""


#end_pymotw_header
import signal
import threading
import os
import time


def signal_handler(num, stack):
    print('Received signal {} in {}'.format(num, threading.currentThread().name))


signal.signal(signal.SIGUSR1, signal_handler)


def wait_for_signal():
    print('Waiting for signal in', threading.currentThread().name)
    signal.pause()  # signal.pause() 去等待接收一个信号
    print('Done waiting')


# Start a thread that will not receive the signal
receiver = threading.Thread(target=wait_for_signal, name='receiver',)
receiver.start()
time.sleep(0.1)


def send_signal():
    print('Sending signal in', threading.currentThread().name)
    os.kill(os.getpid(), signal.SIGUSR1)

sender = threading.Thread(target=send_signal, name='sender')
sender.start()

# Wait for the thread to see the signal (not going to happen!)
print('Waiting for', receiver.name)
signal.alarm(2)
receiver.join()
sender.join()

"""
('Waiting for signal in', 'receiver')
('Sending signal in', 'sender')
Received signal 10 in MainThread
('Waiting for', 'receiver')
Alarm clock
"""