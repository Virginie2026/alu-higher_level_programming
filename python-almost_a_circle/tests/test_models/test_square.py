#!/usr/bin/python3
"""Unittests for models/square.py."""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Unittests for testing Square class."""

    def test_valid_instantiation(self):
        s = Square(5, 1, 2, 9)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 9)

    def test_size_setter(self):
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_invalid_size(self):
        with self.assertRaises(TypeError):
            Square("5")
        with self.assertRaises(ValueError):
            Square(-5)

    def test_str(self):
        s = Square(3, 1, 3, 7)
        self.assertEqual(str(s), "[Square] (7) 1/3 - 3")


if __name__ == "__main__":
    unittest.main()
