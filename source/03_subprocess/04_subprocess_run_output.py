#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""
run()
call()  使用 run() 而没有传递 check=True 等价于调用 call()，它仅仅返回进程的退出码。
check_call()  给 run() 方法传递 check=True 等价于调用 check_all()。
check_output()  传入 check=True 以及设置 stdout 为 PIPE 等价于使用 check_output()。
class Popen


"""

# end_pymotw_header
import subprocess

completed = subprocess.run(["ls", "-1"], stdout=subprocess.PIPE)
print("returncode:", completed.returncode)
print(
    "Have {} bytes in stdout:\n{}".format(
        len(completed.stdout), completed.stdout.decode("utf-8")
    )
)

"""
[root@huzhi-code subprocess]# python3 04_subprocess_run_output.py
returncode: 0
Have 115 bytes in stdout:
01_subprocess_os_system.py
02_subprocess_shell_variables.py
03_subprocess_run_check.py
04_subprocess_run_output.py

[root@huzhi-code subprocess]#
"""
