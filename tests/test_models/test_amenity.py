#!/usr/bin/python3
"""test for Amenity"""
import unittest
from models.amenity import Amenity
from datetime import datetime


class AmenityTestCase(unittest.TestCase):
    """Class for Amenity test"""

    def test_amenity(self):
        new_amenity = Amenity()
        self.assertTrue(hasattr(new_amenity, "id"))
        self.assertTrue(hasattr(new_amenity, "created_at"))
        self.assertTrue(hasattr(new_amenity, "updated_at"))
        self.assertTrue(hasattr(new_amenity, "name"))

        self.assertIsInstance(new_amenity.id, str)
        self.assertIsInstance(new_amenity.created_at, datetime)
        self.assertIsInstance(new_amenity.updated_at, datetime)
        self.assertIsInstance(new_amenity.name, str)


if __name__ == '__main__':
    unittest.main()
