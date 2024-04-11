#!/usr/bin/python3
"""
unittest class module
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test for max integer"""

    def test_basic_check(self):
        """Basic Check"""
        self.assertEqual(max_integer([5, 30, 74]), 74)

    def test_the_same_check(self):
        """Test the same numbers"""
        self.assertEqual(max_integer([5, 5, 5]), 5)

    def test_begin_check(self):
        """Test the beginning numbers"""
        self.assertEqual(max_integer([180, 3, 7]), 180)

    def test_middle_check(self):
        """Test the middle numbers"""
        self.assertEqual(max_integer([7, 63, 7]), 63)

    def test_one_neg_check(self):
        """Test one negative numbers"""
        self.assertEqual(max_integer([6, 83, -33]), 83)

    def test_neg_check(self):
        """Test only negative numbers"""
        self.assertEqual(max_integer([-6, -83, -33]), -6)

    def test_one_check(self):
        """Test only one number"""
        self.assertEqual(max_integer([-5]), -5)

    def test_empty_check(self):
        """Test empty list"""
        self.assertFalse(max_integer([]))

    def test_non_integer_check(self):
        """Test list with non integer elements"""
        with self.assertRaises(TypeError):
            max_integer([23, "23", 233])


if __name__ == '__main__':
    unittest.main()
