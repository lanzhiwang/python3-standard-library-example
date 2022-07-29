#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
信号是一种操作系统的功能，它提供了一种通知事件程序并使其异步处理的方法。
他们可以由系统本身生成或者从一个进程发送到另一个进程。
由于信号会中断程序的常规流程，因此如果在操作中间接收到信号，某些操作（尤其是 I/O）可能会产生错误。

信号由整数标识，并在操作系统中 C 的头文件中定义。
Python 将适配于各个平台的信号定义在了 signal 模块的常量中。
这个模块中使用了 SIGINT 以及 SIGUSR1。两者通常都是针对所有 Unix 和 类 Unix 系统定义。

提醒
Unix 信号编程是一项不小的工作。
本篇只是一个介绍，并不包括在每个平台上成功使用信号所需的详细信息。
不同的 Unix 版本虽然有一定程度的标准化，但是也有一些变化，所以如果遇到麻烦，请查阅操作系统文档。


接收信号
与其他形式的基于事件编程一样，通过创建一个称之为 信号处理器 的回调函数接收信号，
这个函数在信号发生时调用。信号处理器的参数是信号编号以及被信号中断的那个时间点的程序堆栈帧。

这个例子无限循环，每次中断几秒。当信号到来时，sleep() 调用被中断，同时信号处理函数 receive_signal 打印出来了信号编号。
在信号处理器返回之后，循环继续。

可以使用 os.kill() 或者 Unix 命令行程序 kill 给运行中的进程发送信号。

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


前面的输出是由运行 signal_signal.py 在一个窗口中产生的，然后另一个窗口运行：

[root@huzhi-code ~]# kill -USR1 29012
[root@huzhi-code ~]# kill -INT 29012
[root@huzhi-code ~]#


系统支持的所有信号
% kill -l
HUP INT QUIT ILL TRAP ABRT EMT FPE KILL BUS SEGV SYS PIPE ALRM TERM URG STOP
TSTP CONT CHLD TTIN TTOU IO XCPU XFSZ VTALRM PROF WINCH INFO USR1 USR2

SIG HUP       终止进程, 终端线路挂断
SIG INT       终止进程, 中断进程
SIG QUIT      建立 CORE 文件, 终止进程, 并且生成 core 文件
SIG ILL       建立 CORE 文件, 非法指令
SIG TRAP      建立 CORE 文件, 跟踪自陷
SIG BUS       建立 CORE 文件, 总线错误
SIG SEGV      建立 CORE 文件, 段非法错误
SIG FPE       建立 CORE 文件, 浮点异常
SIG IOT       建立 CORE 文件, 执行I/O自陷
SIG KILL      终止进程, 杀死进程
SIG PIPE      终止进程, 向一个没有读进程的管道写数据
SIG ALARM     终止进程, 计时器到时
SIG TERM      终止进程, 软件终止信号
SIG STOP      停止进程, 非终端来的停止信号
SIG TSTP      停止进程, 终端来的停止信号
SIG CONT      忽略信号, 继续执行一个停止的进程
SIG URG       忽略信号, I/O 紧急信号
SIG IO        忽略信号, 描述符上可以进行 I/O
SIG CHLD      忽略信号, 当子进程停止或退出时通知父进程
SIG TTOU      停止进程, 后台进程写终端
SIG TTIN      停止进程, 后台进程读终端
SIG XGPU      终止进程, CPU 时限超时
SIG XFSZ      终止进程, 文件长度过长
SIG WINCH     忽略信号, 窗口大小发生变化
SIG PROF      终止进程, 统计分布图用计时器到时
SIG USR1      终止进程, 用户定义信号1
SIG USR2      终止进程, 用户定义信号2
SIG VTALRM    终止进程, 虚拟计时器到时

"""