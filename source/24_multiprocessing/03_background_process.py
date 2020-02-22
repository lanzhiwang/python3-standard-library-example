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
    name = multiprocessing.current_process().name
    print ("Starting %s" %name)
    time.sleep(3)
    print ("Exiting %s" %name)
    

if __name__ == '__main__':
    background_process = multiprocessing.Process(name='background_process', target=foo)
    background_process.daemon = True

    no_background_process = multiprocessing.Process(name='no_background_process', target=foo)
    no_background_process.daemon = False
    
    background_process.start()
    no_background_process.start()

"""
Starting no_background_process
Exiting no_background_process
"""