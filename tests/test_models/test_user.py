#!/usr/bin/python3
"""Test for User"""
import unittest
from models.user import User
from datetime import datetime


class UserTestCase(unittest.TestCase):
    """Class for User test"""

    def test_user(self):
        new_user = User()
        self.assertTrue(hasattr(new_user, "id"))
        self.assertTrue(hasattr(new_user, "created_at"))
        self.assertTrue(hasattr(new_user, "updated_at"))
        self.assertTrue(hasattr(new_user, "email"))
        self.assertTrue(hasattr(new_user, "password"))
        self.assertTrue(hasattr(new_user, "first_name"))
        self.assertTrue(hasattr(new_user, "last_name"))

        self.assertIsInstance(new_user.id, str)
        self.assertIsInstance(new_user.created_at, datetime)
        self.assertIsInstance(new_user.updated_at, datetime)
        self.assertIsInstance(new_user.email, str)
        self.assertIsInstance(new_user.password, str)
        self.assertIsInstance(new_user.first_name, str)
        self.assertIsInstance(new_user.last_name, str)


if __name__ == '__main__':
    unittest.main()
