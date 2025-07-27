#!/usr/bin/env python3
"""Simplistic examples of unit tests."""

# end_pymotw_header
import unittest


class SimplisticTest(unittest.TestCase):

    def test(self):
        a = "a"
        b = "a"
        self.assertEqual(a, b)


"""
huzhi@bogon 27_unittest % python3 -m unittest 01_unittest_simple.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
huzhi@bogon 27_unittest %
huzhi@bogon 27_unittest % python3 -m unittest -v 01_unittest_simple.py
test (01_unittest_simple.SimplisticTest) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
huzhi@bogon 27_unittest %
"""
