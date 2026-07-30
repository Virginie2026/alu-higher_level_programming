#!/usr/bin/python3
"""Unit tests for the Square class."""
import unittest
import os
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def setUp(self):
        """Reset Base nb_objects counter and clean files."""
        Base._Base__nb_objects = 0
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def tearDown(self):
        """Clean created files after test."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_square_1(self):
        s = Square(1)
        self.assertEqual(s.size, 1)

    def test_square_1_2(self):
        s = Square(1, 2)
        self.assertEqual(s.x, 2)

    def test_square_1_2_3(self):
        s = Square(1, 2, 3)
        self.assertEqual(s.y, 3)

    def test_square_str_size(self):
        with self.assertRaises(TypeError):
            Square("1")

    def test_square_str_x(self):
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_square_str_y(self):
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_square_1_2_3_4(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.id, 4)

    def test_square_negative_size(self):
        with self.assertRaises(ValueError):
            Square(-1)

    def test_square_negative_x(self):
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_square_negative_y(self):
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_square_zero_size(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_str(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (4) 2/3 - 1")

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 1)
        self.assertEqual(s.to_dictionary(), {'id': 1, 'size': 10, 'x': 2, 'y': 1})

    def test_update_empty(self):
        s = Square(5)
        s.update()

    def test_update_89(self):
        s = Square(5)
        s.update(89)
        self.assertEqual(s.id, 89)

    def test_update_89_1(self):
        s = Square(5)
        s.update(89, 1)
        self.assertEqual(s.size, 1)

    def test_update_89_1_2(self):
        s = Square(5)
        s.update(89, 1, 2)
        self.assertEqual(s.x, 2)

    def test_update_89_1_2_3(self):
        s = Square(5)
        s.update(89, 1, 2, 3)
        self.assertEqual(s.y, 3)

    def test_update_kwargs_id(self):
        s = Square(5)
        s.update(**{'id': 89})
        self.assertEqual(s.id, 89)

    def test_update_kwargs_id_size(self):
        s = Square(5)
        s.update(**{'id': 89, 'size': 1})
        self.assertEqual(s.size, 1)

    def test_update_kwargs_id_size_x(self):
        s = Square(5)
        s.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.x, 2)

    def test_update_kwargs_id_size_x_y(self):
        s = Square(5)
        s.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.y, 3)

    def test_create_id(self):
        s = Square.create(**{'id': 89})
        self.assertEqual(s.id, 89)

    def test_create_id_size(self):
        s = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(s.size, 1)

    def test_create_id_size_x(self):
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.x, 2)

    def test_create_id_size_x_y(self):
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.y, 3)

    def test_save_to_file_none(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_square(self):
        Square.save_to_file([Square(1, 0, 0, 1)])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) > 0)

    def test_load_from_file_no_file(self):
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_file_exists(self):
        Square.save_to_file([Square(1, 0, 0, 1)])
        objs = Square.load_from_file()
        self.assertEqual(len(objs), 1)


if __name__ == "__main__":
    unittest.main()
