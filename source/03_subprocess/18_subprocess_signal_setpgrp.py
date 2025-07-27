#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
""" """

# end_pymotw_header
import os
import signal
import subprocess
import tempfile
import time
import sys


def show_setting_prgrp():
    print("Calling os.setpgrp() from {}".format(os.getpid()))
    os.setpgrp()
    print("Process group is now {}".format(os.getpgrp()))
    sys.stdout.flush()


script = """#!/bin/sh
echo "Shell script in process $$"
set -x
python3 signal_child.py
"""
script_file = tempfile.NamedTemporaryFile("wt")
script_file.write(script)
script_file.flush()

proc = subprocess.Popen(
    ["sh", script_file.name],
    preexec_fn=show_setting_prgrp,
)
print("PARENT      : Pausing before signaling {}...".format(proc.pid))
sys.stdout.flush()
time.sleep(1)
print("PARENT      : Signaling process group {}".format(proc.pid))
sys.stdout.flush()
os.killpg(proc.pid, signal.SIGUSR1)
time.sleep(3)

"""
[root@huzhi-code subprocess]# python3 18_subprocess_signal_setpgrp.py
Calling os.setpgrp() from 28954
Process group is now 28954
PARENT      : Pausing before signaling 28954...
Shell script in process 28954
+ python3 signal_child.py
CHILD  28955: Setting up signal handler
CHILD  28955: Pausing to wait for signal
PARENT      : Signaling process group 28954
CHILD  28955: Received USR1
[root@huzhi-code subprocess]#
"""
