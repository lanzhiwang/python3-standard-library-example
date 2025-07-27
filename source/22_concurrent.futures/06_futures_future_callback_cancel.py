#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016 Doug Hellmann.  All rights reserved.
# Written for https://pymotw.com
#
"""Done callbacks."""

# end_pymotw_header
from concurrent import futures
import time


def task(n):
    print("{}: sleeping".format(n))
    time.sleep(0.5)
    print("{}: done".format(n))
    return n / 10


def done(fn):
    if fn.cancelled():
        print("{}: canceled".format(fn.arg))
    elif fn.done():
        print("{}: not canceled".format(fn.arg))


if __name__ == "__main__":
    ex = futures.ThreadPoolExecutor(max_workers=2)
    print("main: starting")
    tasks = []

    for i in range(10, 0, -1):
        print("main: submitting {}".format(i))
        f = ex.submit(task, i)
        f.arg = i
        f.add_done_callback(done)
        tasks.append((i, f))

    for i, t in reversed(tasks):
        if not t.cancel():
            print("main: did not cancel {}".format(i))

    ex.shutdown()

"""
main: starting
main: submitting 10
10: sleeping
main: submitting 9
9: sleeping
main: submitting 8
main: submitting 7
main: submitting 6
main: submitting 5
main: submitting 4
main: submitting 3
main: submitting 2
main: submitting 1
1: canceled
2: canceled
3: canceled
4: canceled
5: canceled
6: canceled
7: canceled
8: canceled
main: did not cancel 9
main: did not cancel 10
10: done
10: not canceled
9: done
9: not canceled



main: starting
main: submitting 10
main: submitting 9
main: submitting 8
main: submitting 7
main: submitting 6
main: submitting 5
main: submitting 4
main: submitting 3
main: submitting 2
main: submitting 1

10: sleeping
10: done

9: sleeping
9: done

1: canceled
2: canceled
3: canceled
4: canceled
5: canceled
6: canceled
7: canceled
8: canceled

main: did not cancel 9
9: not canceled

main: did not cancel 10
10: not canceled
"""
