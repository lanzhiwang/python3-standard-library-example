#!/usr/bin/env python3
"""
"""

#end_pymotw_header
import unittest


class Test(unittest.TestCase):

    @unittest.expectedFailure
    def test_never_passes(self):
        self.assertTrue(False)

    @unittest.expectedFailure
    def test_always_passes(self):
        self.assertTrue(True)

"""
huzhi@bogon 27_unittest % python3 -m unittest -v 14_unittest_expectedfailure.py
test_always_passes (14_unittest_expectedfailure.Test) ... unexpected success
test_never_passes (14_unittest_expectedfailure.Test) ... expected failure

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (expected failures=1, unexpected successes=1)
huzhi@bogon 27_unittest %
"""
