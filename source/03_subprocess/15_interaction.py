#!/usr/bin/env python3
"""More interaction between child processes."""

# end_pymotw_header
import io
import subprocess

print("One line at a time:")
proc = subprocess.Popen(
    "python3 repeater.py",
    shell=True,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
)
stdin = io.TextIOWrapper(
    proc.stdin,
    encoding="utf-8",
    line_buffering=True,  # send data on newline
)
stdout = io.TextIOWrapper(
    proc.stdout,
    encoding="utf-8",
)
for i in range(5):
    line = "{}\n".format(i)
    stdin.write(line)
    output = stdout.readline()
    print(output.rstrip())
remainder = proc.communicate()[0].decode("utf-8")
# print(remainder)
"""
One line at a time:
repeater.py: starting
0
1
2
3
4
repeater.py: exiting
"""

print()
print("All output at once:")
proc = subprocess.Popen(
    "python3 repeater.py",
    shell=True,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
)
stdin = io.TextIOWrapper(
    proc.stdin,
    encoding="utf-8",
)
for i in range(5):
    line = "{}\n".format(i)
    stdin.write(line)
stdin.flush()

output = proc.communicate()[0].decode("utf-8")
print(output)

"""
All output at once:
repeater.py: starting
repeater.py: exiting
0
1
2
3
4

"""
