#!/usr/bin/env python3
"""
"""

#end_pymotw_header
import random
import shutil
import tempfile
import unittest


def remove_tmpdir(dirname):
    print('In remove_tmpdir()')
    shutil.rmtree(dirname)


class FixturesTest(unittest.TestCase):

    def setUp(self):
        super().setUp()
        print('\nIn setUp()')
        self.tmpdir = tempfile.mkdtemp()
        self.addCleanup(remove_tmpdir, self.tmpdir)

    def test1(self):
        print('\nIn test1()')

    def test2(self):
        print('\nIn test2()')

"""
huzhi@bogon 27_unittest % python3 -m unittest -v 11_unittest_addcleanup.py
test1 (11_unittest_addcleanup.FixturesTest) ...
In setUp()

In test1()
In remove_tmpdir()
ok
test2 (11_unittest_addcleanup.FixturesTest) ...
In setUp()

In test2()
In remove_tmpdir()
ok

----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
huzhi@bogon 27_unittest %
"""
