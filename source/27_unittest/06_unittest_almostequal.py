#!/usr/bin/env python3
"""Test for near equality
"""

#end_pymotw_header
import unittest


class AlmostEqualTest(unittest.TestCase):

    def testEqual(self):
        self.assertEqual(1.1, 3.3 - 2.2)

    def testAlmostEqual(self):
        self.assertAlmostEqual(1.1, 3.3 - 2.2, places=1)

    def testNotAlmostEqual(self):
        self.assertNotAlmostEqual(1.1, 3.3 - 2.0, places=1)

"""
huzhi@bogon 27_unittest % python3 -m unittest -v 06_unittest_almostequal.py
testAlmostEqual (06_unittest_almostequal.AlmostEqualTest) ... ok
testEqual (06_unittest_almostequal.AlmostEqualTest) ... FAIL
testNotAlmostEqual (06_unittest_almostequal.AlmostEqualTest) ... ok

======================================================================
FAIL: testEqual (06_unittest_almostequal.AlmostEqualTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/huzhi/work/code/python3-standard-library-example/source/27_unittest/06_unittest_almostequal.py", line 12, in testEqual
    self.assertEqual(1.1, 3.3 - 2.2)
AssertionError: 1.1 != 1.0999999999999996

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=1)
huzhi@bogon 27_unittest %
"""
