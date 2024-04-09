#!/usr/bin/python3
"""
unittest class module
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_empty_list(self):
        """Test case for an empty list."""
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        """Test case for a list with a single element."""
        self.assertEqual(max_integer([5]), 5)

    def test_positive_integers(self):
        """Test case for a list of positive integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_integers(self):
        """Test case for a list of negative integers."""
        self.assertEqual(max_integer([-3, -4, -5, -6]), -3)

    def test_mixed_integers(self):
        """
        Test case for list of mixed positive & negative integers.
        """
        self.assertEqual(max_integer([-2, 2, -5, 7]), 7)

    def test_floats(self):
        """Test case for a list of floats."""
        self.assertEqual(max_integer([1.5, 2.3, 6.7]), 6.7)

    def test_mixed_floats(self):
        """
        Test case for a list of mixed positive and negative floats.
        """
        self.assertEqual(max_integer([-1.5, 4.3, -3.7]), 4.3)

    def test_strings(self):
        """Test case for a list of strings."""
        self.assertEqual(max_integer(["apple", "banana", "lemon"]), "lemon")

    def test_mixed_types(self):
        """Test case for a list of mixed types."""
        self.assertEqual(max_integer([1, "apple", 4.3]), 4.3)

    def test_empty_nested_lists(self):
        """Test case for a list of empty nested lists."""
        self.assertIsNone(max_integer([[], [], []]))

    def test_nested_lists(self):
        """Test case for a list of nested lists."""
        self.assertEqual(max_integer([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 9)

if __name__ == '__main__':
    unittest.main()
