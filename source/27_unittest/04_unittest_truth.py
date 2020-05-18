#!/usr/bin/env python3
"""Test for truth
"""

#end_pymotw_header
import unittest


class TruthTest(unittest.TestCase):

    def testAssertTrue(self):
        self.assertTrue(True)

    def testAssertFalse(self):
        self.assertFalse(False)

"""
huzhi@bogon 27_unittest % python3 -m unittest -v 04_unittest_truth.py
testAssertFalse (04_unittest_truth.TruthTest) ... ok
testAssertTrue (04_unittest_truth.TruthTest) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
huzhi@bogon 27_unittest %
"""
