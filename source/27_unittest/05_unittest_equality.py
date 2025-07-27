#!/usr/bin/env python3
"""Test for equality"""

# end_pymotw_header
import unittest


class EqualityTest(unittest.TestCase):

    def testExpectEqual(self):
        self.assertEqual(1, 3 - 2)

    def testExpectEqualFails(self):
        self.assertEqual(2, 3 - 2)

    def testExpectNotEqual(self):
        self.assertNotEqual(2, 3 - 2)

    def testExpectNotEqualFails(self):
        self.assertNotEqual(1, 3 - 2)


"""
huzhi@bogon 27_unittest % python3 -m unittest -v 05_unittest_equality.py
testExpectEqual (05_unittest_equality.EqualityTest) ... ok
testExpectEqualFails (05_unittest_equality.EqualityTest) ... FAIL
testExpectNotEqual (05_unittest_equality.EqualityTest) ... ok
testExpectNotEqualFails (05_unittest_equality.EqualityTest) ... FAIL

======================================================================
FAIL: testExpectEqualFails (05_unittest_equality.EqualityTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/huzhi/work/code/python3-standard-library-example/source/27_unittest/05_unittest_equality.py", line 15, in testExpectEqualFails
    self.assertEqual(2, 3 - 2)
AssertionError: 2 != 1

======================================================================
FAIL: testExpectNotEqualFails (05_unittest_equality.EqualityTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/huzhi/work/code/python3-standard-library-example/source/27_unittest/05_unittest_equality.py", line 21, in testExpectNotEqualFails
    self.assertNotEqual(1, 3 - 2)
AssertionError: 1 == 1

----------------------------------------------------------------------
Ran 4 tests in 0.000s

FAILED (failures=2)
huzhi@bogon 27_unittest %
"""
