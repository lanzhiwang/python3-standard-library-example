#!/usr/bin/env python3
"""
"""

#end_pymotw_header
import sys
import unittest


class SkippingTest(unittest.TestCase):

    @unittest.skip('always skipped')
    def test(self):
        self.assertTrue(False)

    @unittest.skipIf(sys.version_info[0] > 2,
                     'only runs on python 2')
    def test_python2_only(self):
        self.assertTrue(False)

    @unittest.skipUnless(sys.platform == 'Darwin',
                         'only runs on macOS')
    def test_macos_only(self):
        self.assertTrue(True)

    def test_raise_skiptest(self):
        raise unittest.SkipTest('skipping via exception')

"""
huzhi@bogon 27_unittest % python3 -m unittest -v 13_unittest_skip.py
test (13_unittest_skip.SkippingTest) ... skipped 'always skipped'
test_macos_only (13_unittest_skip.SkippingTest) ... skipped 'only runs on macOS'
test_python2_only (13_unittest_skip.SkippingTest) ... skipped 'only runs on python 2'
test_raise_skiptest (13_unittest_skip.SkippingTest) ... skipped 'skipping via exception'

----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK (skipped=4)
huzhi@bogon 27_unittest %
"""
