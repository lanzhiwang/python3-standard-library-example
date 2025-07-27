#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""
Capture the output of a command and
test its exit code at the same time.
"""

# end_pymotw_header
import subprocess

try:
    completed = subprocess.run(
        "echo to stdout; echo to stderr 1>&2; exit 1",
        check=True,
        shell=True,
        stdout=subprocess.PIPE,
    )
except subprocess.CalledProcessError as err:
    print("ERROR:", err)
else:
    print("returncode:", completed.returncode)
    print(
        "Have {} bytes in stdout: {!r}".format(
            len(completed.stdout), completed.stdout.decode("utf-8")
        )
    )

"""
[root@huzhi-code subprocess]# python3 05_subprocess_run_output_error.py
to stderr
ERROR: Command 'echo to stdout; echo to stderr 1>&2; exit 1' returned non-zero exit status 1.
[root@huzhi-code subprocess]#
"""
