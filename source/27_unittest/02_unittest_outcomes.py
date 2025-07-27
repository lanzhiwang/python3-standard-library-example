#!/usr/bin/env python3
"""Demonstrate possible test outcomes"""

# end_pymotw_header
import unittest


class OutcomesTest(unittest.TestCase):

    def testPass(self):
        return

    def testFail(self):
        self.assertFalse(True)

    def testError(self):
        raise RuntimeError("Test error!")


"""
huzhi@bogon 27_unittest % python3 -m unittest -v 02_unittest_outcomes.py
testError (02_unittest_outcomes.OutcomesTest) ... ERROR
testFail (02_unittest_outcomes.OutcomesTest) ... FAIL
testPass (02_unittest_outcomes.OutcomesTest) ... ok

======================================================================
ERROR: testError (02_unittest_outcomes.OutcomesTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/huzhi/work/code/python3-standard-library-example/source/27_unittest/02_unittest_outcomes.py", line 18, in testError
    raise RuntimeError('Test error!')
RuntimeError: Test error!

======================================================================
FAIL: testFail (02_unittest_outcomes.OutcomesTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/huzhi/work/code/python3-standard-library-example/source/27_unittest/02_unittest_outcomes.py", line 15, in testFail
    self.assertFalse(True)
AssertionError: True is not false

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=1, errors=1)
huzhi@bogon 27_unittest %
"""
