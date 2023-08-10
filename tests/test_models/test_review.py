"""Defines the class testReview"""
import unittest
from models.base_model import BaseModel
from models.review import Review


class testReview(unittest.TestCase):
    """Defines the test cases for the class Review"""
    def test_review_subclass(self):
        """checks if the class Review inherits from BaseModel"""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_review_attributes(self):
        """checks if the attributes exist"""
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))

    def test_review_attr_type(self):
        """checks the type of the attributes"""
        review = Review()
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)

    def test_review_attr_default_value(self):
        """checks the default value of the attributes"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == "__main__":
    unittest.main()
