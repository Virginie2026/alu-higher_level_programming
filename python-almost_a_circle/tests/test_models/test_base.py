#!/usr/bin/python3
"""Unit tests for the Base class."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def setUp(self):
        """Reset the Base object counter before each test."""
        Base._Base__nb_objects = 0

    def test_auto_id(self):
        """Test automatic ID incrementation."""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_auto_id_increment(self):
        """Test automatic ID incrementation across multiple
        instances."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_custom_id(self):
        """Test assigning a custom ID."""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_id_after_custom_id(self):
        """Test that auto ID increment continues normally after a
        custom ID is used."""
        Base(89)
        b = Base()
        self.assertEqual(b.id, 1)

    def test_to_json_string_none(self):
        """Test to_json_string with None."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """Test to_json_string with an empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_list(self):
        """Test to_json_string with a list of dictionaries."""
        result = Base.to_json_string([{"id": 12}])
        self.assertEqual(result, '[{"id": 12}]')

    def test_to_json_string_returns_str(self):
        """Test that to_json_string returns a string."""
        result = Base.to_json_string([{"id": 12}])
        self.assertIsInstance(result, str)

    def test_from_json_string_none(self):
        """Test from_json_string with None."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Test from_json_string with an empty string."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_valid(self):
        """Test from_json_string with a valid JSON string."""
        result = Base.from_json_string('[{"id": 89}]')
        self.assertEqual(result, [{"id": 89}])

    def test_from_json_string_returns_list(self):
        """Test that from_json_string returns a list."""
        result = Base.from_json_string('[{"id": 89}]')
        self.assertIsInstance(result, list)


if __name__ == "__main__":
    unittest.main()
