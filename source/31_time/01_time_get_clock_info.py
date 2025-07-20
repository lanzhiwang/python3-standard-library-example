#!/usr/bin/env python3
# encoding: utf-8
#
"""The difference between clock and time.
"""

#end_pymotw_header
import textwrap
import time

available_clocks = [
    ('monotonic', time.monotonic),
    ('perf_counter', time.perf_counter),
    ('process_time', time.process_time),
    ('time', time.time),
]

for clock_name, func in available_clocks:
    print(textwrap.dedent('''\
    {name}:
        adjustable    : {info.adjustable}
        implementation: {info.implementation}
        monotonic     : {info.monotonic}
        resolution    : {info.resolution}
        current       : {current}
    ''').format(
        name=clock_name,
        info=time.get_clock_info(clock_name),
        current=func())
    )

"""
$ python 01_time_get_clock_info.py
monotonic:
    adjustable    : False
    implementation: clock_gettime(CLOCK_MONOTONIC)
    monotonic     : True
    resolution    : 0.001
    current       : 19.442757686

perf_counter:
    adjustable    : False
    implementation: clock_gettime(CLOCK_MONOTONIC)
    monotonic     : True
    resolution    : 0.001
    current       : 19.443940194

process_time:
    adjustable    : False
    implementation: clock_gettime(CLOCK_PROCESS_CPUTIME_ID)
    monotonic     : True
    resolution    : 1e-09
    current       : 0.088659678

time:
    adjustable    : True
    implementation: clock_gettime(CLOCK_REALTIME)
    monotonic     : False
    resolution    : 0.001
    current       : 1753000837.614081

$
"""