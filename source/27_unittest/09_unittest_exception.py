#!/usr/bin/env python3
"""Unit tests to verify exceptions.
"""

#end_pymotw_header
import unittest


def raises_error(*args, **kwds):
    raise ValueError('Invalid value: ' + str(args) + str(kwds))


class ExceptionTest(unittest.TestCase):

    def testTrapLocally(self):
        try:
            raises_error('a', b='c')
        except ValueError:
            pass
        else:
            self.fail('Did not see ValueError')

    def testAssertRaises(self):
        self.assertRaises(
            ValueError,
            raises_error,
            'a',
            b='c',
        )

"""
huzhi@bogon 27_unittest % python3 -m unittest -v 09_unittest_exception.py
testAssertRaises (09_unittest_exception.ExceptionTest) ... ok
testTrapLocally (09_unittest_exception.ExceptionTest) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
huzhi@bogon 27_unittest %
"""
