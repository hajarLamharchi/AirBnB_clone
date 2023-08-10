"""Defines the class testUser"""
import unittest
from models.user import User
from models.base_model import BaseModel


class testUser(unittest.TestCase):
    """Defines the test cases for the class User"""
    def test_user_subclass(self):
        """checks if User is a subclass of BaseModel"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_user_attribute(self):
        """checks if the class user have all the attributes"""
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_user_attr_type(self):
        """checks if the attributes are of type string"""
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

    def test_user_attr_default_value(self):
        """checks the defaults value of the attributes"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")


if __name__ == "__main__":
    unittest.main()
