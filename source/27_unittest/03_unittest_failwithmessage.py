#!/usr/bin/env python3
"""A test that fails with a custom message."""

# end_pymotw_header
import unittest


class FailureMessageTest(unittest.TestCase):

    def testFail(self):
        self.assertFalse(True, "failure message goes here")


"""
huzhi@bogon 27_unittest % python3 -m unittest -v 03_unittest_failwithmessage.py
testFail (03_unittest_failwithmessage.FailureMessageTest) ... FAIL

======================================================================
FAIL: testFail (03_unittest_failwithmessage.FailureMessageTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/huzhi/work/code/python3-standard-library-example/source/27_unittest/03_unittest_failwithmessage.py", line 12, in testFail
    self.assertFalse(True, 'failure message goes here')
AssertionError: True is not false : failure message goes here

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
huzhi@bogon 27_unittest %
"""
