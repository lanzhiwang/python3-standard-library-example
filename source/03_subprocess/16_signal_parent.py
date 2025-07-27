#!/usr/bin/env python3
"""Illustrate using Unix signals and subprocess."""

# end_pymotw_header
import os
import signal
import subprocess
import time
import sys

proc = subprocess.Popen(["python3", "signal_child.py"])
print("PARENT      : Pausing before sending signal...")
sys.stdout.flush()
time.sleep(1)
print("PARENT      : Signaling child")
sys.stdout.flush()
os.kill(proc.pid, signal.SIGUSR1)

"""
[root@huzhi-code subprocess]# python3 16_signal_parent.py
PARENT      : Pausing before sending signal...
CHILD  28939: Setting up signal handler
CHILD  28939: Pausing to wait for signal
PARENT      : Signaling child
CHILD  28939: Received USR1
[root@huzhi-code subprocess]#
[root@huzhi-code subprocess]# python3 16_signal_parent.py
PARENT      : Pausing before sending signal...
CHILD  28941: Setting up signal handler
CHILD  28941: Pausing to wait for signal
PARENT      : Signaling child
CHILD  28941: Received USR1
[root@huzhi-code subprocess]#
[root@huzhi-code subprocess]# python3 16_signal_parent.py
PARENT      : Pausing before sending signal...
CHILD  28943: Setting up signal handler
CHILD  28943: Pausing to wait for signal
PARENT      : Signaling child
CHILD  28943: Received USR1
[root@huzhi-code subprocess]#
"""
