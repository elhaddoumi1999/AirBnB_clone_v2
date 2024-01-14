#!/usr/bin/python3
"""test for Place"""
import unittest
from models.place import Place
from datetime import datetime


class PlaceTestCase(unittest.TestCase):
    """Class for Place test"""

    def test_place(self):
        new_place = Place()
        self.assertTrue(hasattr(new_place, "id"))
        self.assertTrue(hasattr(new_place, "created_at"))
        self.assertTrue(hasattr(new_place, "updated_at"))
        self.assertTrue(hasattr(new_place, "city_id"))
        self.assertTrue(hasattr(new_place, "user_id"))
        self.assertTrue(hasattr(new_place, "name"))
        self.assertTrue(hasattr(new_place, "description"))
        self.assertTrue(hasattr(new_place, "number_rooms"))
        self.assertTrue(hasattr(new_place, "number_bathrooms"))
        self.assertTrue(hasattr(new_place, "max_guest"))
        self.assertTrue(hasattr(new_place, "price_by_night"))
        self.assertTrue(hasattr(new_place, "latitude"))
        self.assertTrue(hasattr(new_place, "longitude"))
        self.assertTrue(hasattr(new_place, "amenity_ids"))

        self.assertIsInstance(new_place.id, str)
        self.assertIsInstance(new_place.created_at, datetime)
        self.assertIsInstance(new_place.updated_at, datetime)
        self.assertIsInstance(new_place.city_id, str)
        self.assertIsInstance(new_place.user_id, str)
        self.assertIsInstance(new_place.name, str)
        self.assertIsInstance(new_place.description, str)
        self.assertIsInstance(new_place.number_rooms, int)
        self.assertIsInstance(new_place.number_bathrooms, int)
        self.assertIsInstance(new_place.max_guest, int)
        self.assertIsInstance(new_place.price_by_night, int)
        self.assertIsInstance(new_place.latitude, float)
        self.assertIsInstance(new_place.longitude, float)
        self.assertIsInstance(new_place.amenity_ids, list)


if __name__ == '__main__':
    unittest.main()
