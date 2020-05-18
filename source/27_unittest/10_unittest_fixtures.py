#!/usr/bin/env python3
"""A test with fixtures.
"""

#end_pymotw_header
import random
import unittest


def setUpModule():
    print('In setUpModule()')


def tearDownModule():
    print('In tearDownModule()')


class FixturesTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('In setUpClass()')
        cls.good_range = range(1, 10)

    @classmethod
    def tearDownClass(cls):
        print('In tearDownClass()')
        del cls.good_range

    def setUp(self):
        super().setUp()
        print('\nIn setUp()')
        # Pick a number sure to be in the range. The range is
        # defined as not including the "stop" value, so make
        # sure it is not included in the set of allowed values
        # for our choice.
        self.value = random.randint(
            self.good_range.start,
            self.good_range.stop - 1,
        )

    def tearDown(self):
        print('In tearDown()')
        del self.value
        super().tearDown()

    def test1(self):
        print('In test1()')
        self.assertIn(self.value, self.good_range)

    def test2(self):
        print('In test2()')
        self.assertIn(self.value, self.good_range)

"""
huzhi@bogon 27_unittest % python3 -m unittest -v 10_unittest_fixtures.py
In setUpModule()
In setUpClass()
test1 (10_unittest_fixtures.FixturesTest) ...
In setUp()
In test1()
In tearDown()
ok
test2 (10_unittest_fixtures.FixturesTest) ...
In setUp()
In test2()
In tearDown()
ok
In tearDownClass()
In tearDownModule()

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
huzhi@bogon 27_unittest %
"""
