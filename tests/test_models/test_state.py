#!/usr/bin/python3
"""test for State"""
import unittest
from models.state import State
from datetime import datetime


class StateTestCase(unittest.TestCase):
    """Class for State test"""

    def test_state(self):
        new_state = State()
        self.assertTrue(hasattr(new_state, "id"))
        self.assertTrue(hasattr(new_state, "created_at"))
        self.assertTrue(hasattr(new_state, "updated_at"))
        self.assertTrue(hasattr(new_state, "name"))

        self.assertIsInstance(new_state.id, str)
        self.assertIsInstance(new_state.created_at, datetime)
        self.assertIsInstance(new_state.updated_at, datetime)
        self.assertIsInstance(new_state.name, str)


if __name__ == '__main__':
    unittest.main()
