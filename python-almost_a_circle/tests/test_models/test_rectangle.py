#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def test_width_height(self):
        """Test that width and height are correctly set."""
        r = Rectangle(3, 5)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 5)

    def test_default_x_y(self):
        """Test that x and y default to 0."""
        r = Rectangle(3, 5)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_x_y(self):
        """Test that x and y are correctly set."""
        r = Rectangle(3, 5, 2, 1)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 1)

    def test_custom_id(self):
        """Test that a custom id is correctly set."""
        r = Rectangle(3, 5, 0, 0, 89)
        self.assertEqual(r.id, 89)

    def test_width_type_error(self):
        """Test that a non-integer width raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle("3", 5)

    def test_height_type_error(self):
        """Test that a non-integer height raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(3, "5")

    def test_x_type_error(self):
        """Test that a non-integer x raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(3, 5, "0")

    def test_y_type_error(self):
        """Test that a non-integer y raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(3, 5, 0, "0")

    def test_width_value_error(self):
        """Test that a width <= 0 raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(0, 5)

    def test_height_value_error(self):
        """Test that a height <= 0 raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(3, -1)

    def test_x_value_error(self):
        """Test that a negative x raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(3, 5, -1)

    def test_y_value_error(self):
        """Test that a negative y raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(3, 5, 0, -1)

    def test_area(self):
        """Test the area calculation."""
        r = Rectangle(3, 5)
        self.assertEqual(r.area(), 15)

    def test_str(self):
        """Test the __str__ representation."""
        r = Rectangle(3, 5, 1, 2, 9)
        self.assertEqual(str(r), "[Rectangle] (9) 1/2 - 3/5")

    def test_update_args(self):
        """Test update with positional arguments."""
        r = Rectangle(3, 5)
        r.update(89, 10, 2, 1, 2)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)

    def test_update_kwargs(self):
        """Test update with keyword arguments."""
        r = Rectangle(3, 5)
        r.update(width=10, height=2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)

    def test_to_dictionary(self):
        """Test the dictionary representation."""
        r = Rectangle(3, 5, 1, 2, 9)
        expected = {"id": 9, "width": 3, "height": 5, "x": 1, "y": 2}
        self.assertEqual(r.to_dictionary(), expected)


if __name__ == "__main__":
    unittest.main()
