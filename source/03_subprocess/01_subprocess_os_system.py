#!/usr/bin/env python3
"""
run()
call()
check_call()
check_output()
class Popen

"""

# end_pymotw_header
import subprocess

completed = subprocess.run(["ls", "-1"])
print(completed)
print("returncode:", completed.returncode)

"""
[root@huzhi-code subprocess]# python3 01_subprocess_os_system.py
01_subprocess_os_system.py
02_subprocess_shell_variables.py
03_subprocess_run_check.py
CompletedProcess(args=['ls', '-1'], returncode=0)
returncode: 0
[root@huzhi-code subprocess]#
"""
