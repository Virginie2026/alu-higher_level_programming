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

    def test_rectangle_exists_1_2(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)

    def test_rectangle_exists_1_2_3(self):
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.x, 3)

    def test_rectangle_exists_1_2_3_4(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.y, 4)

    def test_rectangle_exists_str_width(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_rectangle_exists_str_height(self):
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_rectangle_exists_str_x(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_rectangle_exists_str_y(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_rectangle_exists_5_args(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 5)

    def test_rectangle_negative_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_rectangle_negative_height(self):
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_rectangle_zero_width(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_rectangle_zero_height(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_rectangle_negative_x(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_rectangle_negative_y(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        r = Rectangle(3, 5)
        self.assertEqual(r.area(), 15)

    def test_str(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (5) 3/4 - 1/2")

    def test_display_without_x_and_y(self):
        r = Rectangle(2, 2)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "##\n##\n")

    def test_display_without_y(self):
        r = Rectangle(2, 2, 2)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "  ##\n  ##\n")

    def test_display(self):
        r = Rectangle(2, 2, 1, 2)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n\n ##\n ##\n")

    def test_to_dictionary(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.to_dictionary(), {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4})

    def test_update_empty(self):
        r = Rectangle(1, 1)
        r.update()

    def test_update_89(self):
        r = Rectangle(1, 1)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_89_1(self):
        r = Rectangle(1, 1)
        r.update(89, 1)
        self.assertEqual(r.width, 1)

    def test_update_89_1_2(self):
        r = Rectangle(1, 1)
        r.update(89, 1, 2)
        self.assertEqual(r.height, 2)

    def test_update_89_1_2_3(self):
        r = Rectangle(1, 1)
        r.update(89, 1, 2, 3)
        self.assertEqual(r.x, 3)

    def test_update_89_1_2_3_4(self):
        r = Rectangle(1, 1)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(r.y, 4)

    def test_update_kwargs_id(self):
        r = Rectangle(1, 1)
        r.update(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_update_kwargs_id_width(self):
        r = Rectangle(1, 1)
        r.update(**{'id': 89, 'width': 1})
        self.assertEqual(r.width, 1)

    def test_update_kwargs_id_width_height(self):
        r = Rectangle(1, 1)
        r.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.height, 2)

    def test_update_kwargs_id_width_height_x(self):
        r = Rectangle(1, 1)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.x, 3)

    def test_update_kwargs_id_width_height_x_y(self):
        r = Rectangle(1, 1)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.y, 4)

    def test_create_id(self):
        r = Rectangle.create(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_create_id_width(self):
        r = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(r.width, 1)

    def test_create_id_width_height(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.height, 2)

    def test_create_id_width_height_x(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.x, 3)

    def test_create_id_width_height_x_y(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.y, 4)

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty_list(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_rect(self):
        Rectangle.save_to_file([Rectangle(1, 2, 0, 0, 1)])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) > 0)

    def test_load_from_file_no_file(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_file_exists(self):
        Rectangle.save_to_file([Rectangle(1, 2, 0, 0, 1)])
        objs = Rectangle.load_from_file()
        self.assertEqual(len(objs), 1)


if __name__ == "__main__":
    unittest.main()
