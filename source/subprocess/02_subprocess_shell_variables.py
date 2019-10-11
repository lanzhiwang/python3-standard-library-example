#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
run()
call()  使用 run() 而没有传递 check=True 等价于调用 call()，它仅仅返回进程的退出码。
check_call()  给 run() 方法传递 check=True 等价于调用 check_all()。
check_output()
class Popen
"""

#end_pymotw_header
import subprocess

completed = subprocess.run('echo $HOME', shell=True)
print('returncode:', completed.returncode)
