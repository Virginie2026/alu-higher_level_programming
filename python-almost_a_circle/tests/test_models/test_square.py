#!/usr/bin/python3
"""Unit tests for the Square class."""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def test_size(self):
        """Test that size sets both width and height."""
        s = Square(4)
        self.assertEqual(s.width, 4)
        self.assertEqual(s.height, 4)
        self.assertEqual(s.size, 4)

    def test_default_x_y(self):
        """Test that x and y default to 0."""
        s = Square(4)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_x_y(self):
        """Test that x and y are correctly set."""
        s = Square(4, 2, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 1)

    def test_custom_id(self):
        """Test that a custom id is correctly set."""
        s = Square(4, 0, 0, 89)
        self.assertEqual(s.id, 89)

    def test_size_type_error(self):
        """Test that a non-integer size raises TypeError."""
        with self.assertRaises(TypeError):
            Square("4")

    def test_size_value_error(self):
        """Test that a size <= 0 raises ValueError."""
        with self.assertRaises(ValueError):
            Square(0)

    def test_area(self):
        """Test the area calculation."""
        s = Square(4)
        self.assertEqual(s.area(), 16)

    def test_str(self):
        """Test the __str__ representation."""
        s = Square(4, 1, 2, 9)
        self.assertEqual(str(s), "[Square] (9) 1/2 - 4")

    def test_size_setter(self):
        """Test setting size after instantiation."""
        s = Square(4)
        s.size = 7
        self.assertEqual(s.width, 7)
        self.assertEqual(s.height, 7)

    def test_update_args(self):
        """Test update with positional arguments."""
        s = Square(4)
        s.update(89, 10, 2, 1)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 1)

    def test_update_kwargs(self):
        """Test update with keyword arguments."""
        s = Square(4)
        s.update(size=10, x=2)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 2)

    def test_to_dictionary(self):
        """Test the dictionary representation."""
        s = Square(4, 1, 2, 9)
        expected = {"id": 9, "size": 4, "x": 1, "y": 2}
        self.assertEqual(s.to_dictionary(), expected)


if __name__ == "__main__":
    unittest.main()
