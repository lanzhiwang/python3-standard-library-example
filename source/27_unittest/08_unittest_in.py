#!/usr/bin/env python3
"""Test for equality"""

# end_pymotw_header
import unittest


class ContainerMembershipTest(unittest.TestCase):

    def testDict(self):
        self.assertIn(4, {1: "a", 2: "b", 3: "c"})

    def testList(self):
        self.assertIn(4, [1, 2, 3])

    def testSet(self):
        self.assertIn(4, set([1, 2, 3]))


"""
huzhi@bogon 27_unittest % python3 -m unittest -v 08_unittest_in.py
testDict (08_unittest_in.ContainerMembershipTest) ... FAIL
testList (08_unittest_in.ContainerMembershipTest) ... FAIL
testSet (08_unittest_in.ContainerMembershipTest) ... FAIL

======================================================================
FAIL: testDict (08_unittest_in.ContainerMembershipTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/huzhi/work/code/python3-standard-library-example/source/27_unittest/08_unittest_in.py", line 12, in testDict
    self.assertIn(4, {1: 'a', 2: 'b', 3: 'c'})
AssertionError: 4 not found in {1: 'a', 2: 'b', 3: 'c'}

======================================================================
FAIL: testList (08_unittest_in.ContainerMembershipTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/huzhi/work/code/python3-standard-library-example/source/27_unittest/08_unittest_in.py", line 15, in testList
    self.assertIn(4, [1, 2, 3])
AssertionError: 4 not found in [1, 2, 3]

======================================================================
FAIL: testSet (08_unittest_in.ContainerMembershipTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/huzhi/work/code/python3-standard-library-example/source/27_unittest/08_unittest_in.py", line 18, in testSet
    self.assertIn(4, set([1, 2, 3]))
AssertionError: 4 not found in {1, 2, 3}

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=3)
huzhi@bogon 27_unittest %
"""
