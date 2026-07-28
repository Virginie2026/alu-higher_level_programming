#!/usr/bin/python3
"""Unittest module for the Base class."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Tests for the Base class functionality."""

    def setUp(self):
        """Reset private instance attribute before each test."""
        Base._Base__nb_objects = 0

    def test_auto_id(self):
        """Test automatic ID incrementation."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_custom_id(self):
        """Test assigning custom ID."""
        b3 = Base(89)
        self.assertEqual(b3.id, 89)

    def test_id_after_custom_id(self):
        """Test auto ID increment after custom ID."""
        b1 = Base()
        b2 = Base(89)
        b3 = Base()
        self.assertEqual(b3.id, 2)


if __name__ == '__main__':
    unittest.main()
