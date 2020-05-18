#!/usr/bin/env python3
"""
"""

#end_pymotw_header
import unittest


class SubTest(unittest.TestCase):

    def test_combined(self):
        self.assertRegex('abc', 'a')
        self.assertRegex('abc', 'B')
        # The next assertions are not verified!
        self.assertRegex('abc', 'c')
        self.assertRegex('abc', 'd')

    def test_with_subtest(self):
        for pat in ['a', 'B', 'c', 'd']:
            with self.subTest(pattern=pat):
                self.assertRegex('abc', pat)

"""
huzhi@bogon 27_unittest % python3 -m unittest -v 12_unittest_subtest.py
test_combined (12_unittest_subtest.SubTest) ... FAIL
test_with_subtest (12_unittest_subtest.SubTest) ...
======================================================================
FAIL: test_combined (12_unittest_subtest.SubTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/huzhi/work/code/python3-standard-library-example/source/27_unittest/12_unittest_subtest.py", line 13, in test_combined
    self.assertRegex('abc', 'B')
AssertionError: Regex didn't match: 'B' not found in 'abc'

======================================================================
FAIL: test_with_subtest (12_unittest_subtest.SubTest) (pattern='B')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/huzhi/work/code/python3-standard-library-example/source/27_unittest/12_unittest_subtest.py", line 21, in test_with_subtest
    self.assertRegex('abc', pat)
AssertionError: Regex didn't match: 'B' not found in 'abc'

======================================================================
FAIL: test_with_subtest (12_unittest_subtest.SubTest) (pattern='d')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/huzhi/work/code/python3-standard-library-example/source/27_unittest/12_unittest_subtest.py", line 21, in test_with_subtest
    self.assertRegex('abc', pat)
AssertionError: Regex didn't match: 'd' not found in 'abc'

----------------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (failures=3)
huzhi@bogon 27_unittest %
"""
