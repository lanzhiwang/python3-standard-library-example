#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""

#end_pymotw_header
import os
import signal
import subprocess
import tempfile
import time
import sys

script = '''#!/bin/sh
echo "Shell script in process $$"
set -x
python3 signal_child.py
'''
script_file = tempfile.NamedTemporaryFile('wt')
script_file.write(script)
script_file.flush()

proc = subprocess.Popen(['sh', script_file.name])
print('PARENT      : Pausing before signaling {}...'.format(proc.pid))
sys.stdout.flush()
time.sleep(1)
print('PARENT      : Signaling child {}'.format(proc.pid))
sys.stdout.flush()
os.kill(proc.pid, signal.SIGUSR1)
time.sleep(3)

"""
[root@huzhi-code subprocess]# python3 17_subprocess_signal_parent_shell.py
PARENT      : Pausing before signaling 28949...
Shell script in process 28949
+ python3 signal_child.py
CHILD  28950: Setting up signal handler
CHILD  28950: Pausing to wait for signal
PARENT      : Signaling child 28949
CHILD  28950: Never received signal
[root@huzhi-code subprocess]#
"""