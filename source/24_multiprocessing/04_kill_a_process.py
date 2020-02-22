#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Spawn a Process – Chapter 3: Process Based Parallelism
"""
#end_pymotw_header
import multiprocessing
import time

def foo():
    print ('Starting function')
    time.sleep(10)
    print ('Finished function')


if __name__ == '__main__':
    p = multiprocessing.Process(target=foo)
    print('Process before execution:', p, p.is_alive())
    
    p.start()
    print('Process running:', p, p.is_alive())
    
    # p.terminate()
    print('Process terminated:', p, p.is_alive())

    p.join()
    print('Process joined:', p, p.is_alive())

    print('Process exit code:', p.exitcode)

"""
Process before execution: <Process(Process-1, initial)> False
Process running: <Process(Process-1, started)> True
Process terminated: <Process(Process-1, started)> True
Process joined: <Process(Process-1, stopped[SIGTERM])> False
Process exit code: -15
"""
