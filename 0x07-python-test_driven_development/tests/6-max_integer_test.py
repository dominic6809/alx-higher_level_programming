#!/usr/bin/python3
"""
unittest class module
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test for max integer"""

    def test_max_integer(self):
        """
        Test all possible occurences of max integers
        """
        self.assertIsNone(max_integer([]))
        self.assertAlmostEqual(max_integer([2, 3, 4, 5, 6]), 6)
        self.assertAlmostEqual(max_integer([-4, -3, -2, -1, 0]), 0)
        self.assertAlmostEqual(max_integer([-90, -120, -150, -180]), -90)
        self.assertAlmostEqual(max_integer([1.2, 1.5, 1.6, 5.7, 2.5]), 5.7)
        self.assertAlmostEqual(max_integer([9.9]), 9.9)

    def test_wrong_types(self):
        """
        Test max integer with wrong parameters types
        """
        with self.assertRaises(TypeError):
            max_integer(None)

        with self.assertRaises(TypeError):
            max_integer(["Monty", 89, 34, -9.7, "Python"])
