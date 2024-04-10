#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_normal_list(self):
        """Test normal list integer"""
        N_list = [0, 1, 2, 3]
        self.assertEqual(max_integer(N_list), 3)

    def testlistorderd(self):
        """Test ordered int in list"""
        Or_list = [7, 8, 9]
        self.assertEqual(max_integer(Or_list), 9)

    def testun_ord_list(self):
        """Test unordered int in list"""
        UN_list = [5, 8, 1]
        self.assertEqual(max_integer(UN_list), 8)

    def testemtylist(self):
        "test empty lis"
        em = []
        self.assertEqual(max_integer(em), None)

    def testfloat(self):
        "test list float"
        F = [2.5, 3.6, 4.5, 3.2, 8.7]
        self.assertEqual(max_integer(F), 8.7)


if __name__ == '__main__':
    unittest.main()
