#!/usr/bin/python3
"""test for Review"""
import unittest
from models.review import Review
from datetime import datetime


class ReviewTestCase(unittest.TestCase):
    """Class for Review test"""

    def test_review(self):
        new_review = Review()
        self.assertTrue(hasattr(new_review, "id"))
        self.assertTrue(hasattr(new_review, "created_at"))
        self.assertTrue(hasattr(new_review, "updated_at"))
        self.assertTrue(hasattr(new_review, "place_id"))
        self.assertTrue(hasattr(new_review, "user_id"))
        self.assertTrue(hasattr(new_review, "text"))

        self.assertIsInstance(new_review.id, str)
        self.assertIsInstance(new_review.created_at, datetime)
        self.assertIsInstance(new_review.updated_at, datetime)
        self.assertIsInstance(new_review.place_id, str)
        self.assertIsInstance(new_review.user_id, str)
        self.assertIsInstance(new_review.text, str)


if __name__ == '__main__':
    unittest.main()
