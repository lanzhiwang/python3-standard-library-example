#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
""" """

# end_pymotw_header
import multiprocessing
import sys
import time


def exit_error():
    sys.exit(1)


def exit_ok():
    return


def return_value():
    return 1


def raises():
    raise RuntimeError("There was an error!")


def terminated():
    time.sleep(3)


if __name__ == "__main__":
    jobs = []
    funcs = [
        exit_error,
        exit_ok,
        return_value,
        raises,
        terminated,
    ]
    for f in funcs:
        print("Starting process for", f.__name__)
        j = multiprocessing.Process(target=f, name=f.__name__)
        jobs.append(j)
        j.start()

    jobs[-1].terminate()

    for j in jobs:
        j.join()
        print("{:>15}.exitcode = {}".format(j.name, j.exitcode))

"""
$ python 09_multiprocessing_exitcode.py
Starting process for exit_error
Starting process for exit_ok
Starting process for return_value
Starting process for raises
Starting process for terminated
     exit_error.exitcode = 1
        exit_ok.exitcode = 0
   return_value.exitcode = 0
Process raises:
Traceback (most recent call last):
  File "/usr/local/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/lib/python3.12/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/python3-standard-library-example/source/24_multiprocessing/09_multiprocessing_exitcode.py", line 27, in raises
    raise RuntimeError("There was an error!")
RuntimeError: There was an error!
         raises.exitcode = 1
     terminated.exitcode = -15
$
"""
