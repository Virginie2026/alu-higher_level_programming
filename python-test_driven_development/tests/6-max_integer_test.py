#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestCase class for testing max_integer function"""

    def test_ordered_list(self):
        """Test with an ordered list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list of integers"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test with a list where max is the first element"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_one_element_list(self):
        """Test with a list of one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_floats(self):
        """Test with a list of floats"""
        self.assertEqual(max_integer([1.53, 6.33, -9.12, 14.2, 6.0]), 14.2)

    def test_ints_and_floats(self):
        """Test with a mixed list of ints and floats"""
        self.assertEqual(max_integer([1.53, 15.5, 10, 15, -6]), 15.5)

    def test_string(self):
        """Test with a string argument"""
        self.assertEqual(max_integer("Brennan"), 'z' if 'z' in "Brennan" else 'r')

    def test_list_of_strings(self):
        """Test with a list of strings"""
        self.assertEqual(max_integer(["Brennan", "is", "the", "best"]), "the")

    def test_negative_numbers(self):
        """Test with a list of all negative numbers"""
        self.assertEqual(max_integer([-10, -5, -2, -50]), -2)


if __name__ == '__main__':
    unittest.main()
