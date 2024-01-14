#!/usr/bin/python3
"""test for City"""
import unittest
from models.city import City
from datetime import datetime


class CityTestCase(unittest.TestCase):
    """Class for City test"""

    def test_city(self):
        new_city = City()
        self.assertTrue(hasattr(new_city, "id"))
        self.assertTrue(hasattr(new_city, "created_at"))
        self.assertTrue(hasattr(new_city, "updated_at"))
        self.assertTrue(hasattr(new_city, "state_id"))
        self.assertTrue(hasattr(new_city, "name"))

        self.assertIsInstance(new_city.id, str)
        self.assertIsInstance(new_city.created_at, datetime)
        self.assertIsInstance(new_city.updated_at, datetime)
        self.assertIsInstance(new_city.state_id, str)
        self.assertIsInstance(new_city.name, str)


if __name__ == '__main__':
    unittest.main()
