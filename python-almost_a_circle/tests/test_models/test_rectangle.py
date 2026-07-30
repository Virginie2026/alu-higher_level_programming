#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import unittest
import os
import io
import sys
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def setUp(self):
        """Reset Base nb_objects counter and clean files."""
        Base._Base__nb_objects = 0
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def tearDown(self):
        """Clean created files after test."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def test_rectangle_instantiation(self):
        """Test Rectangle creation with various parameters."""
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        r2 = Rectangle(1, 2, 3)
        self.assertEqual(r2.x, 3)
        r3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r3.y, 4)
        r4 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r4.id, 5)

    def test_rectangle_type_errors(self):
        """Test type exceptions."""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_rectangle_value_errors(self):
        """Test value exceptions."""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        """Test area method."""
        r = Rectangle(3, 5)
        self.assertEqual(r.area(), 15)

    def test_str(self):
        """Test __str__ representation."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (5) 3/4 - 1/2")

    def test_display(self):
        """Test display method stdout output."""
        r1 = Rectangle(2, 2)
        captured = io.StringIO()
        sys.stdout = captured
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "##\n##\n")

        r2 = Rectangle(2, 2, 2)
        captured = io.StringIO()
        sys.stdout = captured
        r2.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "  ##\n  ##\n")

        r3 = Rectangle(2, 2, 1, 2)
        captured = io.StringIO()
        sys.stdout = captured
        r3.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n\n ##\n ##\n")

    def test_to_dictionary(self):
        """Test to_dictionary method."""
        r = Rectangle(1, 2, 3, 4, 5)
        d = r.to_dictionary()
        self.assertEqual(d, {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4})

    def test_update(self):
        """Test update method with args and kwargs."""
        r = Rectangle(1, 1)
        r.update()
        r.update(89)
        self.assertEqual(r.id, 89)
        r.update(89, 1)
        self.assertEqual(r.width, 1)
        r.update(89, 1, 2)
        self.assertEqual(r.height, 2)
        r.update(89, 1, 2, 3)
        self.assertEqual(r.x, 3)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(r.y, 4)
        r.update(**{'id': 89})
        self.assertEqual(r.id, 89)
        r.update(**{'id': 89, 'width': 1})
        self.assertEqual(r.width, 1)
        r.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.height, 2)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.x, 3)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.y, 4)

    def test_create(self):
        """Test create class method."""
        r1 = Rectangle.create(**{'id': 89})
        self.assertEqual(r1.id, 89)
        r2 = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(r2.width, 1)
        r3 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r3.height, 2)
        r4 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r4.x, 3)
        r5 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r5.y, 4)

    def test_save_to_file(self):
        """Test save_to_file class method."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        Rectangle.save_to_file([Rectangle(1, 2, 0, 0, 1)])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) > 0)

    def test_load_from_file(self):
        """Test load_from_file class method."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])
        Rectangle.save_to_file([Rectangle(1, 2, 0, 0, 1)])
        objs = Rectangle.load_from_file()
        self.assertEqual(len(objs), 1)
        self.assertIsInstance(objs[0], Rectangle)


if __name__ == "__main__":
    unittest.main()
